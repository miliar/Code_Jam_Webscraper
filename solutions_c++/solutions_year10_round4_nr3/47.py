#include <cstdio>
#include <algorithm>
#define MAX_N 110

int n, tests, t[2][MAX_N][MAX_N];

int main() {
	scanf("%d", &tests);
	for (int tc = 1; tc <= tests; tc++) {
		scanf("%d", &n);
		memset(t, 0, sizeof(t));
		for (int i = 0; i < n; i++) {
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for (int x = x1; x <= x2; x++)
				for (int y = y1; y <= y2; y++)
					t[0][x][y] = 1;
		}
		int total = 0, a = 0;
		while (true) {
			bool empty = true;
			for (int i = 0; i < MAX_N; i++)
				for (int j = 0; j < MAX_N; j++)
					if (t[a][i][j]) {
						empty = false;
						if (t[a][i - 1][j] || t[a][i][j - 1])
							t[1 - a][i][j] = 1;
					} else {
						if (t[a][i - 1][j] && t[a][i][j - 1])
							t[1 - a][i][j] = 1;
					}
			if (empty)
				break;
			total++;
			memset(t[a], 0, sizeof(t[a]));
			a = 1 - a;
		}
		printf("Case #%d: %d\n", tc, total);
	}
	return 0;
}