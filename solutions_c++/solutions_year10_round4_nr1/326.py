#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

char buf[1024][1024];
int l[1024], r[1024];

#define dist(a, b) (abs((a) - n) + abs((b) - n))

int main() {
	int re, n, m, s, ans;

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%d", &n);
		gets(buf[0]);
		for (int i = 1; i <= n; ++i) {
			gets(buf[i] + 1);
			l[i] = n - i + 1;
			r[i] = n + i - 1;
		}
		for (int i = 1; i < n; ++i) {
			gets(buf[n + i] + 1);
			l[n + i] = i + 1;
			r[n + i] = n + n - i - 1;
		}
		m = n + n - 1;

		s = 100;
		for (int x = 0; x <= m; ++x) {
			int left, right;
			for (int y = 0; y <= m; ++y) {
				// printf("[%d,%d] = '%c'\n", x, y, buf[x][y]);
				bool f = true;
				int d = 0, xx = x + x, yy = y + y;
				// if (x != n || y != n) continue;
				// if (x != 3 || y != 4) continue;
				for (int i = 1; f && i <= m; ++i) {
					for (int j = l[i]; f && j <= r[i]; ++j) {
						// printf("(%d,%d) %d %d\n", i, j, xx - i, yy - j);
						// printf("'%c' %d:'%c' %d:'%c'\n", buf[i][j], dist(xx - i, j), buf[xx - i][j], dist(i, yy - j), buf[i][yy - j]);
						f &= dist(xx - i, j) >= n || buf[xx - i][j] == buf[i][j];
						f &= dist(i, yy - j) >= n || buf[i][yy - j] == buf[i][j];
						d = max(d, abs(i - x) + abs(j - y));
					}
				}
				if (f) {
					if (d + 1 < s) {
					//	printf("%d %d %d\n", x, y, d + 1);
					}
					s = min(s, d + 1);
				}
			}
		}
	//	printf("s = %d\n", s);

		ans = 0;
		for (int i = 1; i <= n; ++i) {
			ans -= i;
		}
		for (int i = 1; i < n; ++i) {
			ans -= i;
		}
		for (int i = 1; i <= s; ++i) {
			ans += i;
		}
		for (int i = 1; i < s; ++i) {
			ans += i;
		}

		printf("Case #%d: %d\n", ri, ans);
	}

	return 0;
}

