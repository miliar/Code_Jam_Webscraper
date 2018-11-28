#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAXN 64

char g[MAXN][MAXN];

int n, k;

void gira (void)
{
	char copy[MAXN][MAXN];

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			copy[j][n-1-i] = g[i][j];
		}
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			g[i][j] = copy[i][j];
		}
	}
}

void gravidade (void)
{
	for (int j = 0; j < n; j++)
	{
		for (int  k = 0; k < n; k++)
		{
			for (int i = n-1; i > 0; i--)
			{
				if (g[i][j] == '.')
				{
					g[i][j] = g[i-1][j];
					g[i-1][j] = '.';
				}
			}
		}
	}
}

bool row (int i, int j)
{
	int count = 0;

	for (int x = j; x < n; x++)
	{
		if (g[i][x] == g[i][j])
			count++;
		else
			break;

		if (count == k) { return true; }
	}

	return false;
}

bool column (int i, int j)
{
	int count = 0;

	for (int x = i; x < n; x++)
	{
		if (g[x][j] == g[i][j])
			count++;
		else
			break;

		if (count == k) { return true; }
	}

	return false;
}

bool diagonal1 (int i, int j)
{
	int count = 0;

	for (int x = i, y = j; x < n && y < n; x++, y++)
	{
		if (g[x][y] == g[i][j])
			count++;
		else
			break;

		if (count == k) { return true; }
	}

	return false;
}

bool diagonal2 (int i, int j)
{
	int count = 0;

	for (int x = i, y = j; x < n && y >= 0; x++, y--)
	{
		if (g[x][y] == g[i][j])
			count++;
		else
			break;

		if (count == k) { return true; }
	}

	return false;
}

void winner (bool &r, bool &b)
{
	b = false;
	r = false;

	for (int i = 0; i < n && (!b || !r); i++)
	{
		for (int j = 0; j < n && (!b || !r); j++)
		{
			if (g[i][j] == '.') continue;

			if (g[i][j] == 'B' && !b)
				b = b || row(i, j) || column(i, j) || diagonal1(i, j) || diagonal2(i, j);
			else if (g[i][j] == 'R' && !r)
				r = r || row(i, j) || column(i, j) || diagonal1(i, j) || diagonal2(i, j);
		}
	}
}

int main (void)
{
	int tests;
	bool b, r;

	scanf ("%d", &tests);

	for (int tc = 1; tc <= tests; tc++)
	{
		scanf ("%d %d", &n, &k);

		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				scanf (" %c", &g[i][j]);
			}
		}

		gira();

		gravidade();
/*
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				printf ("%c", g[i][j]);
			}
			printf ("\n");
		}
*/
		winner (r, b);

		printf ("Case #%d: ", tc);

		if (r && b) printf ("Both\n");
		else if (r) printf ("Red\n");
		else if (b) printf ("Blue\n");
		else printf ("Neither\n");
	}

	return 0;
}
