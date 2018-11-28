#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int t;
	scanf("%d ", &t);

	for (int k = 0; k < t; k++)
	{
		char board[10][10] = {0};

		for (int i = 0; i < 4; i++)
			scanf("%s ", board[i]);

		int cou = 0;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (board[i][j] == '.')
					cou++;
			}
		}

		int dx[3] = {1,0,1};
		int dy[3] = {0,1,1};

		
		bool X = false;

		for (int i = 0; i < 4; i++)
		{
			bool f = true;
			for (int j = 0; j < 4; j++)
			{
				if (board[i][j] != 'X' && board[i][j] != 'T')
				{
					f = false;
					break;
				}
			}
			if (f)
			{
				X = true;
				break;
			}
		}

		for (int i = 0; i < 4; i++)
		{
			bool f = true;
			for (int j = 0; j < 4; j++)
			{
				if (board[j][i] != 'X' && board[j][i] != 'T')
				{
					f = false;
					break;
				}
			}
			if (f)
			{
				X = true;
				break;
			}
		}

		for (int i = 0; i < 1; i++)
		{
			bool f = true;
			for (int j = 0; j < 4; j++)
			{
				if (board[j][j] != 'X' && board[j][j] != 'T')
				{
					f = false;
					break;
				}
			}
			if (f)
			{
				X = true;
				break;
			}
		}

		for (int i = 0; i < 1; i++)
		{
			bool f = true;
			for (int j = 0; j < 4; j++)
			{
				if (board[4 - j - 1][j] != 'X' && board[4 - j - 1][j] != 'T')
				{
					f = false;
					break;
				}
			}
			if (f)
			{
				X = true;
				break;
			}
		}

		if (X)
		{
			printf("Case #%d: X won\n", k + 1);
			continue;
		}

		bool O = false;

		for (int i = 0; i < 4; i++)
		{
			bool f = true;
			for (int j = 0; j < 4; j++)
			{
				if (board[i][j] != 'O' && board[i][j] != 'T')
				{
					f = false;
					break;
				}
			}
			if (f)
			{
				O = true;
				break;
			}
		}

		for (int i = 0; i < 4; i++)
		{
			bool f = true;
			for (int j = 0; j < 4; j++)
			{
				if (board[j][i] != 'O' && board[j][i] != 'T')
				{
					f = false;
					break;
				}
			}
			if (f)
			{
				O = true;
				break;
			}
		}

		for (int i = 0; i < 1; i++)
		{
			bool f = true;
			for (int j = 0; j < 4; j++)
			{
				if (board[j][j] != 'O' && board[j][j] != 'T')
				{
					f = false;
					break;
				}
			}
			if (f)
			{
				O = true;
				break;
			}
		}

		for (int i = 0; i < 1; i++)
		{
			bool f = true;
			for (int j = 0; j < 4; j++)
			{
				if (board[4 - j - 1][j] != 'O' && board[4 - j - 1][j] != 'T')
				{
					f = false;
					break;
				}
			}
			if (f)
			{
				O = true;
				break;
			}
		}

		if (O)
		{
			printf("Case #%d: O won\n", k + 1);
			continue;
		}

		if (cou == 0)
		{
			printf("Case #%d: Draw\n", k + 1);
			continue;
		}

		printf("Case #%d: Game has not completed\n", k + 1);
		
	}
	return 0;
}