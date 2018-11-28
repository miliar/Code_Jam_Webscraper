#include <cstdio>
#include <cstdlib>
#include <cstring>

int main()
{
	char* temp = NULL;
	size_t size = 0;
	size_t len = getline(&temp, &size, stdin);
	int cases = atoi(temp);

	int test;
	for (test = 0; test < cases; test++)
	{
		len = getline(&temp, &size, stdin);
		char* t = temp;
		int n = atoi(strsep(&t, " "));
		int k = atoi(t);

		char* board_raw = (char*)malloc(n*n*sizeof(char));
		char** board = (char**)malloc(n*sizeof(char*));
		int row = 0;
		for (row = 0; row < n; row++) board[row] = board_raw+row*n;
		for (row = 0; row < n*n; row++) board_raw[row] = '!';
		//printf("%i %i\n", n, k);

		int col = 0;
		for (row = 0; row < n; row++)
		{
			len = getline(&temp, &size, stdin);
			for (col = 0; col < n; col++)
			{
				board[col][n-row-1] = temp[col];
			}
		}

		for (col = 0; col < n; col++)
		{
			int drop = 0;
			for (row = n-1; row >= 0; row--)
			{
				if (board[row][col] == '.')
				{
					drop++;
				}
				else if (drop > 0)
				{
					board[row+drop][col] = board[row][col];
					board[row][col] = '.';
				}
			}
		}

		for (row = 0; row < n; row++)
		{
			for (col = 0; col < n; col++)
			{
				//printf("%c", board[row][col]);
			}
			//printf("\n");
		}

		int blue = 0, red = 0;
		for (row = 0; row < n; row++)
		{
			for (col = 0; col < n; col++)
			{
				if (board[row][col] == '.') continue;
				if (board[row][col] == 'R' && red) continue;
				if (board[row][col] == 'B' && blue) continue;
				char p = board[row][col];
				int temp;
				int h = 1, v = 1, d1 = 1, d2 = 1;
				for (temp = 0; temp < k; temp++)
				{
					if (col > n-k || board[row][col] != board[row][col+temp])
					{
						v = 0;
						break;
					}
				}
				for (temp = 0; temp < k; temp++)
				{
					if (row > n-k || board[row][col] != board[row+temp][col])
					{
						h = 0;
						break;
					}
				}
				for (temp = 0; temp < k; temp++)
				{
					if (row > n-k || board[row][col] != board[row+temp][col+temp])
					{
						d1 = 0;
						break;
					}
				}
				for (temp = 0; temp < k; temp++)
				{
					if (row > n-k || col-temp < 0 || board[row][col] != board[row+temp][col-temp])
					{
						d2 = 0;
						break;
					}
				}
				if (h || v || d1 || d2)
				{
					//printf("%i %i %c\n", row, col, board[row][col]);
					//printf("%i %i %i %i\n", h, v, d1, d2);
					if (board[row][col] == 'R') red = 1;
					else blue = 1;
					continue;
				}
			}
		}

		printf("Case #%i: %s\n", test+1, (red ? (blue ? "Both" : "Red"): (blue ? "Blue" : "Neither")));

	}
}
