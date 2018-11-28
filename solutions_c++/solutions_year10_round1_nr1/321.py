#include <iostream>
#include <string.h>
#define MAX(a, b)  ((a) > (b) ? (a) : (b))
#define MAXN 55
using namespace std;
char board[MAXN][MAXN];
int n, k;



int left (char c, int x, int y)
{
	int sum = 0;
	int i = y;
	while (i >= 0)
	{
		if (board[x][i] == c)
		{
			sum++;
			i--;
		}
		else
			break;
	}
	return sum;
}

int right (char c, int x, int y)
{
	int sum = 0;
	int i = y;
	while (i < n)
	{
		if (board[x][i] == c)
		{
			sum++;
			i++;
		}
		else
			break;
	}
	return sum;
}

int u (char c, int x, int y)
{
	int sum = 0;
	int i = x;
	while (i >= 0)
	{
		if (board[i][y] == c)
		{
			sum++;
			i--;
		}
		else
			break;
	}
	return sum;
}

int d (char c, int x, int y)
{
	int sum = 0;
	int i = x;
	while (i < n)
	{
		if (board[i][y] == c)
		{
			sum++;
			i++;
		}
		else
			break;
	}
	return sum;
}

int dr (char c, int x, int y)
{
	int sum = 0;
	int i = x, j = y;
	while (i < n && j < n)
	{
		if (board[i][j] == c)
		{
			sum++;
			i++;
			j++;
		}
		else
			break;
	}
	return sum;
}

int ur (char c, int x, int y)
{
	int sum = 0;
	int i = x, j = y;
	while (i >= 0 && j < n)
	{
		if (board[i][j] == c)
		{
			sum++;
			i--;
			j++;
		}
		else
			break;
	}
	return sum;
}

int ul (char c, int x, int y)
{
	int sum = 0;
	int i = x, j = y;
	while (i >= 0 && j >= 0)
	{
		if (board[i][j] == c)
		{
			sum++;
			i--;
			j--;
		}
		else
			break;
	}
	return sum;
}

int dl (char c, int x, int y)
{
	int sum = 0;
	int i = x, j = y;
	while (i < n && j >= 0)
	{
		if (board[i][j] == c)
		{
			sum++;
			i++;
			j--;
		}
		else
			break;
	}
	return sum;
}

void Solve ()
{
	int r = 0, b = 0;
	int i, j;
	char c;
	int sum, tmp;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			sum = 0;
			c = board[i][j];
			if (c == '.' || (c == 'R' && r == 1) || (c == 'B' && b == 1))
				continue;
			sum = left(c, i, j) + right(c, i, j) - 1;
			tmp = u(c, i, j) + d(c, i, j) - 1;
			sum = MAX(sum, tmp);
			tmp = ur(c, i, j) + dl(c, i, j) - 1;
			sum = MAX(sum, tmp);
			tmp = ul(c, i, j) + dr(c, i, j) - 1;
			sum = MAX(sum, tmp);
			if (sum >= k)
			{
				if (c == 'R')
					r = 1;
				else
					b = 1;
			}
		}
	}
	if (r == 0 && b == 0)
	{
		printf("Neither\n");
	}
	else if (r == 1 && b == 0)
	{
		printf("Red\n");
	}
	else if (r == 0 && b == 1)
	{
		printf("Blue\n");
	}
	else
	{
		printf("Both\n");
	}
}

int main()
{
	int t, i, j, f, pos;
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);
	cin>>t;
	for (f = 1; f <= t; f++)
	{
		memset (board, 0, sizeof board);
		cin>>n>>k;
		for (i = 0; i < n; i++)
		{
			scanf("%s", board[i]);
			for (j = n - 1, pos = n - 1; j >= 0; j--)
			{
				if (board[i][j] != '.')
				{
					board[i][pos] = board[i][j];
					if (j != pos)
					{
						board[i][j] = '.';
					}
					pos--;
				}
			}
		}/*
		for (i = 0; i < n; i++)
		{
			printf("%s\n", board[i]);
		}
		printf("\n");*/
		printf("Case #%d: ", f);
		Solve ();
	}
	return 0;
}