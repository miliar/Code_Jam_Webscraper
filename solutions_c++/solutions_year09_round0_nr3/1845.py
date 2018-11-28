#include <stdio.h>
#include <string.h>

int d[510][30];
char s[] = "#welcome to code jam\0", p[510];
int main()
{
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int T, t, n, m, i, j;
	scanf("%d", &T);
	getchar();
	for (t = 1; t <= T; t++)
	{
		p[0] = '#';
		gets(p+1);
		n = strlen(p)-1;
		m = strlen(s)-1;
		for (i = 0; i <= n; i++)
			d[i][0] = 1;
		for (i = 1; i <= n; i++)
			for (j = 1; j <= i && j <= m; j++)
			{
				d[i][j] = d[i-1][j];
				if (p[i] == s[j])
					d[i][j] = (d[i][j]+d[i-1][j-1])%1000;
			}
		printf("Case #%d: %04d\n", t, d[n][m]);
	}
	return 0;
}

