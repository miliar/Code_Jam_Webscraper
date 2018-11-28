#include <stdio.h>
#include <string.h>

#define MAXN 128
#define MOD 10007

char bad[MAXN][MAXN];
int tot[MAXN][MAXN];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		int N, M, R;
		scanf("%d %d %d", &N, &M, &R);
		memset(bad, 0, sizeof(bad));
		memset(tot, 0, sizeof(tot));
		N--; M--;
		tot[0][0] = 1;
		for (int i = 0; i < R; i++)
		{
			int x, y;
			scanf("%d %d", &x, &y);
			x--; y--;
			bad[x][y] = 1;
		}
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= M; j++)
			{
				if (bad[i][j]) continue;
				if (i >= 1 && j >= 2)
					tot[i][j] = tot[i - 1][j - 2];
				if (i >= 2 && j >= 1)
					tot[i][j] += tot[i - 2][j - 1],
					tot[i][j] %= MOD;
			}

		printf("Case #%d: %d\n", t, tot[N][M]);
	}
	return 0;
}
