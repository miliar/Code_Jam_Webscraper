#include <stdio.h>
#define inf 1000000000

int d[102][102];
char s[102][102];
int di[4] = {-1, 0, 0, 1};
int dj[4] = {0, -1, 1, 0};
int main()
{
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	char b;
	int T, t, n, m, p, q, i, j, k, l;
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%d%d", &n, &m);
		for (i = 0; i <= n+1; i++)
			for (j = 0; j <= m+1; j++)
			{
				d[i][j] = inf;
				s[i][j] = 0;
			}
		for (i = 1; i <= n; i++)
			for (j = 1; j <= m; j++)
				scanf("%d", d[i]+j);
		b = 'a';
		for (i = 1; i <= n; i++)
			for (j = 1; j <= m; j++)
			{
				p = i;
				q = j;
				while (1)
				{
					for (l = k = 0; k < 4; k++)
						if (d[p+di[k]][q+dj[k]] < d[p+di[l]][q+dj[l]])
							l = k;
					if (d[p+di[l]][q+dj[l]] >= d[p][q])
						break;
					p += di[l];
					q += dj[l];
				}
				if (s[p][q] == 0)
					s[p][q] = b++;
				s[i][j] = s[p][q];
			}
		printf("Case #%d:\n", t);
		for (i = 1; i <= n; i++)
		{
			for (j = 1; j < m; j++)
				printf("%c ", s[i][j]);
			printf("%c\n", s[i][j]);
		}
	}
	return 0;
}

