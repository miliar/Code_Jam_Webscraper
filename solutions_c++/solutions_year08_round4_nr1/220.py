#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>

#define INF 1000000000

using namespace std;

int gate[10010];
int value[10010];
int change[10010];
int dp[10010][2];

int main()
{
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; ++tt)
	{
		int m, v;
		cin >> m >> v;
		for(int i = 1; i <= (m - 1) / 2; ++i) scanf("%d %d", gate + i, change + i);
		memset(value, -1, 10010 * 4);
		for(int i = 0; i <= m; ++i) dp[i][0] = dp[i][1] = INF;
		for(int i = 1; i <= (m + 1) / 2; ++i) scanf("%d", value + i + (m - 1) / 2);
		for(int i = m; i >= 1; --i)
		{
			if(value[i] != -1) dp[i][value[i]] = 0;
			else
			{
				if(gate[i])
				{
					dp[i][0] = min(dp[i][0], min(dp[i << 1][0], dp[(i << 1) + 1][0]));
					dp[i][1] = min(dp[i][1], dp[i << 1][1] + dp[(i << 1) + 1][1]);
					if(change[i])
					{
						dp[i][0] = min(dp[i][0], dp[i << 1][0] + dp[(i << 1) + 1][0] + 1);
						dp[i][1] = min(dp[i][1], min(dp[i << 1][1], dp[(i << 1) + 1][1]) + 1);
					}
				}else
				{
					dp[i][1] = min(dp[i][1], min(dp[i << 1][1], dp[(i << 1) + 1][1]));
					dp[i][0] = min(dp[i][0], dp[i << 1][0] + dp[(i << 1) + 1][0]);
					if(change[i])
					{
						dp[i][1] = min(dp[i][1], dp[i << 1][1] + dp[(i << 1) + 1][1] + 1);
						dp[i][0] = min(dp[i][0], min(dp[i << 1][0], dp[(i << 1) + 1][0]) + 1);
					}
				}
			}
		}
		printf("Case #%d: ", tt);
		if(dp[1][v] != INF) printf("%d\n", dp[1][v]);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}