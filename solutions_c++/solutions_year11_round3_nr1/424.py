#include <stdio.h>

#define N 51

int m, n;
char a[N][N];

int cover(int r, int c)
{
	if ('#' != a[r][c]) return 1;
	if (r+1>=m || c+1>=n) return 0;
	if ('#'!=a[r][c+1] || '#'!=a[r+1][c] || '#'!=a[r+1][c+1]) return 0;
	a[r][c] = '/';
	a[r][c+1] = '\\';
	a[r+1][c] = '\\';
	a[r+1][c+1] = '/';
	return 1;
}

int go()
{
	int i, j, k = 0;
	for (i = 0; i < m; ++i)
		for (j = 0; j < n; ++j)
			if ('#' == a[i][j]) ++k;
	if (k & 3) return 0;
	if (!k) return 1;
	for (i = 0; i < m; ++i)
		for (j = 0; j < n; ++j)
			if (!cover(i, j)) return 0;
	return 1;
}

int main()
{
	int T, TT;
	scanf("%d", &TT);
	for (T = 1; T <= TT; ++T)
	{
		scanf("%d%d", &m, &n);
		for (int i = 0; i < m; ++i) scanf("%s", &a[i]);
		printf("Case #%d:\n", T);
		if (go()) {
			for (int i = 0; i < m; ++i) puts(a[i]);
		} else puts("Impossible");
	}
	return 0;
}
