#include <stdio.h>

int T;
char board[8][8];

bool check(char c)
{
	for (int i = 0; i < 4; ++i) {
		bool same = true;
		for (int j = 0; j < 4; ++j) if (board[i][j] != 'T' && board[i][j] != c) same = false;
		if (same) return true;
	}
	for (int j = 0; j < 4; ++j) {
		bool same = true;
		for (int i = 0; i < 4; ++i) if (board[i][j] != 'T' && board[i][j] != c) same = false;
		if (same) return true;
	}
	bool same = true;
	for (int i = 0; i < 4; ++i) if (board[i][i] != 'T' && board[i][i] != c) same = false;
	if (same) return true;
	same = true;
	for (int i = 0; i < 4; ++i) if (board[i][3 - i] != 'T' && board[i][3 - i] != c) same = false;
	return same;
}

void work()
{
	static int ttt = 0;
	printf("Case #%d: ", ++ttt);
	for (int i = 0; i < 4; ++i) gets(board[i]);
	gets(board[4]);
	if (check('X')) {
		printf("X won\n");
	} else if (check('O')) {
		printf("O won\n");
	} else {
		bool complete = true;
		for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j) if (board[i][j] == '.') complete = false;
		if (!complete) {
			printf("Game has not completed\n");
		} else {
			printf("Draw\n");
		}
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d\n", &T);
	while (T--) work();
}