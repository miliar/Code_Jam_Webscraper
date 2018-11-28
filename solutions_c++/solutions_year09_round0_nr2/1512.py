#include <stdio.h>
#include <string.h>

int altitudes[110][110];
char labels[110][110];

char next_label;
int H, W;

int D[][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };

char floodfill(int x) {
	int i = x/W;
	int j = x%W;

	if (labels[i][j] != '\0') return labels[i][j];

	int best_alt = altitudes[i][j];
	int best_d = -1;
	for (int d=0; d < 4; d++) {
		int ii = i + D[d][0];
		int jj = j + D[d][1];
		if (ii < 0 || ii >= H || jj < 0 || jj >= W) continue;

		if (altitudes[ii][jj] < best_alt) {
			best_alt = altitudes[ii][jj];
			best_d = d;
		}
	}

	if (best_d == -1) {
		return labels[i][j] = next_label++;
	}
	else {
		int xx = ((i + D[best_d][0]) * W) + (j + D[best_d][1]);
		return labels[i][j] = floodfill(xx);
	}
}

int main() {
	int T, _42;
	scanf(" %d", &T);
	for (int _42=1; _42 <= T; _42++) {
		memset(labels, 0, sizeof(labels));
		scanf(" %d %d", &H, &W);

		for (int i=0; i < H; i++) {
			for (int j=0; j < W; j++) {
				scanf(" %d", &altitudes[i][j]);
			}
		}

		next_label = 'a';
		for (int i=0; i < H*W; i++) floodfill(i);

		printf("Case #%d:\n", _42);
		for (int i=0; i < H; i++) {
			for (int j=0; j < W; j++) {
				if (j) printf(" ");
				printf("%c", labels[i][j]);
			}
			printf("\n");
		}
	}

	return 0;
}
