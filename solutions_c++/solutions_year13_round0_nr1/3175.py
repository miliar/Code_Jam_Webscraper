#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

char ar[4][4];

int row(int v)
{
	int X = 0, O = 0;
	for (int i = 0; i < 4; i++)
	{
		if (ar[v][i] == 'X')
		{
			X++;
		}
		if (ar[v][i] == 'O')
		{
			O++;
		}
		if (ar[v][i] == 'T')
		{
			X++, O++;
		}
	}
	if (X == 4)
	{
		return 1;
	}
	if (O == 4)
	{
		return -1;
	}
	return 0;
}

int colon(int v)
{
	int X = 0, O = 0;
	for (int i = 0; i < 4; i++)
	{
		if (ar[i][v] == 'X')
		{
			X++;
		}
		if (ar[i][v] == 'O')
		{
			O++;
		}
		if (ar[i][v] == 'T')
		{
			X++, O++;
		}
	}
	if (X == 4)
	{
		return 1;
	}
	if (O == 4)
	{
		return -1;
	}
	return 0;
}

int diag()
{
	int d1X = 0, d1O = 0, d2X = 0, d2O = 0;
	for (int i = 0; i < 4; i++)
	{
		if (ar[i][i] == 'X')
		{
			d1X++;
		}
		if (ar[i][i] == 'O')
		{
			d1O++;
		}
		if (ar[i][i] == 'T')
		{
			d1O++, d1X++;
		}
	}
	for (int i = 0; i < 4; i++)
	{
		if (ar[3 - i][i] == 'X')
		{
			d2X++;
		}
		if (ar[3 - i][i] == 'O')
		{
			d2O++;
		}
		if (ar[3 - i][i] == 'T')
		{
			d2O++, d2X++;
		}
	}
	if (d1X == 4 || d2X == 4)
	{
		return 1;
	}
	if (d1O == 4 || d2O == 4)
	{
		return -1;
	}
	return 0;
}

void check()
{
	int res = 0;
	for (int i = 0; i < 4; i++)
	{
		int v = row(i);
		if (v != 0)
		{
			if (v > 0)
			{
				printf("X won\n");
			}
			else
			{
				printf("O won\n");
			}
			return;
		}
		v = colon(i);
		if (v != 0)
		{
			if (v > 0)
			{
				printf("X won\n");
			}
			else
			{
				printf("O won\n");
			}
			return;
		}
	}
	int v = diag();
	if (v != 0)
	{
		if (v > 0)
		{
			printf("X won\n");
		}
		else
		{
			printf("O won\n");
		}
		return;
	}
	int empty = 0;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			empty += (ar[i][j] == '.');
		}
	}
	if (empty)
	{
		printf ("Game has not completed\n");
	}
	else
	{
		printf("Draw\n");
	}
}

int t;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n", &t);
	for (int q = 0; q < t; q++)
	{
		for (int i = 0; i < 4; i++)
		{
			scanf("%s", &ar[i]);
		}
		scanf("\n");
		printf("Case #%d: ", q + 1);
		check();
	}
	return 0;
}