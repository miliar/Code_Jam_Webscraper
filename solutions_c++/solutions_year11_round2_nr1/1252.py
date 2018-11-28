#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	char c;
	int t, n;

	cin >> t;
	for(int tc = 1; tc <= t; tc++)
	{
		cin >> n;
		
		vector<int> wins(n, 0);
		vector<int> loses(n, 0);
		vector<vector<char> > s(n, vector<char>(n));
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cin >> s[i][j];
				if (s[i][j] == '1')
				{
					wins[i]++;
				}
				else if (s[i][j] == '0')
				{
					loses[i]++;
				}
			}
		}

		vector<double> wp(n);
		vector<double> owp(n);
		vector<double> oowp(n);
		for (int j = 0; j < n; j++)
		{
			int cnt = 0;

			for (int i = 0; i < n; i++)
			{
				if (s[i][j] != '.' && i != j)
				{
					if (s[i][j] == '1')
					{
						owp[j] += (wins[i] - 1.0) / (wins[i] + loses[i] - 1.0);
					}
					else if (s[i][j] == '0')
					{
						owp[j] += wins[i] / (wins[i] + loses[i] - 1.0);
					}
					cnt++;
				}
			}
			owp[j] /= cnt;
			wp[j] = wins[j] / (wins[j] + loses[j] + .0);
		}

		for (int i = 0; i < n; i++)
		{
			int cnt = 0;
			for (int j = 0; j < n; j++)
			{
				if (s[i][j] != '.' && i != j)
				{
					oowp[i] += owp[j];
					cnt++;
				}
			}
			oowp[i] /= cnt;
		}

		cout << "Case #" << tc << ":" << endl;
		for (int i = 0; i < n; i++)
		{
			cout << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;
		}
	}

	return 0;
}