#include <cstdio>

char game[4][5];

char check() {
	int i, j;
	for (i = 0; i < 4; i++) {
		for (j = 1; j < 4 && game[i][j] != '.' && game[i][j] == game[i][j - 1]; j++);
		if (j == 4) return game[i][0];
		for (j = 1; j < 4 && game[j][i] != '.' && game[j][i] == game[j - 1][i]; j++);
		if (j == 4) return game[0][i];
	}
	for (i = 1; i < 4 && game[i][i] != '.' && game[i][i] == game[i - 1][i - 1]; i++);
	if (i == 4) return game[0][0];
	for (i = 1; i < 4 && game[i][3 - i] != '.' && game[i][3 - i] == game[i - 1][4 - i]; i++);
	if (i == 4) return game[0][3];
	return 0;
}

int main() {
	int ti, tj, n, N;
	bool draw;
	scanf("%d", &N);
	for (n = 1; n <= N; n++) {
		ti = tj = -1;
		gets(game[0]);
		printf("Case #%d: ", n);
		draw = true;
		for (int i = 0; i < 4; i++) {
			gets(game[i]);
			for (int j = 0; j < 4; j++) {
				if (game[i][j] == 'T') {
					ti = i;
					tj = j;
				}
				if (game[i][j] == '.') {
					draw = false;
				}
			}
		}
		if ((ti + 1)) {
			game[ti][tj] = 'X';
		}
		char w = check();
		if (w) {
			printf("%c won\n", w);
			continue;
		}
		if ((ti + 1)) {
			game[ti][tj] = 'O';
			w = check();
			if (w) {
				printf("%c won\n", w);
				continue;
			}
		}
		if (draw) {
			puts("Draw");
		} else {
			puts("Game has not completed");
		}
	}
	return 0;
}
