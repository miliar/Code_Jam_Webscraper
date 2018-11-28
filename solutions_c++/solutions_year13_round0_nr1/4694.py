#include <cstdio>
#include <algorithm>

enum {
	X_WON, O_WON, DRAW, NOT_COMPLETE
};

char state[5][5];

bool allrow(int row, char player) {
	for (int i = 0; i < 4; i++) {
		if (state[row][i] != player && state[row][i] != 'T') return false;
	}
	return true;
}

bool allcol(int col, char player) {
	for (int i = 0; i < 4; i++) {
		if (state[i][col] != player && state[i][col] != 'T') return false;
	}
	return true;
}

bool alldiag1(char player) {
	for (int i = 0; i < 4; i++) {
		if (state[i][i] != player && state[i][i] != 'T') return false;
	}
	return true;
}

bool alldiag2(char player) {
	for (int i = 0; i < 4; i++) {
		if (state[i][4 - i - 1] != player && state[i][4 - i - 1] != 'T') return false;
	}
	return true;
}

int solve() {
	int numsq = 0;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			state[i][j] = fgetc(stdin);
			if (state[i][j] == '.') numsq++;
		}
		fgetc(stdin);
	}
	fgetc(stdin); // line separator

	// check rows and columns
	for (int i = 0; i < 4; i++) {
		if (allrow(i, 'X') || allcol(i, 'X')) return X_WON;
		if (allrow(i, 'O') || allcol(i, 'O')) return O_WON;
	}

	// check diagonals
	if (alldiag1('X') || alldiag2('X')) return X_WON;
	if (alldiag1('O') || alldiag2('O')) return O_WON;

	if (numsq) return NOT_COMPLETE;
	return DRAW;
}

int main() {
	int t; scanf("%d\n", &t);
	for (int i = 1; i <= t; i++) {
		int result = solve();

		printf("Case #%d: ", i);
		if (result == X_WON) printf("X won\n");
		else if (result == O_WON) printf("O won\n");
		else if (result == DRAW) printf("Draw\n");
		else printf("Game has not completed\n");
	}
}