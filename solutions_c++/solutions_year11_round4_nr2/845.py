#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MAX = 550;
const double eps = 1e-8;
char s[MAX];
int dp[MAX][MAX];
int r, c, d;

int sgn(double x) {
	return x < -eps ? -1 : x > eps;
}

bool check(int sx, int sy, int ex, int ey) {
	double rx = 0, ry = 0;
	int ox = (sx + ex) / 2, oy = (sy + ey) / 2;
	int d = ex - sx + 1;

	if (d & 1) {
		for (int i = sx; i <= ex; i++) {
			for (int j = sy; j <= ey; j++) {
				if ((i == sx && (j == sy || j == ey)) || (i == ex && (j == sy
						|| j == ey)))
					continue;
				rx += (double) dp[i][j] * (i - ox);
				ry += (double) dp[i][j] * (j - oy);
			}
		}
	} else {
		for (int i = sx; i <= ex; i++) {
			for (int j = sy; j <= ey; j++) {
				if ((i == sx && (j == sy || j == ey)) || (i == ex && (j == sy
						|| j == ey)))
					continue;
				rx += (double) dp[i][j] * (i - ox - 0.5);
				ry += (double) dp[i][j] * (j - oy - 0.5);
			}
		}
	}

	return sgn(rx) == 0 && sgn(ry) == 0;
}

int run() {
	for (int k = min(r, c); k >= 3; k--) {
		for (int i = 0; i + k <= r; i++) {
			for (int j = 0; j + k <= c; j++) {
				if (check(i, j, i + k - 1, j + k - 1)) {
					return k;
				}
			}
		}
	}

	return -1;
}

int main() {
	int T, cas = 1;
	int ret;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);
	while (T--) {
		memset(dp, 0, sizeof(dp));
		printf("Case #%d: ", cas++);
		scanf("%d%d%d", &r, &c, &d);
		for (int i = 0; i < r; i++) {
			scanf("%s", s);
			for (int j = 0; j < c; j++) {
				dp[i][j] = s[j] - '0' + d;
			}
		}
		ret = run();
		if (ret != -1)
			printf("%d\n", ret);
		else
			puts("IMPOSSIBLE");
	}

	return 0;
}
