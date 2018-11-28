#include <stdio.h>

int grid[100][100], N, H, W, R;

int main() {
	int i, j, k, y, x;
	FILE * fin = fopen("D.in", "r"), * fout = fopen("Ds.out", "w");
	fscanf(fin, "%d", &N);
	for (i = 1; i <= N; ++i) {
		fscanf(fin, "%d%d%d", &H, &W, &R);
		for (j = 0; j < H; ++j) {
			for (k = 0; k < W; ++k) {
				grid[j][k] = 0;
			}
		}
		for (j = 0; j < R; ++j) {
			fscanf(fin, "%d%d", &y, &x);
			grid[y - 1][x - 1] = -1;
		}
		grid[0][0] = 1;
		for (j = 0; j < H; ++j) {
			for (k = 0; k < W; ++k) {
				if (grid[j][k] > 0) {
					if (j + 1 < H && k + 2 < W && grid[j + 1][k + 2] != -1) {
						grid[j + 1][k + 2] += grid[j][k];
						grid[j + 1][k + 2] %= 10007;
					}
					if (j + 2 < H && k + 1 < W && grid[j + 2][k + 1] != -1) {
						grid[j + 2][k + 1] += grid[j][k];
					}
					grid[j + 2][k + 1] %= 10007;
				}
			}
		}
		fprintf(fout, "Case #%d: %d\n", i, grid[H - 1][W - 1]);
	}
	return 0;
}
