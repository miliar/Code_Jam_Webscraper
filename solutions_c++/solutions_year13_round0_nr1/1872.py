#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int SIZE = 4;
char board[SIZE][SIZE+1];
int tt;

bool has_won(char player) {
	bool full_main = true, full_sec = true;
	for (int i = 0; i < SIZE; i++) {
		if (board[i][i] != player && board[i][i] != 'T') {
			full_main = false;
		}
		if (board[i][SIZE-i-1] != player && board[i][SIZE-i-1] != 'T') {
			full_sec = false;
		}
	}
	if (full_main || full_sec) {
		return true;
	}
	for (int i = 0; i < SIZE; i++) {
		bool full_row = true, full_col = true;
		for (int j = 0; j < SIZE; j++) {
			if (board[i][j] != player && board[i][j] != 'T') {
				full_row = false;
			}
			if (board[j][i] != player && board[j][i] != 'T') {
				full_col = false;
			}
		}
		if (full_row || full_col) {
			return true;
		}
	}
	return false;
}

bool game_over() {
	for (int i = 0; i < SIZE; i++) {
		for (int j = 0; j < SIZE; j++) {
			if (board[i][j] == '.') {
				return false;
			}
		}
	}
	return true;
}

int main() {
	scanf("%d", &tt);
	for (int t = 1; t <= tt; t++) {
		for (int i = 0; i < SIZE; i++) {
			scanf ("%s", board[i]);
		}
		printf("Case #%d: ", t);
		if (has_won('X')) {
			printf("X won");
		} else if (has_won('O')) {
			printf("O won");
		} else if (game_over()) {
			printf("Draw");
		} else {
			printf("Game has not completed");
		}
		printf("\n");
	}

	return 0;
}