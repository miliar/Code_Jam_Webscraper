#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
int main()
{
	int T;
	scanf("%d", &T);
	int cas = 0;
	for(cas = 1; cas <= T; cas++)
	{
		int n;
		cin >> n;
		string temp(n, 'a');
		vector <string>	a(n,temp);
		int i, j;
		for(i = 0; i < n; i++)
			cin >> a[i];
		vector <int> win(n, 0);
		vector <int> played(n, 0);
		for(i = 0; i < n; i++)
			for(j = 0; j < n; j++)
				if(a[i][j] == '.')
					continue;
				else
				{
						played[i]++;
						if(a[i][j] == '1')
							win[i]++;
				}
		vector <double> owp(n, 0);
		for(i = 0; i < n; i++)
		{
				double val = 0;
				int cnt = 0;
				for(j = 0; j < n; j++)
				{
						if(a[i][j] != '.')
						{
							if(a[i][j] == '1')
								val = val + (1.0*win[j]/(played[j] - 1));	
							else if(a[i][j] == '0')
								val = val + (1.0*(win[j] - 1)/(played[j] - 1));	
							cnt++;
						}
				}
				owp[i] = val/cnt;
		}
		vector <double> oowp(n, 0);
		for(i = 0; i < n; i++)
		{
			double val = 0;
			int cnt = 0;
			for(j = 0; j < n; j++)
			{
				if(a[i][j] != '.')
				{
					val = val + owp[j];
					cnt++;	
				}
			}
			oowp[i] = val/cnt;
		}
		cout << "Case #" << cas << ":\n";
		for(i = 0; i < n; i++)
		{
			printf("%0.12lf\n", ((0.25 * win[i])/played[i]) + (0.5 * owp[i]) + (0.25*oowp[i]));
		}
	}
	return 0;
}
