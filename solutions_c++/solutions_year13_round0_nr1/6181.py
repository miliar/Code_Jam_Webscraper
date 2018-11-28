#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	  // Process queries.
	int T;
	char buffLine[5];

	char board[4][5];
	
	scanf("%d", &T);
	for (int prob = 1; prob <= T; prob++)
	{
		for (int ii = 0; ii < 4; ii++)
		{
			scanf("%s", board[ii]);
			board[ii][4] = 0;
		}
		
		bool xwin = false;
		bool owin = false;
		// check lines;
		int countDot = 0;
		for (int ii = 0; ii < 4; ii++)
		{
			int countX = 0;
			int countO = 0;
			int countT = 0;
			for (int jj = 0; jj < 4; jj++)
			{
				if (board[ii][jj] == 'X')
				{
					countX++;
				}
				else if (board[ii][jj] == 'O')
				{
					countO++;
				}
				else if (board[ii][jj] == 'T')
				{
					countT++;
				}
				else
				{
					countDot++;
				}
			}

			if (countX + countT == 4)
			{
				xwin = true;
			}
			else if (countO + countT == 4)
			{
				owin = true;
			}

			if (xwin || owin) 
				break;
		}

		if (xwin) 
		{
			printf("Case #%d: %s\n", prob, "X won");
			continue;
		}

		if (owin) 
		{
			printf("Case #%d: %s\n", prob, "O won");
			continue;
		}


		// columns
		for (int ii = 0; ii < 4; ii++)
		{
			int countX = 0;
			int countO = 0;
			int countT = 0;
			for (int jj = 0; jj < 4; jj++)
			{
				if (board[jj][ii] == 'X')
				{
					countX++;
				}
				else if (board[jj][ii] == 'O')
				{
					countO++;
				}
				else if (board[jj][ii] == 'T')
				{
					countT++;
				}
				
			}

			if (countX + countT == 4)
			{
				xwin = true;
			}
			else if (countO + countT == 4)
			{
				owin = true;
			}

			if (xwin || owin) 
				break;

		}

		if (xwin) 
		{
			printf("Case #%d: %s\n", prob, "X won");
			continue;
		}

		if (owin) 
		{
			printf("Case #%d: %s\n", prob, "O won");
			continue;
		}

		
		// diagonals;
		int countX = 0;
		int countO = 0;
		int countT = 0;
		for (int jj = 0; jj < 4; jj++)
		{
			if (board[jj][jj] == 'X')
			{
				countX++;
			}
			else if (board[jj][jj] == 'O')
			{
				countO++;
			}
			else if (board[jj][jj] == 'T')
			{
				countT++;
			}
		}

		if (countX + countT == 4)
		{
			printf("Case #%d: %s\n", prob, "X won");
			continue;
		}
		
		if (countO + countT == 4)
		{
			printf("Case #%d: %s\n", prob, "O won");
			continue;
		}

		countX = 0;
		countO = 0;
		countT = 0;
		for (int jj = 0; jj < 4; jj++)
		{
			if (board[jj][3 - jj] == 'X')
			{
				countX++;
			}
			else if (board[jj][3 - jj] == 'O')
			{
				countO++;
			}
			else if (board[jj][3 - jj] == 'T')
			{
				countT++;
			}
		}

		if (countX + countT == 4)
		{
			printf("Case #%d: %s\n", prob, "X won");
			continue;
		}
		
		if (countO + countT == 4)
		{
			printf("Case #%d: %s\n", prob, "O won");
			continue;
		}

		if (countDot > 0)
		{
			printf("Case #%d: %s\n", prob, "Game has not completed");
		}
		else
		{
			printf("Case #%d: %s\n", prob, "Draw");
		}

	}



	return 0;
}