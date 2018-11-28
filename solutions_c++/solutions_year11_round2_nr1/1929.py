#include<vector>
#include<string>
#include<map>
#include<set>
#include<utility>
#include<algorithm>
#include<cmath>
#include<iostream>
#include<cstdio>

using namespace std;

#define FOR(A,B) for(int A;A<B.size();++A)
#define X first
#define Y second
#define LI size()-1

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, n;

	cin >> t;
	for(int tc = 1; tc <= t; tc++)
	{
		cin >> n;

		vector<int> wn(n, 0);
		vector<int> ls(n, 0);
		vector<vector<char> > s(n, vector<char>(n));
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cin >> s[i][j];
				if (s[i][j] == '1')
				{
					wn[i]++;
				}
				else if (s[i][j] == '0')
				{
					ls[i]++;
				}
			}
		}

		vector<double> wp(n);
		vector<double> owp(n);
		vector<double> oowp(n);
		for (int j = 0; j < n; j++)
		{
			int count = 0;

			for (int i = 0; i < n; i++)
			{
				if (s[i][j] != '.' && i != j)
				{
					if (s[i][j] == '1')
					{
						owp[j] += (wn[i] - 1.0) / (wn[i] + ls[i] - 1.0);
					}
					else if (s[i][j] == '0')
					{
						owp[j] += wn[i] / (wn[i] + ls[i] - 1.0);
					}
					count++;
				}
			}
			owp[j] /= count;
			wp[j] = wn[j] / (wn[j] + ls[j] + .0);
		}

		for (int i = 0; i < n; i++)
		{
			int count = 0;
			for (int j = 0; j < n; j++)
			{
				if (s[i][j] != '.' && i != j)
				{
					oowp[i] += owp[j];
					count++;
				}
			}
			oowp[i] /= count;
		}

		cout << "Case #" << tc << ":" << endl;
		for (int i = 0; i < n; i++)
		{
			cout << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;
		}
	}

	return 0;
}