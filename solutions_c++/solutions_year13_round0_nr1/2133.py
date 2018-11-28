#include <cstdio>
const int S = 4;
char board[S][S + 1];
bool filled()
{
	for (int i = 0; i < S; i++)
		for (int j = 0; j < S; j++)
			if (board[i][j] == '.')
				return false;
	return true;
}
int winner()
{
	char w = 0;
	for (int i = 0; i < S; i++)
	{
		for (int j = 0; j < S; j++)
			if (board[i][j] != 'T')
				w |= board[i][j];
			else
				board[i][j] = 0;
		if (w == 'X')
			return 1;
		if (w == 'O')
			return -1;
		w = 0;
	}
	for (int j = 0; j < S; j++)
	{
		for (int i = 0; i < S; i++)
			w |= board[i][j];
		if (w == 'X')
			return 1;
		if (w == 'O')
			return -1;
		w = 0;
	}
	for (int i = 0, j = 0; i < S; i++, j++)
		w |= board[i][j];
	if (w == 'X')
		return 1;
	if (w == 'O')
		return -1;
	w = 0;
	for (int i = 0, j = S - 1; i < S; i++, j--)
		w |= board[i][j];
	
	if (w == 'X')
		return 1;
	if (w == 'O')
		return -1;
	return 0;
}
int main()
{
	int t, win;
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		for (int j = 0; j < S; j++)
			scanf("%s", board[j]);
		printf("Case #%d: ", i);
		win = winner();
		if (!win)
		{
			if (filled())
				printf("Draw\n");
			else
				printf("Game has not completed\n");
		}
		else if (win > 0)
			printf("X won\n");
		else
			printf("O won\n");
	}
	return 0;
}