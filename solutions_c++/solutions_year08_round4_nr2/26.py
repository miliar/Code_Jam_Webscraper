#include <cstdio>

int		n , m , S;

void	init()
{
	scanf("%d%d%d" , &n , &m , &S);
}

bool	factor(int v , int& a , int& b)
{
	if (v == 0)
	{
		a = b = 0; return 1;
	}
	int	st = v / m;
	a = st; 
	if (!a) a ++;
	for (; a <= n; a ++)
	{
		if (v % a == 0)
		{
			b = v / a;
			if (b <= m)
			{
				return 1;
			}
		}
	}
	return 0;
}

void	solve()
{
	int	x2 , y2 , x3 , y3;

	int	y2x3 , x2y3;
	for (y2x3 = 0; ;y2x3 ++)
	{
		x2y3 = y2x3 + S;
		if (x2y3 > n * m) break;
		if (factor(y2x3, x3 , y2)
			&& factor(x2y3 , x2 , y3))
		{
			printf("0 0 %d %d %d %d\n" , x2 , y2 , x3 , y3);
			return;
		}
	}
	puts("IMPOSSIBLE");
}

int	main()
{
	freopen("B-large.in" , "r" , stdin);
	freopen("Blarge.txt" , "w" , stdout);
	
	int	t , caseNo;

	scanf("%d" , &caseNo);
	for (t = 1; t <= caseNo; t ++)
	{
		printf("Case #%d: " , t);
		init();
		solve();
	}

	return 0;
}
