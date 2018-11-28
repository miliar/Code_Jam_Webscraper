#include <cstdio>

const int N = 4;

char checkBoard(char board[N][N], int i0, int di, int j0, int dj) {
	int x = 0, o = 0, t = 0;
	for (int i = i0, j = j0; i >= 0 && i < N && j >= 0 && j < N; i += di, j += dj) {
		switch (board[i][j]) {
                case 'X':
                        x++;
                        break;
                case 'O':
                       	o++;
                       	break;
               	case 'T':
                       	t++;
                       	break;
       		}
	}

	if (x == 4 || (x == 3 && t == 1)) {
		return 'X';
	}
	if (o == 4 || (o == 3 && t == 1)) {
		return 'O';
	}

	return ' ';
}

bool isFull(char board[N][N]) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (board[i][j] == '.') {
				return false;
			}
		}
	}

	return true;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int ti = 1; ti <= t; ti++) {
		char board[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				scanf(" %c", &board[i][j]);
			}
		}

		char result = isFull(board) ? 'D' : ' ';

		// Check rows
		for (int i = 0; i < N; i++) {
			char tmp = checkBoard(board, i, 0, 0, 1);
			if (tmp != ' ') {
				result = tmp;
			}
		}

		// Check columns
		for (int i = 0; i < N; i++) {
			char tmp = checkBoard(board, 0, 1, i, 0);
			if (tmp != ' ') {
				result = tmp;
			}
		}

		// Check diagonals
		char tmp = checkBoard(board, 0, 1, 0, 1);
		if (tmp != ' ') {
			result = tmp;
		}
		tmp = checkBoard(board, 0, 1, N - 1, -1);
		if (tmp != ' ') {
			result = tmp;
		}

		printf("Case #%d: ", ti);
		switch (result) {
			case 'X':
			case 'O':
				printf("%c won", result);
				break;
			case 'D':
				printf("Draw");
				break;
			default:
				printf("Game has not completed");
				break;
		}
		printf("\n");
	}
	return 0;
}

