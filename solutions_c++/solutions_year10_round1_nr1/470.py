#include <queue>
#include <cstdio>
#include <cstring>

const int MAX_N = 55;
int T, N, K;
char grid[MAX_N][MAX_N];

int line(int r, int c, int dr, int dc) {
	if (r <= 0 || r > N || c <= 0 || c > N) return 0;
	if (grid[r][c] != grid[r+dr][c+dc]) return 1;
	return 1 + line(r+dr, c+dc, dr, dc);
}

const char* won() {
	bool red = false, blue = false;
	for (int r = 1; r <= N; ++r) {
		for (int c = 1; c <= N; ++c) {
				if (grid[r][c] == '.') continue;
				if (line(r, c, 1, 0) >= K || line(r, c, 0, 1) >= K ||
						line(r, c, 1, 1) >= K || line(r, c, 1, -1) >= K) {
							(grid[r][c] == 'R' ? red : blue) = true;
				}
		}
	}
	if (!red && !blue) return "Neither";
	if (red && blue) return "Both";
	if (red) return "Red";
	if (blue) return "Blue";
}


int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d %d \n", &N, &K);
		memset(grid, 0, sizeof(char)*MAX_N*MAX_N);
		for (int r = 1; r <= N; ++r) {
			for (int c = 1; c <= N; ++c)
				grid[r][c] = getchar();
			int back = N;
			for (int c = N; c != 0; --c) {
				if (grid[r][c] == '.') continue;
				grid[r][back--] = grid[r][c];
				if (back+1 != c) grid[r][c] = '.';
			}
			scanf(" \n");
		}
		printf("Case #%d: %s\n", t, won());
	}
}
