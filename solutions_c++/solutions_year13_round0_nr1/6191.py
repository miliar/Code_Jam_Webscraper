#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;

char tictacbrd[4][4];
bool full;

bool tictaccomp (char c, int x, int y)
{
	int check = 0;
	for(int col = 0 ; col < 4 ; col++)
	{
		if(tictacbrd[x][col] == 'T' || tictacbrd[x][col] == c) check++;
	}

	if(check == 4) return true;

	check = 0;
	for(int row = 0 ; row < 4 ; row++)
	{
		if(tictacbrd[row][y] == 'T' || tictacbrd[row][y] == c) check++;
	}

	if(check == 4) return true;

	check = 0;

	if(x+y == 3)
	{
		for(int i = 0 ; i < 4 ; i++)
		{
			for(int j = 0 ; j < 4 ; j++)
			{
				if(i+j == 3)
				{
					if(tictacbrd[i][j] == 'T' || tictacbrd[i][j] == c) check++;
				}
			}
		}
		if(check == 4) return true;
		check = 0;
	}

	if(x == y)
	{
		for(int i = 0 ; i < 4 ; i++)
		{
			for(int j = 0 ; j < 4 ; j++)
			{
				if(!(i-j))
				{
					if(tictacbrd[i][j] == 'T' || tictacbrd[i][j] == c) check++;
				}
			}
		}
		if(check == 4) return true;
		check = 0;
	}
	return false;
}

int main()
{
	int test, count = 1;
	scanf("%d", &test);
	while(test--)
	{
		memset(tictacbrd, 0, sizeof(tictacbrd));

		for(int i = 0 ; i < 4 ; i++)
		{
			scanf("%s", tictacbrd[i]);
		}

		string winner = "Draw";
		full = true;
		
		for(int i = 0 ; i < 4 ; i++)
		{
			for(int j = 0 ; j < 4 ; j++)
			{
				if(tictacbrd[i][j] == '.') full = false;
				else if(tictacbrd[i][j] == 'X' || tictacbrd[i][j] == 'O')
				{
					bool iswin = tictaccomp(tictacbrd[i][j], i, j);
					if(iswin)
					{
						winner = "";
						winner += tictacbrd[i][j];
						break;
					}
				}
			}
		}

		printf("Case #%d: ", count++);

		if(winner == "X" || winner == "O") printf("%s won\n", winner.c_str()); 
		else if(winner == "Draw")
		{
			if(full) puts("Draw");
			else puts("Game has not completed");
		}
	}
	return 0;
}