#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int ss[501][501];
int sx[501][501];
int sy[501][501];
int R, C;

int s[501][501];
int x[501][501];
int y[501][501];

int d[501][501];

void acc(int a[501][501], int s[501][501]) {
	memset(s, 0, sizeof s);

	for (int i = 1; i <= R; i++)
		for (int j = 1; j <= C; j++)
			s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + a[i][j];
}

int corner(int s[501][501], int a[501][501], int x, int y, int k) {
	return s[x + k - 1][y + k - 1] - s[x - 1][y + k - 1] - s[x + k - 1][y - 1] + s[x - 1][y - 1]
		- a[x + k - 1][y + k - 1] - a[x][y + k - 1] - a[x + k - 1][y] - a[x][y];
}

void solve() {
	int ans = 0;
	for (int i = 1; i <= R; i++)
		for (int j = 1; j <= C; j++)
			for (int k = 3; k + i - 1 <= R && k + j - 1 <= C; k++) {
				int ret = corner(ss, s, i, j, k);
				int retx = corner(sx, x, i, j, k);
				int rety = corner(sy, y, i, j, k);

				if (ret * (i + i + k - 1) == retx * 2 &&
						ret * (j + j + k - 1) == rety * 2)
					ans = max(ans, k);
			}

	if (ans < 3) printf("IMPOSSIBLE\n");
	else printf("%d\n", ans);
}

void init() {
	int D; scanf("%d%d%d", &R, &C, &D);
	
	for (int i = 1; i <= R; i++) {
		char buf[501]; scanf("%s", buf);
		for (int j = 1; j <= C; j++)
			d[i][j] = buf[j - 1] - '0';
	}

	for (int i = 1; i <= R; i++)
		for (int j = 1; j <= C; j++) {
			s[i][j] = d[i][j];
			x[i][j] = d[i][j] * i;
			y[i][j] = d[i][j] * j;
		}

	acc(s, ss);
	acc(x, sx);
	acc(y, sy);
}

int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		init();
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
