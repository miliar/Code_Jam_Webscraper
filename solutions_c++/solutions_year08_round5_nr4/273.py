#include <cstdio>
#include <cstring>

#define MAXN 128
#define MOD 10007

int dp[MAXN][MAXN], r[MAXN][MAXN];

void readAndSolve()
{
	int N;

	scanf("%d", &N);

	for (int i = 1; i <= N; i++)
	{
		memset(dp, 0, sizeof(dp));
		memset(r, 0, sizeof(r));
		int R, H, W;
		scanf("%d %d %d", &H, &W, &R);
		for (int j = 0; j < R; j++)
		{
			int x, y;
			scanf("%d %d", &x, &y), x--, y--;
			r[x][y] = 1;
		}

		dp[0][0] = 1;
		for (int i = 1; i < H; i++)
			for (int j = 0; j < W; j++)
			{
				if (r[i][j])
					continue;
				int l = i - 1, c = j - 2;
				if (l >= 0 && c >= 0)
					dp[i][j] += dp[l][c], dp[i][j] %= MOD;
				l = i - 2, c = j - 1;
				if (l >= 0 && c >= 0)
					dp[i][j] += dp[l][c], dp[i][j] %= MOD;
			}

		printf("Case #%d: %d\n", i, dp[H - 1][W - 1]);
	}
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);

	readAndSolve();

	return 0;
}