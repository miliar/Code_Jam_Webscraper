#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAXN 128

char g[MAXN][MAXN];
char cpy[MAXN][MAXN];

int main (void)
{
	int c, r, x, y, x1, x2, y1, y2, ones, count;

	scanf ("%d", &c);

	for (int tests = 1; tests <= c; tests++)
	{
		scanf ("%d", &r);
		
		x = 0;
		y = 0;
		ones = 0;
		memset (g, 0, sizeof(g));

		for (int i = 0; i < r; i++)
		{
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

			if (x2 > x) x = x2;
			if (y2 > y) y = y2;

			for (int j = x1; j <= x2; j++)
			{
				for (int k = y1; k <= y2; k++)
				{
					if (!g[k][j]) ones++;
					g[k][j] = 1;
				}
			}
		}
		x++; y++;
/*
		for (int i = 0; i < y; i++)
		{
			for (int j = 0; j < x; j++)
			{
				printf ("%d ", g[i][j]);
			}
			printf ("\n");
		}
		printf ("%d\n\n", ones);
*/		
		count = 0;
		while (ones)
		{
			ones = 0;
			count++;
			for (int i = 0; i < y; i++)
			{
				for (int j = 0; j < x; j++)
				{
					if (i == 0)
					{
						if (!j)
						{
							cpy[i][j] = 0;
						}
						else if (g[i][j-1] != 1)
						{
							cpy[i][j] = 0;
						}
						else
						{
							cpy[i][j] = g[i][j];
							if (cpy[i][j] == 1) ones++;
						}
					}
					else if (j == 0)
					{
						if (g[i-1][j] != 1)
						{
							cpy[i][j] = 0;
						}
						else
						{
							cpy[i][j] = g[i][j];
							if (cpy[i][j] == 1) ones++;
						}
					}
					else if (g[i-1][j] == 1 && g[i][j-1] == 1)
					{
						ones++;
						cpy[i][j] = 1;
					}
					else if (g[i-1][j] != 1 && g[i][j-1] != 1)
					{
						cpy[i][j] = 0;
					}
					else
					{
						cpy[i][j] = g[i][j];
						if (cpy[i][j] == 1) ones++;
					}
				}
			}

			for (int i = 0; i < y; i++)
			{
				for (int j = 0; j < x; j++)
				{
					g[i][j] = cpy[i][j];
					//printf ("%d ", g[i][j]);
				}
				//printf ("\n");
			}
			//printf ("%d\n\n", ones);
		}

		printf ("Case #%d: ", tests);
		printf ("%d\n", count);
	}

	return 0;
}
