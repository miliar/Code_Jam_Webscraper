#include <stdio.h>
#include <string.h>

#define SIZE 104

int grid[SIZE][SIZE];

void print(int size) {
	for (int i = 1; i <= size; i++) {
		for (int j = 1; j <= size; j++) {
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}

int generate() {
	int alive = 0;
	for (int i = SIZE - 1; i > 0; i--) {
		for (int j = SIZE - 1; j > 0; j--) {
			if (grid[i][j]) {
				// keep alive when one neighbour is alive
				if (grid[i-1][j] || grid[i][j-1]) {
					alive++;
				} else {
					grid[i][j] = 0;
				}
			} else {
				// born if both neighbours alive
				if (grid[i-1][j] && grid[i][j-1]) {
					grid[i][j] = 1;
					alive++;
				}
			}
		}
	}
	for (int i = 0; i < SIZE; i++) {
		grid[0][i] = 0;
		grid[i][0] = 0;
	}
	return alive;
}

int calc() {
	int seconds = 0;
	do {
		seconds++;
		//print(6);
		//printf("Generation %d\n", seconds);
	} while (generate());
	//print(6);
	return seconds;
}

int main() {
	int cases;
	scanf("%d", &cases);
	
	for (int i = 1; i <= cases; i++) {
		memset(grid, 0, sizeof(grid));
		int coords;
		scanf("%d", &coords);
		while (coords--) {
			int xmin, xmax, ymin, ymax;
			scanf("%d %d %d %d", &xmin, &ymin, &xmax, &ymax);
			for (int x = xmin; x <= xmax; x++) {
				for (int y = ymin; y <= ymax; y++) {
					grid[y][x] = 1;
				}
			}
		}
		int seconds = calc();
		printf("Case #%d: %d\n", i, seconds);
	}
	return 0;
}
