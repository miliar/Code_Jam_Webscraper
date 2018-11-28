#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define INF 0x3fffffff
int f[110][265];
int main()
{
	int T, tcnt = 1;
	freopen("B-large.in", "r", stdin);
	freopen("bLarge.out", "w", stdout); 
	scanf("%d", &T);
	while (T--)
	{
		int N, M, D, I;
		int i, j, k, v[110], tmp[265];
		scanf("%d%d%d%d", &D, &I, &M, &N);
		//printf("%d %d\n", M, N);
		for (i = 0; i < N; i++)
			scanf("%d", &v[i]);
		for (i = 0; i < N; i++)
			for (j = 0; j <= 255; j++)
				f[i][j] = INF;
		for (j = 0; j <= 255; j++)
		{
			f[0][j] = abs(j - v[0]);
		}
		f[0][256] = D;
		for (i = 1; i < N; i++)
		{
			for (j = 0; j <= 255; j++)
			{
				tmp[j] = f[i - 1][j];
				for (k = 0; k <= 255; k++)
					if (k != j && M)
						tmp[j] <?= f[i - 1][k] + ((abs(k - j) - 1)/ M + 1) * I;
				tmp[j] <?= f[i - 1][256] + I;
			}
			for (j = 0; j <= 255; j++)
			{
				f[i][j] = tmp[j] + D;
				for (k = 0; k <= 255; k++)
					if (abs(k - j) <= M)
					{
						f[i][j] <?= tmp[k] + abs(j - v[i]);
					}
				f[i][j] <?= f[i - 1][256] + abs(j - v[i]);
			}
			f[i][256] = f[i - 1][256] + D;
		}
		int ans = INF;
		for (j = 0; j <= 255; j++)
			ans <?= f[N - 1][j];
		printf("Case #%d: %d\n", tcnt, ans);
		tcnt++;
	}
	return 0;
}
