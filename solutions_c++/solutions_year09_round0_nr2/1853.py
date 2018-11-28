#include <stdio.h>

#define INF 10001;

const char VAZIO = '_';
int matrix[102][102];
char map[102][102];
char basis;
int h, w;

char sink(int i, int j) {
	if (map[i][j] != VAZIO)
		return map[i][j];
	int k = 0, l = 0;
	if (matrix[i - 1][j] < matrix[i + k][j + l])
		k = -1, l = 0;
	if (matrix[i][j - 1] < matrix[i + k][j + l])
		k = 0, l = -1;
	if (matrix[i][j + 1] < matrix[i + k][j + l])
		k = 0, l = 1;
	if (matrix[i + 1][j] < matrix[i + k][j + l])
		k = 1, l = 0;
	if (k == 0 && l == 0)
		return map[i][j] = ++basis;
	return map[i][j] = sink(i + k, j + l);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int count = 1; count <= t; count++) {
		scanf("%d%d", &h, &w);
		for (int i = 0; i <= h + 1; i++)
			matrix[i][0] = matrix[i][w + 1] = INF;
		for (int i = 0; i <= w + 1; i++)
			matrix[0][i] = matrix[h + 1][i] = INF;
		for (int i = 1; i <= h; i++)
			for (int j = 1; j <= w; j++)
				scanf("%d", &matrix[i][j]);
		for (int i = 0; i <= h + 1; i++)
			for (int j = 0; j <= w + 1; j++)
				map[i][j] = VAZIO;
		basis = 'a' - 1;
		for (int i = 1; i <= h; i++)
			for (int j = 1; j <= w; j++)
				sink(i, j);
		printf("Case #%d:\n", count);
		for (int i = 1; i <= h; i++) {
			for (int j = 1; j <= w; j++)
				printf("%c ", map[i][j]);
			printf("\n");
		}
	}
}
