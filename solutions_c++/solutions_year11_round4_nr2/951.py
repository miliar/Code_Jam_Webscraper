#include <cstdio>
#include <cstring>

const int MAXN = 500 + 1;

int q, n, m, d;
int a[MAXN][MAXN];

int main() {
	scanf("%d", &q);
	for (int z = 1; z <= q; z ++) {
		scanf("%d%d%d\n", &n, &m, &d);
		for (int i = 1; i <= n; i ++) {
			for (int j = 1; j <= m; j ++) {
				char c;
				scanf("%c", &c);
				a[i][j] = d + (c - '0');
			}
			scanf("\n");
		}
		bool flag = false;
		for (int r = n; r >= 3; r --) {
			for (int x = 1; x <= n; x ++) {
				if (x + r - 1 > n) break;
				for (int y = 1; y <= m; y ++) {
					if (y + r - 1 > m) break;
					int t1 = 0, t2 = 0;
					int x1 = x + r / 2 - 1;
					int x2 = x + r / 2;
					if (r % 2 == 1) x2 ++;
					int y1 = y + r / 2 - 1;
					int y2 = y + r / 2;
					if (r % 2 == 1) y2 ++;
					if (r % 2 == 1) {
						for (int i = x; i <= x1; i ++)
							for (int j = y; j <= y + r - 1; j ++) t1 += a[i][j] * (x1 - i + 1);
						t1 -= a[x][y] * (x1 - x + 1);
						t1 -= a[x][y + r - 1] * (x1 - x + 1);
						for (int i = x2; i <= x + r - 1; i ++)
							for (int j = y; j <= y + r - 1; j ++) t2 += a[i][j] * (i - x2 + 1);
						t2 -= a[x + r - 1][y] * (x + r - x2);
						t2 -= a[x + r - 1][y + r - 1] * (x + r - x2);
						if (t1 != t2) continue;
					} else {
						for (int i = x; i <= x1; i ++)
							for (int j = y; j <= y + r - 1; j ++) t1 += a[i][j] * (2 * (x1 - i) + 1);
						t1 -= a[x][y] * (2 * (x1 - x) + 1);
						t1 -= a[x][y + r - 1] * (2 * (x1 - x) + 1);
						for (int i = x2; i <= x + r - 1; i ++)
							for (int j = y; j <= y + r - 1; j ++) t2 += a[i][j] * (2 * (i - x2) + 1);
						t2 -= a[x + r - 1][y] * (2 * (x + r - 1 - x2) + 1);
						t2 -= a[x + r - 1][y + r - 1] * (2 * (x + r - 1 - x2) + 1);					
						if (t1 != t2) continue;
					}

					t1 = t2 = 0;
					if (r % 2 == 1) {
						for (int j = y; j <= y1; j ++)
							for (int i = x; i <= x + r - 1; i ++) t1 += a[i][j] * (y1 - j + 1);
						for (int j = y2; j <= y + r - 1; j ++)
							for (int i = x; i <= x + r - 1; i ++) t2 += a[i][j] * (j - y2 + 1);
						t1 -= a[x][y] * (y1 - y + 1);
						t1 -= a[x + r - 1][y] * (y1 - y + 1);
						t2 -= a[x][y + r - 1] * (y + r - y2);
						t2 -= a[x + r - 1][y + r - 1] * (y + r - y2);
						if (t1 != t2) continue;
					} else {
						for (int j = y; j <= y1; j ++)
							for (int i = x; i <= x + r - 1; i ++) t1 += a[i][j] * (2 * (y1 - j) + 1);
						for (int j = y2; j <= y + r - 1; j ++)
							for (int i = x; i <= x + r - 1; i ++) t2 += a[i][j] * (2 * (j - y2) + 1);
						t1 -= a[x][y] * (2 * (y1 - y) + 1);
						t1 -= a[x + r - 1][y] * (2 * (y1 - y) + 1);
						t2 -= a[x][y + r - 1] * (2 * (y + r - 1 - y2) + 1);
						t2 -= a[x + r - 1][y + r - 1] * (2 * (y + r - 1- y2) + 1);
						if (t1 != t2) continue;					
					}
				
					printf("Case #%d: %d\n", z, r);
					flag = true;
					break;
				}
				if (flag) break;
			}	
			if (flag) break;
		}
		if (!flag) printf("Case #%d: IMPOSSIBLE\n", z);
	}
	return 0;
}

