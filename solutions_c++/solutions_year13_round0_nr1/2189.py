#include <cstdio>

char board[4][4];
int T, dr[8] = {0, 1, 0, -1, 1, 1, -1, -1}, dc[8] = {1, 0, -1, 0, -1, 1, -1, 1};

bool oob(int r, int c) {
	return r < 0 || c < 0 || r >= 4 || c >= 4;
}

bool winningTile(int r, int c, char ch, int d, int count = 0) {
	if (count == 4) {
		return true;
	}
	if (oob(r, c)) {
		return false;
	}
	if (board[r][c] != ch && board[r][c] != 'T') {
		return false;
	}
	return winningTile(r+dr[d], c+dc[d], ch, d, count+1);
}

int main() {
	scanf("%d ", &T);
	for (int t = 1; t <= T; ++t) {
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				board[i][j] = getchar();
			}
			scanf(" ");
		}

		bool over = true;
		int winner = 0;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (board[i][j] == '.') {
					over = false;
				}
				for (int k = 0; k < 8; ++k) {
					if (winningTile(i, j, 'X', k)) {
						winner = 1;
					}
					if (winningTile(i, j, 'O', k)) {
						winner = 2;
					}
				}
			}
		}
		printf("Case #%d: ", t);
		if (winner) {
			printf("%s won", winner == 1 ? "X" : "O");
		} else if (over) {
			printf("Draw");
		} else {
			printf("Game has not completed");
		}
		printf("\n");
	}
}
