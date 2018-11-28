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

const	int	limitSize	= 100 + 10;
int	n , m;
int	ax , ay;
int	bx , by;
int	sx , sy;

void	init()
{
	scanf("%d%d" , &m , &n);
	scanf("%d%d" , &ay , &ax);
	scanf("%d%d" , &by , &bx);
	scanf("%d%d" , &sy , &sx);
}

int	mark	[limitSize][limitSize];
int	curtMark;
int	cnt;

inline	bool	valid(int x , int y)
{
	return	0 <= x && x < n && 0 <= y && y < m;
}

void	go(int x , int y)
{
	if (! valid(x , y)) return;
	if (curtMark == mark[x][y]) return;
	mark[x][y] = curtMark;
	cnt ++;

	go(x + ax , y + ay);
	go(x + bx , y + by);
	//printf("%d %d\n" , x , y);
}

void	solve()
{
	memset(mark , 0 , sizeof(mark));
	curtMark = 0;

	int	ret = 0;
	int	i , j;
	/*for (i = 0; i < n; i ++)
		for (j = 0; j < m; j ++)
		{
			curtMark ++;
			cnt = 0;
			go(i , j);
			if (cnt > ret) ret = cnt;
		}
		*/
	curtMark ++;
	cnt = 0;
	go(sx , sy);

		printf("%d\n" , cnt);
}

int	main()
{
	//freopen("in.txt" , "r" , stdin);
	freopen("B-small-attempt0.in" , "r" , stdin);
	//freopen("B-small-attempt1.in" , "r" , stdin);
	//freopen("B-large.in" , "r" , stdin);

	freopen("B-small.out" , "w" , stdout);
	//freopen("B-large.out" , "w" , stdout);

	int	t , x = 0;
	for (scanf("%d" , &t); t > 0; t --)
	{
		init();
		printf("Case #%d: " , ++ x);
		solve();
	}

	return 0;
}