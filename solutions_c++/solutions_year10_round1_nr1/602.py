// cj1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

char board1[64][64];
char board2[64][64];
int n, k;

bool Check(char tag)
{
	for (int y = 0; y < n; y++)
	{
		for (int x = 0; x < n; x++)
		{
			if (board2[y][x] != tag)
				continue;
			int dx[] = { 0, -1, 1, 1 };
			int dy[] = { 1, 1, 1, 0 };
			for (int t = 0; t < 4; t++)
			{
				int i;
				for (i = 1; i < k; i++)
				{
					int xx = x + dx[t]*i;
					int yy = y + dy[t]*i;
					if (xx < 0 || xx >= n || yy < 0 || yy >= n)
						break;
					if (board2[yy][xx] != tag)
						break;
				}
				if (i == k)
				{
					return true;
				}
			}

		}
	}
	return false;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	scanf("%d", &t);
	for (int c = 1; c <= t; c++)
	{
		printf("Case #%d: ", c);
		scanf("%d %d", &n, &k);
		for (int j = 0; j < n; j++)
		{
			scanf("%s", board1[j]);
		}
		memset(board2, 0, sizeof(board2));
		//rotate...
		for (int x = 0; x < n; x++)
		{
			for (int y = 0; y < n; y++)
			{
				board2[y][x] = board1[n-1-x][y];
			}
		}
		/*for (int y = 0; y < n; y++)
			printf("%s\n", board2[y]);
		*/
		//grace
		bool bMove;
		do
		{
			bMove = false;
			for (int y = n-1; y > 0; y--)
			{
				for (int x = 0; x < n; x++)
				{
					if (board2[y][x] == '.' && board2[y-1][x] != '.')
					{
						board2[y][x] = board2[y-1][x];
						board2[y-1][x] = '.';
						bMove = true;
					}
				}
			}
		} while(bMove);
		//print...
		/*for (int y = 0; y < n; y++)
			printf("%s\n", board2[y]);
		*/
		bool bRed = Check('R');
		bool bBlue = Check('B');
		if (bRed && bBlue)
			printf("Both\n");
		else if (bRed)
			printf("Red\n");
		else if (bBlue)
			printf("Blue\n");
		else
			printf("Neither\n");
	}
	return 0;
}

