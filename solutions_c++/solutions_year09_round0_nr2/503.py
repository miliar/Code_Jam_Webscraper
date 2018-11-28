#include <cstdio>

#define For(i,n) for (int i = 0; i < n; ++i)

int T, n, m, d[100][100], a[100][100], b[10000], c;

int f(int x, int y) {
	if (a[x][y] ^ -1) return a[x][y];
	int r = -1, t = d[x][y];
	if (x && d[x - 1][y] < t) t = d[x - 1][y], r = 0;
	if (y && d[x][y - 1] < t) t = d[x][y - 1], r = 1;
	if (y + 1 < m && d[x][y + 1] < t) t = d[x][y + 1], r = 2;
	if (x + 1 < n && d[x + 1][y] < t) t = d[x + 1][y], r = 3;
	if (r == -1) return a[x][y] = x*m + y;
	if (r == 0) return a[x][y] = f(x - 1, y);
	if (r == 1) return a[x][y] = f(x, y - 1);
	if (r == 2) return a[x][y] = f(x, y + 1);
	if (r == 3) return a[x][y] = f(x + 1, y);
	return 0;
}

int main() {
	scanf("%d", &T);
	For(r,T) {
		printf("Case #%d:\n", r + 1);
		scanf("%d%d", &n, &m);
		For(i,n) For(j,m) scanf("%d", d[i] + j);
		For(i,n) For(j,m) a[i][j] = b[i*m + j] = -1;
		For(i,n) For(j,m) a[i][j] = f(i, j);
		c = 'a' - 1;
		For(i,n) For(j,m) if (b[a[i][j]] == -1) b[a[i][j]] = ++c;
		For(i,n) For(j,m) printf("%c%c", b[a[i][j]], j + 1 == m ? '\n' : ' ');
	}
	return 0;
}
