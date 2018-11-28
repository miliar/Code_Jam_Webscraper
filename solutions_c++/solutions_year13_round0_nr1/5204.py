#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	int t = 0;
	while (t < T)
	{
		t++;
		char board[5][5];
		for (int i = 0; i < 4; i ++)
		{
			scanf("%s", board[i]);
		}
		fgets(board[4], 3, stdin);

		int flag = 0;
		char winner = 0;
		for (int i = 0; i < 4; i ++)
		{
			flag = 0;
			winner = 0;
			for (int j = 0; j < 4; j ++)
			{
				if (board[i][j] == '.')
				{
					flag = 1;
					break;
				}

				if (winner == 0)
				{
					winner = board[i][j];
				}
				else if (winner == 'T')
				{
					winner = board[i][j];
				}
				else
				{
					if (winner != board[i][j] && board[i][j] != 'T')
					{
						flag = 1;
						break;
					}
				}
			}
			if (!flag)
			{
				break;
			}
		}

		if (!flag)
		{
			printf("Case #%d: %c won\n", t, winner);
			continue;
		}
		for (int j = 0; j < 4; j ++)
		{
			flag = 0;
			winner = 0;
			for (int i = 0; i < 4; i ++)
			{
				if (board[i][j] == '.')
				{
					flag = 1;
					break;
				}

				if (winner == 0)
				{
					winner = board[i][j];
				}
				else if (winner == 'T')
				{
					winner = board[i][j];
				}
				else
				{
					if (winner != board[i][j] && board[i][j] != 'T')
					{
						flag = 1;
						break;
					}
				}
			}
			if (!flag)
			{
				break;
			}
		}

		if (!flag)
		{
			printf("Case #%d: %c won\n", t, winner);
			continue;
		}

		flag = 0;
		winner = 0;
		for (int i = 0; i < 4; i ++)
		{
			if (board[i][i] == '.')
			{
				flag = 1;
				break;
			}
			if (winner == 0)
			{
				winner = board[i][i];
			}
			else if (winner == 'T')
			{
				winner = board[i][i];
			}
			else
			{
				if (winner != board[i][i] && board[i][i] != 'T')
				{
					flag = 1;
					break;
				}
			}
		}

		if (!flag)
		{
			printf("Case #%d: %c won\n", t, winner);
			continue;
		}

		flag = 0;
		winner = 0;
		for (int i = 0; i < 4; i ++)
		{
			if (board[i][3 - i] == '.')
			{
				flag = 1;
				break;
			}
			if (winner == 0)
			{
				winner = board[i][3 - i];
			}
			else if (winner == 'T')
			{
				winner = board[i][3 - i];
			}
			else
			{
				if (winner != board[i][3 - i] && board[i][3 - i] != 'T')
				{
					flag = 1;
					break;
				}
			}
		}

		if (!flag)
		{
			printf("Case #%d: %c won\n", t, winner);
			continue;
		}

		flag = 0;
		for (int i = 0; i < 4; i ++)
		for (int j = 0; j < 4; j ++)
		{
			if (board[i][j] == '.')
			{
				flag = 1;
				break;
			}
		}

		if (flag)
		{
			printf("Case #%d: Game has not completed\n", t);
		}
		else
		{
			printf("Case #%d: Draw\n", t);
		}

	}
}
