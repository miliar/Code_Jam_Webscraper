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

const	int	limitSize	=  18;

int		n , m;
char		mat	[limitSize][limitSize];

void	init()
{
	scanf("%d%d" , &n , &m);
	for (int i = 0; i < n; i ++)
	{
		scanf("%s" , mat[i]);
		mat[i][m] = '.';
	}
	for (int i = 0; i <= m; i ++)
		mat[n][i] = '.';
}

int		opt	[limitSize][limitSize][1<<16];

int	calc(int x , int y , int stat)
{
	if (x >= n) return 0;
	if (y >= m) return calc(x + 1 , 0 , stat);

	if (opt[x][y][stat] >= 0)
		return	opt[x][y][stat];

	int	& ret = opt[x][y][stat];

	ret = 0;
	int	bit , gain;
	for (bit = 0; bit <= 1; bit ++)
	{
		if (mat[x][y] == '#') bit = 1;
		if (mat[x][y] == '.') bit = 0;

		gain = 0;
		if (bit) {
			gain += 4;
			if ( y && (stat & (1<<(y-1))) ) gain -= 2;
			if ( stat & (1<<y) ) gain -= 2;
		}

		gain += calc(x , y + 1 , (stat ^ (stat & (1<<y))) | (bit << y));
		if (gain > ret) ret = gain;

		if (mat[x][y] == '#' || mat[x][y] == '.') break;
	}
	
	return	ret;
}

void	solve()
{	
	memset(opt , 0xff , sizeof(opt));
	int	ret = calc(0 , 0 , 0);
	
	printf("%d\n" , ret);
}

int	main()
{
	//freopen("in.txt" , "r" , stdin);
	freopen("E-small-attempt0.in" , "r" , stdin);
	//freopen("E-small-attempt1.in" , "r" , stdin);
	//freopen("E-large.in" , "r" , stdin);

	freopen("E-small.out" , "w" , stdout);
	//freopen("E-large.out" , "w" , stdout);

	int	t , x = 0;
	for (scanf("%d" , &t); t > 0; t --)
	{
		init();
		printf("Case #%d: " , ++ x);
		solve();
	}

	return 0;
}