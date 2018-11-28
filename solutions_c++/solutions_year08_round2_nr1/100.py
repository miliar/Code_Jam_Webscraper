#include <stdio.h>
#include <string>

#define maxn 100010
#define maxl 3

int n;
int A, B, C, D, mod;
int x, y;
long long c[maxn][maxl+1][maxl][maxl];

int main()
{
	freopen("triang.in", "r", stdin);
	freopen("triang.out", "w", stdout);

	int T, i, j, k, k2;

	for (scanf("%d ", &T); T; T--)
	{
		scanf("%d %d %d %d %d %d %d %d ", &n, &A, &B, &C, &D, &x, &y, &mod);

		memset(c, 0, sizeof(c));

		c[0][0][0][0] = 1;

		for (i=0; i<n; i++) 
		{
			for (j=0; j<maxl+1; j++)
				for (k=0; k<maxl; k++)
					for (k2=0; k2<maxl; k2++) 
					{
						if (j < maxl) c[i+1][j+1][(k+x)%maxl][(k2+y)%maxl] += c[i][j][k][k2];
						c[i+1][j][k][k2] += c[i][j][k][k2];
					}

			x = (1LL * A * x + B) % mod;
			y = (1LL * C * y + D) % mod;
		}

		printf("%lld\n", c[n][3][0][0]);
	}

	return 0;
}
