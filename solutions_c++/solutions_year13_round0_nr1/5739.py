#include <cstdio>
#include <cstring>
#include <cstdlib>

char matriz[5][5];
int lines[5];
int columns[5];
int mainDiagonal, complDiagonal;
int tI, tJ;
int isIncomplete;

void read() {
	for (int i = 0; i < 4; i++) {
		scanf("%s", matriz[i]);
	}
	for (int i = 0; i < 4; i++) {
		lines[i] = 0;
		columns[i] = 0;
	}
	mainDiagonal = 0;
	complDiagonal = 0;
	isIncomplete = 0;
	tI = -1;
	tJ = -1;
}

void process() {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			int summed;
			if (matriz[i][j] == 'X') {
				summed = 1;
			} else if (matriz[i][j] == 'O') {
				summed = -1;
			} else {
				summed = 0;
				if (matriz[i][j] == 'T') {
					tI = i;
					tJ = j;
				} else {
					isIncomplete = 1;
				}
			}
			lines[i] += summed;
			columns[j] += summed;
			if (i == j) {
				mainDiagonal += summed;
			} else if (i + j == 3) {
				complDiagonal += summed;
			}
		}
	}
	int winner = 0;
	for (int i = 0; i < 4; i++) {
		if (lines[i] == 4 or columns[i] == 4) {
			winner = 1;
		} else if (lines[i] == -4 or columns[i] == -4) {
			winner = -1;
		} else if ((lines[i] == 3 and tI == i) or (columns[i] == 3 and tJ == i)) {
			winner  = 1;
		} else if ((lines[i] == -3 and tI == i) or (columns[i] == -3 and tJ == i)) {
			winner = -1;
		}
	}
	if (mainDiagonal == 4 or complDiagonal == 4) {
		winner = 1;
	} else if (mainDiagonal == -4 or complDiagonal == -4) {
		winner = -1;
	}
	if ((mainDiagonal == 3 and tI > 0 and tI == tJ) or (complDiagonal == 3 and tI + tJ == 3)) {
		winner = 1;
	} else if ((mainDiagonal == -3 and tI > 0 and tI == tJ) or (complDiagonal == -3 and tI + tJ == 3)) {
		winner = -1;
	}

	if (winner) {
		printf("%s won\n", (winner > 0 ? "X" : "O"));
	} else {
		if (isIncomplete) {
			printf("Game has not completed\n");
		} else {
			printf("Draw\n");
		}
	}
}

int main() {
	int cases;
	scanf("%d", &cases);
	for (int i = 1; i <= cases; i++) {
		read();
		printf("Case #%d: ", i);
		process();
	}
	return 0;
}