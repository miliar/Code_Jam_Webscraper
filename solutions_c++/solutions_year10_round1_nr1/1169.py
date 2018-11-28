#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;

int main()
{
	freopen("a.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int kase, tCase = 0;
	scanf ("%d",&kase);

	while (kase--)
	{
		int N, K, i, j, len, last, col, row, p, m;
		scanf ("%d%d",&N,&K);
		getchar();
		char grid[55][55], input[100];
		for (i=0; i<55; i++)
			for (j=0; j<55; j++)
				grid[i][j] = '.';
		last = (54-N+1);
		col = 54;
		for (p=54; p>=last; p--)
		{
			row = 54;
			gets(input);
			len=strlen(input);
			for (m=len-1; m>=0; m--)
				if (input[m] != '.')
				{
					grid[row][col] = input[m];
					row--;
				}
			col--;
		}
		int r = 1, b = 1, found, flag = 0; // 1 mane jite nai.
//		while (r)
		{
			for (i=0; i<55; i++)
			{
				for (j=0; j<55; j++)
				{
					found = 0;
					if (grid[i][j] == 'R')
					{
						int rowc, colc;
						for (rowc = i; rowc<55; rowc++)
							if (grid[rowc][j] == 'R') found++;
							else break;
						if (found >= K)
						{
							r=0;
							flag = 1;
							break;
						}
						found = 0;
						for (colc = j; colc<55; colc++)
							if (grid[i][colc] == 'R') found++;
							else break;
						if (found >= K)
						{
							r=0;
							flag = 1;
							break;
						}
						found = 0;
						rowc = i;
						int colcL = j, colcR = j;
						int loop = K;
						while (loop-- && colcL>=0 && rowc<55)
						{
							if (grid[rowc][colcL] == 'R') found++;
							else break;
							colcL--;
							rowc++;
						}
						if (found >= K)
						{
							r=0;
							flag = 1;
							break;
						}
						found = 0;
						rowc = i;
						loop = K;
						while (loop-- && colcR<55 && rowc<55)
						{
							if (grid[rowc][colcR] == 'R') found++;
							else break;
							colcR++;
							rowc++;
						}
						if (found >= K)
						{
							r=0;
							flag = 1;
							break;
						}
					}
				}
				if (flag) break;
			}
		}
		flag = 0;
//		while (b)
		{
			for (i=0; i<55; i++)
			{
				for (j=0; j<55; j++)
				{
					found = 0;
					if (grid[i][j] == 'B')
					{
						int rowc, colc;
						for (rowc = i; rowc<55; rowc++)
							if (grid[rowc][j] == 'B') found++;
							else break;
						if (found >= K)
						{
							b=0;
							flag = 1;
							break;
						}
						found = 0;
						for (colc = j; colc<55; colc++)
							if (grid[i][colc] == 'B') found++;
							else break;
						if (found >= K)
						{
							b=0;
							flag = 1;
							break;
						}
						found = 0;
						rowc = i;
						int colcL = j, colcR = j;
						int loop = K;
						while (loop-- && colcL>=0 && rowc<55)
						{
							if (grid[rowc][colcL] == 'B') found++;
							else break;
							colcL--;
							rowc++;
						}
						if (found >= K)
						{
							b=0;
							flag = 1;
							break;
						}
						found = 0;
						rowc = i;
						loop = K;
						while (loop-- && colcR<55 && rowc<55)
						{
							if (grid[rowc][colcR] == 'B') found++;
							else break;
							colcR++;
							rowc++;
						}
						if (found >= K)
						{
							b=0;
							flag = 1;
							break;
						}
					}
				}
				if (flag) break;
			}
		}
		if (r==0 && b==0)
			printf ("Case #%d: Both\n",++tCase);
		else if (r==0)
			printf ("Case #%d: Red\n",++tCase);
		else if (b==0)
			printf ("Case #%d: Blue\n",++tCase);
		else
			printf ("Case #%d: Neither\n",++tCase);
	}

	return 0;
}