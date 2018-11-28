#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int T, N, K, data[16][25];
int dp[16][1<<16];
bool match(int u, int v)
{
	for (int i = 0; i < K; i++)
		if (data[v][i] <= data[u][i])
			return false;
	return true;
}

int DP(int u, int k)
{
	if (dp[u][k] == -1)
	{
		dp[u][k] = 999999999;
		for (int v = 0; v < N; v++) if (k & (1<<v))
		{
			if (match(u, v))
				dp[u][k] = min(dp[u][k], DP(v, k & ~(1<<u)));
			dp[u][k] = min(dp[u][k], 1+DP(v, k & ~(1<<u)));
		}
	}
	return dp[u][k];
}
int main()
{
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d%d", &N, &K);
		for (int i = 0; i < N; i++)
			for (int j = 0; j < K; j++)
				scanf("%d", &data[i][j]);
		memset(dp, -1, sizeof dp);
		for (int i = 0; i < N; i++)
			dp[i][1<<i] = 1;
		int best = 999999999;
		for (int i = 0; i < N; i++)
			best = min(best, DP(i, (1<<N)-1));
		printf("Case #%d: %d\n", t, best);
	}
}
