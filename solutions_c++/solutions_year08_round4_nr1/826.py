#include <iostream>
#include <cstdio>
using namespace std;

#define INF 20000
struct Node
{
	int G;
	int C;
};
Node node[10010];
int leaf[10010];
int dp[10010][2];
int M, V;

int min3(int a, int b, int c)
{
	return min(a, b < c ? b : c);
}

void dfs(int v)
{
	if (v > (M - 1) / 2)
	{
		dp[v][leaf[v]] = 0;
		dp[v][1 - leaf[v]] = INF;
	}
	else
	{
		dfs(v * 2); dfs(v * 2 + 1);
		if (node[v].C == 0)
		{
			if (node[v].G == 1)
			{
				dp[v][0] = min3(dp[v * 2][0] + dp[v * 2 + 1][0], dp[v * 2][0] + dp[v * 2 + 1][1], dp[v * 2][1] + dp[v * 2 + 1][0]);
				dp[v][1] = dp[v * 2][1] + dp[v * 2 + 1][1];
			}
			else
			{
				dp[v][1] = min3(dp[v * 2][1] + dp[v * 2 + 1][1], dp[v * 2][0] + dp[v * 2 + 1][1], dp[v * 2][1] + dp[v * 2 + 1][0]);
				dp[v][0] = dp[v * 2][0] + dp[v * 2 + 1][0];
			}
		}
		else
		{
			int tmp1, tmp2, tmp3, tmp4;
			tmp1 = min3(dp[v * 2][0] + dp[v * 2 + 1][0], dp[v * 2][0] + dp[v * 2 + 1][1], dp[v * 2][1] + dp[v * 2 + 1][0]);
			tmp2 = dp[v * 2][1] + dp[v * 2 + 1][1];
			tmp3 = min3(dp[v * 2][1] + dp[v * 2 + 1][1], dp[v * 2][0] + dp[v * 2 + 1][1], dp[v * 2][1] + dp[v * 2 + 1][0]);
			tmp4 = dp[v * 2][0] + dp[v * 2 + 1][0];
			if (node[v].G == 1)
			{
				dp[v][0] = min(tmp1, tmp4 + 1);
				dp[v][1] = min(tmp2, tmp3 + 1);
			}
			else
			{
				dp[v][1] = min(tmp3, tmp2 + 1);
				dp[v][0] = min(tmp4, tmp1 + 1);
			}	
		}
	}
}

int main()
{
	int T, t, i, j;
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		memset(dp, 0, sizeof(dp));
		scanf("%d%d", &M, &V);
		for (i = 1; i <= (M - 1) / 2; i++)
			scanf("%d%d", &node[i].G, &node[i].C);
		for (i = (M - 1) / 2 + 1; i <= M; i++)
			scanf("%d", &leaf[i]);
		dfs(1);
		if (dp[1][V] >= INF)
			printf("Case #%d: IMPOSSIBLE\n", t);
		else
			printf("Case #%d: %d\n", t, dp[1][V]);
	}
	return 0;
}