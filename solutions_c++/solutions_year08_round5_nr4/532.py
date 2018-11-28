#include <cstdio>
#include <cstring>

const int P = 10007;
bool map[128][128];
int memo[128][128];

int main() {
	int t, w, h, r;
	scanf("%d", &t);
	for (int kase = 0; kase < t; ++kase) {
		int x, y;
		scanf("%d%d%d", &h, &w, &r);
		memset(memo, 0, sizeof(memo));
		memset(map, 0, sizeof(map));
		memo[1][1] = 1;
		for (int i = 0; i < r; ++i) {
			scanf("%d%d", &x, &y);
			map[x][y] = true;
		}
		for (int i = 1; i <= h; ++i) {
			for (int j = 1; j <= w; ++j) {
				x = i - 1, y = j - 2;
				if (x > 0 && y > 0 && !map[i][j]) {
					memo[i][j] += memo[x][y];
				}
				x = i - 2; y = j - 1;
				if (x > 0 && y > 0 && !map[i][j]) {
					memo[i][j] += memo[x][y];
				}
				memo[i][j] %= 10007;
			}
		}
		printf("Case #%d: %d\n", kase + 1, memo[h][w]);
	}
	return 0;
}
