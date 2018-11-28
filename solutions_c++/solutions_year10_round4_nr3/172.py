#include <iostream>
using namespace std;

const int maxn = 101;

int tcase;
bool map[maxn][maxn];

void init() {
	int r, x1, x2, y1, y2;
	scanf("%d", &r);
	memset(map, 0, sizeof(map));
	while (r--) {
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int i = x1; i <= x2; ++i)
			for (int j = y1; j <= y2; ++j)
				map[i][j] = 1;
	}
}

int solve() {
	for (int res = 1; ; ++res) {
		int cnt = 0;
		for (int i = 100; i; --i)
			for (int j = 100; j; --j) {
				if (map[i-1][j] && map[i][j-1])
					map[i][j] = 1;
				else if (map[i][j] && !map[i-1][j] && !map[i][j-1])
					map[i][j] = 0;
				cnt += map[i][j];
			}
		if (cnt == 0) return res;
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcase);
	for (int c = 1; c <= tcase; ++c) {
		init();
		printf("Case #%d: %d\n", c, solve());
	}
	return 0;
}
