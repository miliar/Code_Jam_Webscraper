/*
 * tictactoe.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: stephenfebrian
 */

#include <cstdio>
#include <cstring>
#include <string>

char maze[4][4];
int sumO;
int sumX;
int sumT;

void clearCount()
{
	sumO = 0;
	sumX = 0;
	sumT = 0;
}

void findSymbol(int yy, int xx)
{
	if(maze[yy][xx] == 'X') sumX++;
	if(maze[yy][xx] == 'T') sumT++;
	if(maze[yy][xx] == 'O') sumO++;
}

void countHorRight(int yy)
{
	for(int i=0;i<4;i++) //column
	{
		findSymbol(yy,i);
	}
}

void countDigRight(int yy, int xx)
{
	for(int i=0;i<4;i++) //column
	{
		findSymbol(yy+i,xx+i);
	}
}

void countDigLeft(int yy, int xx)
{
	for(int i=0;i<4;i++) //column
	{
		findSymbol(yy+i,xx-i);
	}
}

void countVerDown(int xx)
{
	for(int i=0;i<4;i++) //row
	{
		findSymbol(i,xx);
	}
}

int isAnyWinner()
{
	if((sumX == 4) || (sumX == 3 && sumT == 1) )
	{
		return 1;
	}

	if((sumO == 4) || (sumO == 3 && sumT == 1) )
	{
		return 2;
	}

	return 0;
}

int checkGame()
{
	int totalFilled = 0;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(maze[i][j] != '.') totalFilled++;
		}
	}
	if(totalFilled == 16) return 3;
	return 4;
}

int checkWinner(int yy, int xx)
{
	int res = 0;
	if (yy == 0 && xx == 0)	//complete check
	{
		clearCount();
		countHorRight(yy);
		res = isAnyWinner();
		if(res > 0)
		{
			return res;
		}

		clearCount();
		countVerDown(xx);
		res = isAnyWinner();
		if(res > 0)
		{
			return res;
		}

		clearCount();
		countDigRight(yy,xx);
		res = isAnyWinner();
		if(res > 0)
		{
			return res;
		}
	}
	else if (yy == 0 && (xx == 1 || xx == 2))
	{
		clearCount();
		countVerDown(xx);
		res = isAnyWinner();
		if(res > 0)
		{
			return res;
		}
	}
	else if (yy == 0 && (xx == 3))
	{
		clearCount();
		countVerDown(xx);
		res = isAnyWinner();
		if(res > 0)
		{
			return res;
		}

		clearCount();
		countDigLeft(yy,xx);
		res = isAnyWinner();
		if(res > 0)
		{
			return res;
		}
	}
	else if ((yy == 1 || yy == 2 || yy == 3) && xx == 0)
	{
		clearCount();
		countHorRight(yy);
		res = isAnyWinner();
		if(res > 0)
		{
			return res;
		}
	}
	return res;
}

int main()
{
	freopen("tictactoe.in","r",stdin);
	freopen("tictactoe.out","w",stdout);
	int cases;
	int i,j,k,l;
	char s[100];
	int winnerFound;
	scanf("%s",s);
	cases = atoi(s);
	for(i=0;i<cases;i++)
	{
		for(j=0;j<4;j++)
		{
			scanf("%s",maze[j]);

		}
		for(k=0;k<4;k++)
		{
			winnerFound = 0;
			for(l=0;l<4;l++)
			{
				winnerFound = checkWinner(k,l);
				if(winnerFound > 0)
				{
					if(winnerFound == 1)
					{
						printf("Case #%d: X won\n",i+1);
					}
					else if(winnerFound == 2)
					{
						printf("Case #%d: O won\n",i+1);
					}
					break;
				}
			}
			if(winnerFound > 0) break;
		}
		if(!winnerFound)
		{
			if(checkGame() == 3)
			{
				printf("Case #%d: Draw\n",i+1);
			}
			else
			{
				printf("Case #%d: Game has not completed\n",i+1);
			}
		}
	}
	return 0;
}




