#include <cstdio>
#include <memory.h>
#include <cmath>

using namespace std;

int dp[101][256];
int data[101];

int main()
{
	int tc;
	scanf("%d", &tc);
	int ti;
	for (ti = 1;ti <= tc;ti++)
	{
		printf("Case #%d: ", ti);

		memset(dp, 0x7F, sizeof(dp));

		memset(dp[0], 0, sizeof(dp[0]));

		int del, ins, threshold, n;

		scanf("%d %d %d %d", &del, &ins, &threshold, &n);
		int i;
		for (i = 0;i < n;i++)
			scanf("%d", &data[i]);

		int prev, next;
		for (i = 0;i < n;i++)
		{
			for (prev = 0;prev <= 255;prev++)
			{
				if (dp[i][prev] == 0x7F7F7F7F)
					continue;

				if (dp[i + 1][prev] > dp[i][prev] + del)
					dp[i + 1][prev] = dp[i][prev] + del;

				for (next = 0;next <= 255;next++)
				{
					int diff = prev - next;
					if (diff < 0) diff *= -1;

					if (threshold == 0 && diff != 0)
						continue;

					int to_insert = 0;
					if (threshold != 0 && diff != 0)
						to_insert = (diff - 1) / threshold;

					int cost = (data[i] - next);
					if (cost < 0) cost *= -1;
					cost += to_insert * ins;

					if (dp[i + 1][next] > dp[i][prev] + cost)
						dp[i + 1][next] = dp[i][prev] + cost;
				}
			}
		}
		int ans = 0x7F7F7F7F;
		for (i = 0;i <= 255;i++)
			if (ans > dp[n][i])
				ans = dp[n][i];
		printf("%d\n", ans);
		fprintf(stderr, "%d\n", ti);
	}
	return 0;
}
