// Tile.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>

bool debug = false;

const int MaxR = 50;
const int MaxC = 50;

void PrintGrid(char grid[MaxR][MaxC], int R, int C);

int _tmain(int argc, _TCHAR* argv[])
{
	int T;

	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		int R, C;
		char row[80];
		char grid[MaxR][MaxC];
		int blueCount = 0;

		scanf("%d %d", &R, &C);

		fgets(row, 80, stdin);

		for (int r = 0; r < R; r++)
		{
			fgets(row, 80, stdin);
			if (debug)
			{
				printf("%2d: |%s|\n", r, row);
			}
			for (int c = 0; c < C; c++)
			{
				grid[r][c] = row[c];
				if (row[c] == '#')
				{
				   blueCount++;
				}
			}
		}

		if (debug)
		{
			PrintGrid(grid, R, C);
			printf("blueCount %d\n", blueCount);
		}

		for (int r = 0; r < R; r++)
		{
			for (int c = 0; c < C; c++)
			{
				if ((r + 1 < R) && (c + 1 < C))
				{
					if ((grid[r][c] == '#') &&
						(grid[r+1][c] == '#') &&
						(grid[r][c+1] == '#') &&
						(grid[r+1][c+1] == '#'))
					{
						grid[r][c] = '/';
						grid[r][c+1] = '\\';
					    grid[r+1][c] = '\\';
						grid[r+1][c+1] =  '/';
						blueCount -= 4;
					}
				}
			}
		}

		printf ("Case #%d:\n", t);

		if (blueCount == 0)
		{
			PrintGrid(grid, R, C);
		}
		else
		{
			printf("Impossible\n");
			if (debug)
			{
				printf("blueCount = %d\n", blueCount);
				PrintGrid(grid, R, C);
			}
		}
	}

	return 0;
}

void PrintGrid(char grid[MaxR][MaxC], int R, int C)
{
  for (int r = 0; r < R; r++)
  {
	  for (int c = 0; c < C; c++)
	  {
		  printf("%c", grid[r][c]);

	  }
	  printf("\n");
  }

}

