#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iostream>
using namespace std;

int tests, n, tcount;
int maxx, maxy, map[500][500], tmap[500][500];
inline int max(int a, int b) { return a > b ? a : b; }
int main(int argc, char *argv[]) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tests);
	for (int cases = 1; cases <= tests; ++ cases) {
		scanf("%d", &n);
		maxx = maxy = 0;
		memset(map, 0, sizeof(map));
		for (int p = 0; p < n; ++ p) {
			int x1, x2, y1, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			maxx = max(maxx, x1);
			maxy = max(maxy, y1);
			maxx = max(maxx, x2);
			maxy = max(maxy, y2);
			for (int i = x1; i <= x2; ++ i)
				for (int j = y1; j <= y2; ++ j)
					map[i][j] = true;
		}
		int ans = 0;
		do {
			tcount = 0;
			++ ans;
			for (int i = maxx + 1; i; -- i)
				for (int j = maxy + 1; j; -- j)
					if (map[i][j] == 0 && map[i][j - 1] == 1 && map[i - 1][j] == 1) {
						map[i][j] = 1;
						maxx = max(maxx, i); maxy = max(maxy, j);
					} else if (map[i][j] == 1) {
						if (map[i][j - 1] == 0 && map[i - 1][j] == 0) map[i][j] = 0;
					}
			for (int i = 0; i <= maxx; ++ i)
				for (int j = 0; j <= maxy; ++ j)
					if (map[i][j]) ++ tcount;
		} while (tcount != 0);
		printf("Case #%d: %d\n", cases, ans);
	}
	return 0;
}
