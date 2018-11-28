#include <stdio.h>

char board[4][5];

bool same(char *str, char symbol)
{
	for(int i=0; i<4; i++) {
		if (str[i] != symbol && str[i] != 'T') 
			return false;
	}

	return true;
}

bool checkWin(char symbol)
{
	// row
	for(int i=0; i<4; i++) {
		if (same(board[i], symbol)) return true;
	}

	char tmp[4];

	// column
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			tmp[j] = board[j][i];
		}
		if (same(tmp, symbol)) return true;
	}

	// diagonal 
	for(int i=0, j=0; i<4; i++,j++) {
		tmp[i] = board[i][j];
	}
	if (same(tmp, symbol)) return true;

	for(int i=0, j=3; i<4; i++, j--) {
		tmp[i] = board[i][j];
	}
	if (same(tmp, symbol)) return true;

	return false;
}

bool checkDraw()
{
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			if (board[i][j] == '.') return false;
		}
	}
	return true;
}

int main()
{
	int t;

	scanf("%d", &t);

	for(int k=1; k<=t; k++)
	{
		for(int i=0; i<4; i++) {
			scanf("%s", board[i]);
		}

		if (checkWin('X')) {
			printf("Case #%d: X won\n", k);	
		} else if (checkWin('O')) {
			printf("Case #%d: O won\n", k);	
		} else if (checkDraw()) {
			printf("Case #%d: Draw\n", k);	
		} else {
			printf("Case #%d: Game has not completed\n", k);	
		}
	}

	return 0;
}

