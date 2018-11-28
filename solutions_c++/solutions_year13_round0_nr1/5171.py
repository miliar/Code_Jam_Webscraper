#include <iostream>
#include <cstdio>
using namespace std;

int check_col(int c, char bd[4][6], char who) {
	int i;
	for (i = 0; i < 4; i++) {
		// printf("%c", bd[i][c]);
		if (bd[i][c] != who && bd[i][c] != 'T')
			return 0;
	}
	// printf("\n\n");
	return 1;
}

int check_row(int r, char bd[4][6], char who) {
	int i;
	for (i = 0; i < 4; i++) {
		// printf("%c", bd[r][i]);
		if (bd[r][i] != who && bd[r][i] != 'T')
			return 0;
	}
	// printf("\n\n");
	return 1;
}

int check_diag_left(char bd[4][6], char who) {
	int i;
	for (i = 0; i < 4; i++) {
		if (bd[i][i] != who && bd[i][i] != 'T')
			return 0;
	}
	return 1;
}

int check_diag_right(char bd[4][6], char who) {
	int i;
	for (i = 0; i < 4; i++) {
		if (bd[i][3-i] != who && bd[i][3-i] != 'T')
			return 0;
	}
	return 1;
}

int who_win(char bd[4][6], char who) {
	int i, j;

	for (i = 0; i < 4; i++) {
		if (check_col(i, bd, who))
			return 1;
		if (check_row(i, bd, who))
			return 1;
	}
	if (check_diag_left(bd, who))
		return 1;
	if (check_diag_right(bd, who))
		return 1;
	return 0;
}

int game_over(char bd[4][6]) {
	int i, j;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (bd[i][j] == '.')
				return 0;
		}
	}
	return 1;
}

int main() {
	int T;
	char board[4][6], ch;
	int i, j, k;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &T);
	for (i = 0; i < T; i++) {
		for (j = 0; j < 4; j++) {
			scanf("%s", &board[j]);
		}
		// for (j = 0; j < 4; j++) {
		// 	printf("%s", board[j]);
		// }
		printf("Case #%d: ", i+1);
		if (who_win(board, 'X')) {
			printf("X won\n");
			continue;
		}
		if (who_win(board, 'O')) {
			printf("O won\n");
			continue;
		}
		if (game_over(board)) {
			printf("Draw\n");
			continue;
		}
		printf("Game has not completed\n");
	}


	return 0;
}