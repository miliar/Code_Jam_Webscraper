#include <cstdio>
#include <cstring>

#define MAXN 16
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int M, N;
int dp[MAXN][1 << 11];
char map[MAXN][MAXN];

int solve()
{
	int res = 0;
	memset(dp, 0, sizeof(dp));

	for (int i = 0; i < M; i++)
		for (int j = 0; j < (1 << N); j++)
			for (int k = 0; k < (1 << N); k++)
			{
				if (j & k)
					continue;
				int nr = 0, flag = 0, last = -1;
				for (int p = 0; (1 << p) <= k; p++)
					if (k & (1 << p))
					{
						nr++;
						if (map[i][p] == 'x')
							flag = 1;
						if (p > 0 && last == p - 1)
							flag = 1;
						last = p;
					}
				if (flag)
					continue;
				int next = ((k << 1) | (k >> 1)) & ((1 << N) - 1);
				dp[i + 1][next] = MAX(dp[i + 1][next], dp[i][j] + nr);
				if (i + 1 == M)
					res = MAX(res, dp[i + 1][next]);
			}

	return res;
}

void readAndSolve()
{
	int C;

	scanf("%d", &C);

	for (int i = 1; i <= C; i++)
	{
		scanf("%d %d", &M, &N);

		for (int i = 0; i < M; i++)
			scanf("%s", map[i]);

		printf("Case #%d: %d\n", i, solve());
	}
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	readAndSolve();

	return 0;
}