#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

char xfield[4][4];
char ofield[4][4];

bool xwon(void)
{
	int i;
	
	//Zeilen
	for (i = 0; i < 4; i++)
	{
		if (xfield[i][0] == 'X' && xfield[i][1] == 'X' && xfield[i][2] == 'X' && xfield[i][3] == 'X')
		{
			return true;
		}
	}
	
	//Spalten
	for (i = 0; i < 4; i++)
	{
		if (xfield[0][i] == 'X' && xfield[1][i] == 'X' && xfield[2][i] == 'X' && xfield[3][i] == 'X')
		{
			return true;
		}
	}
	
	//Diagonalen
	if (xfield[0][0] == 'X' && xfield[1][1] == 'X' && xfield[2][2] == 'X' && xfield[3][3] == 'X')
	{
		return true;
	}
	if (xfield[3][0] == 'X' && xfield[2][1] == 'X' && xfield[1][2] == 'X' && xfield[0][3] == 'X')
	{
		return true;
	}
	
	return false;
}

bool owon(void)
{
	int i;
	
	//Zeilen
	for (i = 0; i < 4; i++)
	{
		if (ofield[i][0] == 'O' && ofield[i][1] == 'O' && ofield[i][2] == 'O' && ofield[i][3] == 'O')
		{
			return true;
		}
	}
	
	//Spalten
	for (i = 0; i < 4; i++)
	{
		if (ofield[0][i] == 'O' && ofield[1][i] == 'O' && ofield[2][i] == 'O' && ofield[3][i] == 'O')
		{
			return true;
		}
	}
	
	//Diagonalen
	if (ofield[0][0] == 'O' && ofield[1][1] == 'O' && ofield[2][2] == 'O' && ofield[3][3] == 'O')
	{
		return true;
	}
	if (ofield[3][0] == 'O' && ofield[2][1] == 'O' && ofield[1][2] == 'O' && ofield[0][3] == 'O')
	{
		return true;
	}
	
	return false;
}

bool unfinished(void)
{
	int i, j;
	
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 4; j++)
		{
			if (xfield[i][j] == '.')
			{
				return true;
			}
		}
	}
	return false;
}

int main()
{
	int t;
	int cases;
	int i, j;
	string line;
	
	//scanf("%d", &t);
	cin >> t;
	for (cases = 1; cases <= t; cases++)
	{
		//printf("Case #%d: ", cases);
		cout << "Case #" << cases << ": ";
		
		for (i = 0; i < 4; i++)
		{
			cin >> line;
			for (j = 0; j < 4; j++)
			{
				if (line[j] != 'T')
				{
					xfield[i][j] = line[j];
					ofield[i][j] = line[j];
				}
				else
				{
					xfield[i][j] = 'X';
					ofield[i][j] = 'O';
				}
			}
		}
		
		if (xwon())
		{
			//printf("X won");
			cout << "X won";
			
		}
		else if (owon())
		{
			//printf("O won");
			cout << "O won";
		}
		else if (unfinished())
		{
			//printf("Game has not completed");
			cout << "Game has not completed";
		}
		else
		{
			//printf("Draw");
			cout << "Draw";
		}		
		
		//printf("\n");
		cout << endl;
	}
	
	return 0;
}
