#include <iostream>
#include <vector>
#include <string>

using namespace std;

double ww[110][110];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tc = 0; tc < t; tc++)
	{
		int n;
		cin >> n;
		vector <string> arr(n);
		for(int i = 0; i < n; i++)
			cin >> arr[i];
		vector <double> wp(n), owp(n), oowp(n);
		for(int i = 0; i < n; i++)
		{
			int w = 0, t = 0;
			for(int j = 0; j < n; j++)
			{
				if(arr[i][j] == '.')
					continue;
				t++;
				if(arr[i][j] == '1')
					w++;
			}
			wp[i] = double(w) / t;
		}
		for(int i = 0; i < n; i++)
		{
			int op = 0;
			for(int j = 0; j < n; j++)
				if(arr[i][j] != '.')
				{
					op++;
					int w = 0, t = 0;
					for(int k = 0; k < n; k++)
						if(arr[j][k] != '.' && i != k)
						{
							if(arr[j][k] == '1')
								w++;
							t++;
						}
					owp[i] += double(w) / t;
				}
			owp[i] /= op;
		}
		for(int i = 0; i < n; i++)
		{
			int op = 0;
			for(int j = 0; j < n; j++)
				if(arr[i][j] != '.')
				{
					op++;
					double x = 0;
					int t = 0;
					for(int k = 0; k < n; k++)
						if(arr[j][k] != '.')
						{
							t++;
							int tt = 0, w = 0;
							for(int l = 0; l < n; l++)
							{
								
								if(arr[k][l] != '.' && l != j)
								{
									if(arr[k][l] == '1')
										w++;
									tt++;
								}
								
							}
							x += double(w) / tt;
						}
					oowp[i] += x / t;
				}
			oowp[i] /= op;
		}
		printf("Case #%d:\n", tc + 1);
		for(int i = 0; i < n; i++)
			printf("%.9lf\n", 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}
	return 0;
}