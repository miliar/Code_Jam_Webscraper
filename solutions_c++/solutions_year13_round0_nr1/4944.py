#include <cstdio>

char board[4][4];

bool gagne(char c) {
	bool ok = false;
	for (int lin = 0; lin < 4; lin++) {
		bool g = true;
		for (int col = 0; col < 4; col++)
			if (!(board[lin][col] == c || board[lin][col] == 'T'))
				g = false;
		ok |= g;
	}
	for (int col = 0; col < 4; col++) {
		bool g = true;
		for (int lin = 0; lin < 4; lin++)
			if (!(board[lin][col] == c || board[lin][col] == 'T'))
				g = false;
		ok |= g;
	}
	bool diag = true;
	for (int i = 0; i < 4; i++)
	   if(!(board[i][i] == c || board[i][i] == 'T'))
			diag = false;	   
	ok |= diag;
	diag = true;
	for (int i = 0; i < 4; i++)
		if (!(board[i][3-i] == c || board[i][3-i] == 'T'))
		   diag = false;
	ok |= diag;	
	return ok;
}

int main(void) {
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		bool rempli = true;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) {
				scanf(" %c", &board[i][j]);
				if (board[i][j] == '.')
					rempli = false;
			}
		printf("Case #%d: ", test);
		if (gagne('X'))
			printf("X won\n");
		else if (gagne('O'))
			printf("O won\n");
		else if (rempli)
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
	return 0;
}
