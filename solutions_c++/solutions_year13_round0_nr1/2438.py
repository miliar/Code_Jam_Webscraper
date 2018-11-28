#include <stdio.h>

#define O_WON 0
#define X_WON 1
#define DRAW 2
#define NOT_COMPLETED 3

int T;
char board[5][5];
bool has_empty_block;

char what_col(int c)
{
	int r;

	// check first row
	if (c == 0) {
		if (board[0][0] != 'T') {
			for (r = 1; r < 4; r++)
				if (board[0][r] != 'T' && board[0][r] != board[0][0]) break;
			if (r == 4) return board[0][0];
		}
		else {
			for (r = 2; r < 4; r++) 
				if (board[0][r] != board[0][1]) break;
			if (r == 4) return board[0][1];
		}
	}

	// check specific col
	if (board[0][c] != 'T') {
		for (r = 1; r < 4; r++) 
			if (board[r][c] != 'T' && board[r][c] != board[0][c]) break;
		if (r == 4) return board[0][c];
	}
	else {
		for (r = 2; r < 4; r++) 
			if (board[r][c] != board[1][c]) break;
		if (r == 4) return board[1][c];
	}

	return 0;
}

char what_row(int r)
{
	int c;

	// check diag
	if (r == 0) {
		if (board[c][c] != 'T') {
			for (c = 1; c < 4; c++)
				if (board[c][c] != board[r][r] && board[c][c] != 'T') break;
			if (c == 4) return board[r][r];
		}
		else {
			for (c = 2; c < 4; c++)
				if (board[c][c] != board[1][1]) break;
			if (c == 4) return board[1][1];
		}
	}
	else if (r == 3) {
		if (board[3][0] != 'T') {
			for (c = 2; c >= 0; c--) 
				if (board[c][3-c] != board[3][0] && board[c][3-c] != 'T') break;
			if (c < 0) return board[3][0];
		}
		else {
			for (c = 1; c >= 0; c--)
				if (board[c][3-c] != board[2][1]) break;
			if (c < 0) return board[2][1];
		}
	}

	// check first column
	if (r == 0) {
		if (board[0][0] != 'T') {
			for (c = 1; c < 4; c++) 
				if (board[c][0] != board[0][0] && board[c][0] != 'T') break;
			if (c == 4) return board[0][0];
		}
		else {
			for (c = 2; c < 4; c++)
				if (board[c][0] != board[1][0]) break;
			if (c == 4) return board[1][0];
		}
	}

	// check specific row
	if (board[r][0] != 'T') {
		for (c = 1; c < 4; c++) 
			if (board[r][c] != board[r][0] && board[r][c] != 'T') break;
		if (c == 4) return board[r][0];
	}
	else {
		for (c = 2; c < 4; c++) 
			if (board[r][c] != board[r][1]) break;
		if (c == 4) return board[r][1];
	}

	return 0;
}

int brute_force_detect()
{
	char fg;
	int r, c;

	// check row
	for (r = 0; r < 4; r++) {
		fg = what_row(r);
		if (fg == 'O') return O_WON;
		else if (fg == 'X') return X_WON;
	}

	// check col
	for (c = 0; c < 4; c++) {
		fg = what_col(c);
		if (fg == 'O') return O_WON;
		else if (fg == 'X') return X_WON;
	}

	if (has_empty_block) return NOT_COMPLETED;
	
	return DRAW;
}

int main()
{
	int r, t;
	int i, j;
	char msg[30];

	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		has_empty_block = false;
		for (i = 0; i < 4; i++) {
			scanf("%s", board[i]);
			for (j = 0; !has_empty_block && j < 4; j++) 
				if (board[i][j] == '.') has_empty_block = true;
		}
		r = brute_force_detect();
		if (r == X_WON) sprintf(msg, "X won");
		else if (r == O_WON) sprintf(msg, "O won");
		else if (r == DRAW) sprintf(msg, "Draw");
		else sprintf(msg, "Game has not completed");
		printf("Case #%d: %s\n", t, msg);
	}
	return 0;
}

