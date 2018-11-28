#include <cstdio>
#include <cstring>

const int MAX_GRID = 105;
int T, R;
bool grid[MAX_GRID][MAX_GRID];

bool clear() {
	for (int i = 0; i < MAX_GRID; ++i)
		for (int j = 0; j < MAX_GRID; ++j)
			if (grid[i][j]) return false;
	return true;
}

int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		memset(grid, 0, sizeof(bool)*MAX_GRID*MAX_GRID);
		scanf("%d", &R);
		for (int r = 0; r < R; ++r) {
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for (int x = x1; x <= x2; ++x)
				for (int y = y1; y <= y2; ++y)
					grid[x][y] = true;
		}

		int s = 0;
		while (!clear()) {
			bool next[MAX_GRID][MAX_GRID] = {};
			for (int x = 0; x < MAX_GRID; ++x) {
				for (int y = 0; y < MAX_GRID; ++y) {
					next[x][y] = grid[x][y];
					if ((x > 0 && grid[x-1][y]) && (y > 0 && grid[x][y-1]))
						next[x][y] = true;
					if ((x <= 0 || grid[x-1][y] == false) && (y <= 0 || grid[x][y-1] == false))
						next[x][y] = false;
				}
			}
			memcpy(grid, next, sizeof(bool)*MAX_GRID*MAX_GRID);
			++s;
		}
		printf("Case #%d: %d\n", t, s);
	}
}
