#include <cstdio>
#include <algorithm>
#include <memory.h>

using namespace std;

int cost[1024];
int dp[2048][11];
int N;

int main()
{
	int tc;
	scanf("%d", &tc);

	int ti;
	for (ti = 1;ti <= tc;ti++)
	{
		printf("Case #%d: ", ti);
		scanf("%d", &N);
		int i;
		memset(dp, 0x7F, sizeof(dp));
		for (i = 0;i < (1 << N);i++)
		{
			int miss;
			scanf("%d", &miss);
			dp[(1 << N) - 1 + i][miss] = 0;
		}
		int j;
		for (i = N - 1;i >= 0;i--)
		{
			int prev = 0;
			if (i)
				prev = (1 << i) - 1;
			for (j = 0;j < (1 << i);j++)
				scanf("%d", &cost[prev + j]);
		}

		for (i = (1 << N) - 2;i >= 0;i--)
		{
			int left, right;
			int lv = i * 2 + 1, rv = i * 2 + 2;
			for (left = 0;left <= N;left++)
			{
				if (dp[lv][left] == 0x7F7F7F7F)
					continue;
				for (right = 0;right <= N;right++)
				{
					if (dp[rv][right] == 0x7F7F7F7F)
						continue;

					int m = min(left, right);
					// see this
					if (dp[i][m] > dp[lv][left] + dp[rv][right] + cost[i])
						dp[i][m] = dp[lv][left] + dp[rv][right] + cost[i];
					// otherwise
					if (m > 0 && dp[i][m - 1] > dp[lv][left] + dp[rv][right])
						dp[i][m - 1] = dp[lv][left] + dp[rv][right];
				}
			}
		}

		int ans = 0x7F7F7F7F;
		for (i = 0;i <= 10;i++)
			if (ans > dp[0][i])
				ans = dp[0][i];
		printf("%d\n", ans);
		fprintf(stderr, "Case #%d: %d\n", ti, ans);
	}
	return 0;
}
