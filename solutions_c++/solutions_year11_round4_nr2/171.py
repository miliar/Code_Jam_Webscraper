#include <cstdio>

int T, n, m, d[1024][1024], a[1024][1024], b[1024][1024], tx, ty, ans, ma[1024][1024], tm, li, hi, lj, hj, sz, ci, cj;
char s[1024];

void check() {
	tx = a[hi][hj] - a[li - 1][hj] - a[hi][lj - 1] + a[li - 1][lj - 1];
	ty = b[hi][hj] - b[li - 1][hj] - b[hi][lj - 1] + b[li - 1][lj - 1];
	tm = ma[hi][hj] - ma[li - 1][hj] - ma[hi][lj - 1] + ma[li - 1][lj - 1];
	tx -= d[li][lj]*li + d[li][hj]*li + d[hi][lj]*hi + d[hi][hj]*hi;
	ty -= d[li][lj]*lj + d[li][hj]*hj + d[hi][lj]*lj + d[hi][hj]*hj;
	tm -= d[li][lj] + d[li][hj] + d[hi][lj] + d[hi][hj];
	if (2*tx == ci*tm && 2*ty == cj*tm) {
		ans = sz;
//		printf("? %d %d\n", ci, cj);
	}
}

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d:", r);
		scanf("%d%d%*d", &n, &m);
		for (int i = 0; i <= n; ++i)
			for (int j = 0; j <= m; ++j)
				a[i][j] = b[i][j] = ma[i][j] = 0;
		for (int i = 1; i <= n; ++i) {
			scanf("%s", s);
			for (int j = 1; j <= m; ++j) {
				d[i][j] = s[j - 1] - '0';
				a[i][j] = d[i][j]*i + a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1];
				b[i][j] = d[i][j]*j + b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1];
				ma[i][j] = d[i][j] + ma[i - 1][j] + ma[i][j - 1] - ma[i - 1][j - 1];
			}
		}
		ans = 2;
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= m; ++j)
				for (int k = (ans + 1 >> 1); i - k >= 1 && i + k <= n && j - k >= 1 && j + k <= m; ++k) {
					li = i - k, hi = i + k, lj = j - k, hj = j + k, sz = 2*k + 1;
					ci = 2*i, cj = 2*j;
					check();
				}
		for (int i = 3; i <= 2*n - 1; i += 2)
			for (int j = 3; j <= 2*m - 1; j += 2)
				for (int k = (ans >> 1)*2 + 1; i - k >= 2 && i + k <= 2*n && j - k >= 2 && j + k <= 2*m; k += 2) {
					li = (i - k >> 1), hi = (i + k >> 1), lj = (j - k >> 1), hj = (j + k >> 1), sz = k + 1;
					ci = i, cj = j;
					check();
				}
		if (ans == 2)
			puts(" IMPOSSIBLE");
		else
			printf(" %d\n", ans);
	}
	return 0;
}
