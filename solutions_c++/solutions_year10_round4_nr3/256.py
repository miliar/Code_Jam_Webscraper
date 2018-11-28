#include <iostream>
#include <algorithm>
using namespace std;

const int	MAXN	=	100 + 1;

int		grids[MAXN][MAXN];
int		R, N, T;

void Init ()
{
	memset (grids, 0, sizeof (grids));

	scanf ("%d", &R);
	for (int i = 0; i < R; ++i)
	{
		int x1, y1, x2, y2;
		scanf ("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int x = x1; x <= x2; ++x)
		for (int y = y1; y <= y2; ++y)
			grids[x][y] = 1;
	}
}

bool empty ()
{
	for (int i = 1; i <= 100; ++i)
	for (int j = 1; j <= 100; ++j)
		if (grids[i][j] == 1)
			return false;

	return true;
}

void print ()
{
	for (int i = 1; i <= 10; ++i)
	{
		for (int j = 1; j <= 10; ++j)
			printf ("%d", grids[i][j]);
		printf ("\n");
	}
}

void Solve ()
{
	int bak[101][101];
	int ret = 0;
	while (!empty ())
	{
		memcpy (bak, grids, sizeof (grids));
		for (int i = 1; i <= 100; ++i)
		for (int j = 1; j <= 100; ++j)
			if (grids[i][j] == 1)
			{
				if ((i == 1 || bak[i - 1][j] == 0) && (j == 1 || bak[i][j - 1] == 0))
					grids[i][j] = 0;
			} else
			{
				if (bak[i - 1][j] == 1 && bak[i][j - 1] == 1)
					grids[i][j] = 1;
			}
		
		ret ++;
				//print ();
	}

	printf ("%d\n", ret);
}

int main()
{
	freopen ("C-small-attempt0.in", "r", stdin);
	freopen ("ou.txt", "w", stdout);

	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf ("Case #%d: ", i);
		Init ();
		Solve ();
	}
	
	return 0;
}
