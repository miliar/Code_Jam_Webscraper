#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

const	int	limitSize	= 50 + 5;

int		n , m;
int		tar	[limitSize][limitSize];

void	init()
{
	scanf("%d%d" , &n , &m);

		for (int i = 1; i <= n; i ++)
			for (int j = 1; j <= m; j ++)
				scanf("%d" , &tar[i][j]);
}

int		ret;
int		mat	[limitSize][limitSize];

inline	bool	valid(int x , int y)
{
	return	1 <= x && x <= n && 1 <= y && y <= m;
}

void	check()
{
	int	x , y;
	for (x = 1; x <= n; x ++)
		for (y = 1; y <= m; y ++)
		{
			if (x + y > 1 + n && x + y > 1 + m)
			{
				mat[x][y] = tar[x - 1][y - 1]
						- mat[x - 1][y] - mat[x - 2][y]
						- mat[x][y - 1] - mat[x - 1][y - 1] - mat[x - 2][y - 1]
						- mat[x][y - 2] - mat[x - 1][y - 2] - mat[x - 2][y - 2];
				if (mat[x][y] != 0 && mat[x][y] != 1)
					return;
			}
		}
	for (x = 1; x <= n; x ++)
		if (tar[x][m] !=  mat[x][m] + mat[x][m - 1]
				+ mat[x-1][m] + mat[x-1][m - 1]
				+ mat[x+1][m] + mat[x+1][m - 1])
					return;
	for (y = 1; y <= m; y ++)
		if (tar[n][y] !=  mat[n][y] + mat[n - 1][y]
				+ mat[n][y-1] + mat[n - 1][y-1]
				+ mat[n][y+1] + mat[n - 1][y+1])
					return;


	int	tmp = 0;
	for (y = 1; y <= m; y ++)
		tmp += mat[(n + 1) / 2][y];
	if (tmp > ret) ret = tmp;
}

void	makeSearch(int p)
{
	if (p > n && p > m)
	{
		check();
		return;
	}

	int	x , y;

	for (mat[1][p] = 1; mat[1][p] >= 0; mat[1][p] --)
	{
		for (mat[p][1] = 1; mat[p][1] >= 0; mat[p][1] --)
		{
			x = 2; y = p - 1;
			while (y > 1)
			{
				if (valid(x,y))
				{
					mat[x][y] = tar[x - 1][y - 1]
						- mat[x - 1][y] - mat[x - 2][y]
						- mat[x][y - 1] - mat[x - 1][y - 1] - mat[x - 2][y - 1]
						- mat[x][y - 2] - mat[x - 1][y - 2] - mat[x - 2][y - 2];
					if (mat[x][y] != 0 && mat[x][y] != 1)
						goto next_loop;
				}
				x ++; y --;
			}

			makeSearch(p + 1);

			next_loop:
			if (p > n) break;
		}
		if (p > m) break;
	}
}

void	solve()
{
	ret = -1;

	memset(mat , 0 , sizeof(mat));

	mat[1][1] = 0;
	makeSearch(2);
	mat[1][1] = 1;
	makeSearch(2);
	

	printf("%d\n" , ret);
}

int	main()
{
	//freopen("in.txt" , "r" , stdin);
	//freopen("C-small-attempt0.in" , "r" , stdin);
	freopen("C-small-attempt1.in" , "r" , stdin);
	//freopen("C-large.in" , "r" , stdin);

	freopen("C-small.out" , "w" , stdout);
	//freopen("C-large.out" , "w" , stdout);

	int	t , x = 0;
	for (scanf("%d" , &t); t > 0; t --)
	{
	//	fprintf(stderr , "%d cases left\n" , t);

		init();
		printf("Case #%d: " , ++ x);
		solve();		
	}

	return 0;
}