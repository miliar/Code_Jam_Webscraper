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

struct	Tdat
{
	int	a , b , c;
};

bool	operator < (const Tdat& A , const Tdat& B)
{
	return	A.a < B.a;
}

const	int	limitSize	= 15000 + 10;

int		n;
Tdat	list	[limitSize];

void	init()
{
	scanf("%d" , &n);
	for (int i = 0; i < n; i ++)
		scanf("%d%d%d" , &list[i].a , &list[i].b , &list[i].c);
	sort(list , list + n);
}

Tdat	tmp	[limitSize];

bool	cmp_b( const Tdat&A , const Tdat& B)
{
	return	A.b < B.b;
}

int	ret;
int	ctree	[limitSize];
int	mark	[limitSize];
int	curtMark;

inline	int	lowbit(int x)
{
	return	x & (x ^ (x - 1));
}

void	add(int c)
{
	c ++;

	while (c <= 10010)
	{
		if (curtMark != mark[c])
			mark[c] = curtMark , ctree[c] = 0;
		ctree[c] ++;
		c += lowbit(c);
	}
}

int	sum(int c)
{
	if (c < 0) return 0;
	c ++;

	int	ret = 0;
	while (c > 0)
	{
		if (curtMark != mark[c])
			mark[c] = curtMark , ctree[c] = 0;
		ret += ctree[c];
		c -= lowbit(c);
	}

	return	ret;
}

void	calc(int m , int left)
{
	curtMark ++;

	int	val , c;
	for (int i = 0; i < m; i ++)
	{
		c = left - tmp[i].b;
		add(tmp[i].c);
		val = sum(c);
		if (val > ret) ret = val;		
	}
}

void	solve()
{
	curtMark = 0;
	memset(mark , 0 , sizeof(mark));

	ret = 0;

	int	i;
	for (i = 0; i < n; i ++)
	{
		if (i == n - 1 || list[i].a != list[i + 1].a)
		{
			int	left = 10000 - list[i].a;

			memcpy(tmp , list , sizeof(Tdat) * (i + 1));
			sort(tmp , tmp + (i + 1) , cmp_b);

			calc(i + 1 , left);
		}
	}


	printf("%d\n" , ret);
}

int	main()
{
	//freopen("in.txt" , "r" , stdin);
	//freopen("A-small-attempt0.in" , "r" , stdin);
	//freopen("A-small-attempt1.in" , "r" , stdin);
	freopen("A-large.in" , "r" , stdin);

	//freopen("A-small.out" , "w" , stdout);
	freopen("A-large.out" , "w" , stdout);


	int	t , x = 0;
	for (scanf("%d" , &t); t > 0; t --)
	{
		init();
		printf("Case #%d: " , ++ x);
		solve();

		fprintf(stderr , "%d\n" , x);
	}	

	return 0;
}