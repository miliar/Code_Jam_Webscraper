#include <cstdio>
#include <algorithm>

using namespace std;

const char dir[] = "-|\\/";
const int dx[4] = {0, 1, 1, 1};
const int dy[4] = {1, 0, 1, -1};
const int MAXN = 128;

char buf[MAXN][MAXN];
int a[MAXN][MAXN], b[MAXN][MAXN];

int main() {
	int re, r, c, x, y, n, ans;

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%d%d", &r, &c);
		for (int i = 0; i < r; ++i) {
			scanf("%s", buf[i]);
			for (int j = 0; j < c; ++j) {
				a[i][j] = find(dir, dir + 4, buf[i][j]) - dir;
			}
		}

		n = r * c;
		ans = 0;
		for (int m = 0; m < (1 << n); ++m) {
			for (int i = 0; i < r; ++i) {
				for (int j = 0; j < c; ++j) {
					b[i][j] = 0;
				}
			}
			bool flag = true;
			for (int i = 0; flag && i < r; ++i) {
				for (int j = 0; flag && j < c; ++j) {
					if ((m >> (i * c + j)) & 1) {
						x = (i + dx[a[i][j]] + r) % r;
						y = (j + dy[a[i][j]] + c) % c;
					} else {
						x = (i - dx[a[i][j]] + r) % r;
						y = (j - dy[a[i][j]] + c) % c;
					}
					if (++b[x][y] > 1) {
						flag = false;
					}
				}
			}
			if (flag) {
				++ans;
			}
		}
		printf("Case #%d: %d\n", ri, ans % 1000003);
	}

	return 0;
}

