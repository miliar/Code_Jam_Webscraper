#include <stdio.h>
char board[4][5];
enum State {
	XWIN,
	OWIN,
	DRAW,
	NOTCOMPLETE
};
bool checkHor(int row, char c)
{
	int c_count = 0, t_count = 0;
	for (int i = 0; i < 4; i++)
	{
		if (board[row][i] == c) c_count++;
		if (board[row][i] == 'T') t_count++;
	}
	return (c_count + t_count == 4) ? true : false;
}
bool checkVer(int col, char c)
{
	int c_count = 0, t_count = 0;
	for (int i = 0; i < 4; i++)
	{
		if (board[i][col] == c) c_count++;
		if (board[i][col] == 'T') t_count++;
	}
	return (c_count + t_count == 4) ? true : false;
}
bool checkDiag(char c)
{
	int c_count = 0, t_count = 0;
	for (int i = 0; i < 4; i++)
	{
		if (board[i][i] == c) c_count++;
		if (board[i][i] == 'T') t_count++;
	}
	return (c_count + t_count == 4) ? true : false;
}
bool checkAnoDiag(char c)
{
	int c_count = 0, t_count = 0;
	for (int i = 0; i < 4; i++)
	{
		if (board[i][3 - i] == c) c_count++;
		if (board[i][3 - i] == 'T') t_count++;
	}
	return (c_count + t_count == 4) ? true : false;
}
State Check()
{
	for (int i = 0; i < 4; i++)
	{
		if (checkHor(i, 'X')) return XWIN;
		if (checkHor(i, 'O')) return OWIN;
	}
	for (int i = 0; i < 4; i++)
	{
		if (checkVer(i, 'X')) return XWIN;
		if (checkVer(i, 'O')) return OWIN;
	}
	if (checkDiag('X')) return XWIN;
	if (checkDiag('O')) return OWIN;
	if (checkAnoDiag('X')) return XWIN;
	if (checkAnoDiag('O')) return OWIN;
	int left = 0;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (board[i][j] == '.') left++;
	return (left == 0) ? DRAW : NOTCOMPLETE;
}
int main()
{
	int t;
	scanf("%d", &t);
	for (int cases = 1; cases <= t; cases++)
	{
		for (int i = 0; i < 4; i++)
			scanf("%s", board[i]);
		printf("Case #%d: ", cases);
		State ret = Check();
		switch (ret)
		{
		case XWIN:
			printf("X won\n");
			break;
		case OWIN:
			printf("O won\n");
			break;
		case DRAW:
			printf("Draw\n");
			break;
		case NOTCOMPLETE:
		default:
			printf("Game has not completed\n");
			break;
		}
	}
}