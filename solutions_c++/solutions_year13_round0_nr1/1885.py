#include <cstdio>
#include <cstring>

char board[4][4+1];

bool CheckIfWon(char ch)
{
	int i, j;

	// horizontal
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 4; j++)
		{
			if (board[i][j] != ch && board[i][j] != 'T')
			{
				break;
			}
		}
		if (j == 4)
		{
			return true;
		}
	}

	// verical
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 4; j++)
		{
			if (board[j][i] != ch && board[j][i] != 'T')
			{
				break;
			}
		}
		if (j == 4)
		{
			return true;
		}
	}

	// diagonal
	for (i = 0; i < 4; i++)
	{
		if (board[i][i] != ch && board[i][i] != 'T')
		{
			break;
		}
	}
	if (i == 4)
	{
		return true;
	}
	for (i = 3; i >= 0; i--)
	{
		if (board[3-i][i] != ch && board[3-i][i] != 'T')
		{
			break;
		}
	}
	if (i < 0)
	{
		return true;
	}

	return false;
}

int main()
{
	int test, t, i, j;
	bool has_empty;

	scanf("%d", &t);
	for (test = 1; test <= t; test++)
	{
		has_empty = false;

		for (i = 0; i < 4; i++)
		{
			scanf("%s", board[i]);

			if (strchr(board[i], '.') != NULL)
			{
				has_empty = true;
			}
		}

		if (CheckIfWon('O'))
		{
			printf("Case #%d: O won\n", test);
		}
		else if (CheckIfWon('X'))
		{
			printf("Case #%d: X won\n", test);
		}
		else if (has_empty)
		{
			printf("Case #%d: Game has not completed\n", test);
		}
		else
		{
			printf("Case #%d: Draw\n", test);
		}
	}

	return 0;
}
