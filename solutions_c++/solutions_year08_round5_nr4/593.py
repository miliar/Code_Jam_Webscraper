#include <stdio.h>
#include <string>

#define maxn 110
#define mod 10007

int n, m, l;
int a[maxn][maxn], d[maxn][maxn];

int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);

	int t, T, i, j, x, y;

	scanf("%d ", &T);

	for (t=1; t<=T; t++)
	{
		scanf("%d %d %d ", &n, &m, &l);

		memset(a, 0, sizeof(a));
		memset(d, 0, sizeof(d));

		for (i=1; i<=l; i++) 
		{
			scanf("%d %d ", &x, &y);
			a[x][y] = 1;
		}

		if (!a[1][1]) d[1][1] = 1;

		for (i=1; i<=n; i++)
			for (j=1; j<=m; j++) 
				if (!a[i][j])
				{
					if (i>2 && j>1) d[i][j] = d[i-2][j-1];
					if (i>1 && j>2) d[i][j] = (d[i][j] + d[i-1][j-2]) % mod;
				}

		printf("Case #%d: %d\n", t, d[n][m]);
	}

	return 0;
}
