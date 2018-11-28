#include <cstdio>

char board[4][5];

bool findRun(char c) {
	for (int i = 0; i < 4; i++) {
		int found = 0;
		for (int j = 0; j < 4; j++) {
			if (board[i][j] == 'T' || board[i][j] == c) {
				found++;
			}
		}
		if (found == 4) {
			return true;
		}
		found = 0;
		for (int j = 0; j < 4; j++) {
			if (board[j][i] == 'T' || board[j][i] == c) {
				found++;
			}
		}
		if (found == 4) {
			return true;
		}
	}

	int found = 0;

	for (int i = 0; i < 4; i++) {
		if (board[i][i] == 'T' || board[i][i] == c) {
			found++;
		}
	}
	if (found == 4) {
		return true;
	}

	found = 0;

	for (int i = 0; i < 4; i++) {
		if (board[i][3 - i] == 'T' || board[i][3 - i] == c) {
			found++;
		}
	}

	if (found == 4) {
		return true;
	}
	
	return false;


}

void proc() {
	for (int i = 0; i < 4; i++) {
		scanf("%s ", board[i]);
	}
	if (findRun('X')) {
		printf("X won");
		return;
	}
	if (findRun('O')) {
		printf("O won");
		return;
	}
	int numFilled = 0;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (board[i][j] != '.') {
				numFilled++;
			}
		}
	}
	if (numFilled == 16) {
		printf("Draw");
	} else {
		printf("Game has not completed");
	}
}


int main() {
	int t;
	scanf("%d", &t);

	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		proc();
		printf("\n");
	}

	return 0;
}
