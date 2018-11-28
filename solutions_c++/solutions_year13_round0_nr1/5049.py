#include <cstdio>

int N;
char line[200];
char board[50][50];

bool isWon(char ch) {
	bool valid;
	for (int i=0; i<4; ++i) {
		valid = true;
		for (int j=0; j<4; ++j) 
			if ((board[i][j] != 'T') && (board[i][j] != ch)) valid = false;
		if (valid) return true;

		valid = true;
		for (int j=0; j<4; ++j)
			if ((board[j][i] != 'T') && (board[j][i] != ch)) valid = false;
		if (valid) return true;
	}

	valid = true;
	for (int i=0; i<4; ++i) if ((board[i][3-i] != 'T') && (board[i][3-i] != ch)) valid = false;
	if (valid) return true;

	valid = true;
	for (int i=0; i<4; ++i) if ((board[i][i] != 'T') && (board[i][i] != ch)) valid = false;
	return valid;
}

bool found(char ch) {
	for (int i=0; i<4; ++i)
		for (int j=0; j<4; ++j)
			if (board[i][j] == ch) return true;
	return false;
}

int main() {
	gets(line);
	sscanf(line, "%d", &N);
	for (int i=0; i<N; ++i) {
		for (int j=0; j<4; ++j) gets(board[j]);

		printf("Case #%d: ", i+1);
		if (isWon('X')) printf("X won\n");
		else
			if (isWon('O')) printf("O won\n");
			else
				if (found('.')) printf("Game has not completed\n");
				else
					printf("Draw\n");

		gets(line);
	}
	return 0;
}
