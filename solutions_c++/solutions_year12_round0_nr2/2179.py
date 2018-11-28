#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <map>
using namespace std;

int dp[105][105];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	int ii;
	for(ii = 1; ii <= tt; ii++)
	{
		int n, s, p;
		int m[105];
		int i;
		cin >> n >> s >> p;
		memset(dp, -1, sizeof(dp));
		dp[0][0] = 0;
		for(i = 1; i <= n; i++)
		{
			cin >> m[i];
			int j;
			for(j = 0; j <= i; j++)
			{
				int j1, j2;
				for(j1 = 0; j1 <= 10; j1++)
				{
					for(j2 = 0; j2 <= 10; j2++)
					{
						int j3 = m[i] - j1 - j2;
						if(j3 < 0 || j3 > 10) continue;
						int dif = max(max(j1, j2), j3) - min(min(j1, j2), j3);
						if(dif > 2) continue;
						if(dif == 2 && j == 0) continue;
						int j0 = j;
						if(dif == 2) j0--;
						int t = dp[i - 1][j0];
						if(t != -1)
						{
							if(max(max(j1, j2), j3) >= p) t++;
							if(t > dp[i][j])
							{
								dp[i][j] = t;
							}
						}
					}
				}
			}
		}
		cout << "Case #" << ii << ": " << dp[n][s] << endl;
	}
	return 0;
}
