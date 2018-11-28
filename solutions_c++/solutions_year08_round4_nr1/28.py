#include <cstdio>
#include <cstring>

const	int	limitSize = 10000 + 10;
const	int	infinity  = 123456789;

int		n , v;
int		value	[limitSize];
int		gate	[limitSize];

void	init()
{
	scanf("%d%d" , &n , &v);
	for (int i = 1; i <= n; i ++)
	{
		if (i * 2 <= n)
		{
			scanf("%d%d" , gate + i , value + i);
		}
		else	scanf("%d" , value + i);
	}
}

int		opt	[limitSize][2];

void	renew(int& x , int x0)
{
	if (x0 < x) x = x0;
}

void	solve()
{
	memset(opt , 0x3f , sizeof(opt));

	int	i;
	int	a , b , x , y;
	for (i = n; i >= 1; i --)
	{
		if (i * 2 > n)
		{
			opt[i][ value[i] ] = 0;
		}
		else
		{
			a = 2 * i;
			b = 2 * i + 1;
			for (x = 0; x < 2; x ++)
				for (y = 0; y < 2; y ++)
					if (opt[a][x] <= n && opt[b][y] <= n)
				{
					if (gate[i] == 1)
					{
						renew(opt[i][x & y] , opt[a][x] + opt[b][y]);
						if (value[i])
							renew(opt[i][x | y] , opt[a][x] + opt[b][y] + 1);
					}
					else
					{
						renew(opt[i][x | y] , opt[a][x] + opt[b][y]);
						if (value[i])
							renew(opt[i][x & y] , opt[a][x] + opt[b][y] + 1);
					}
				}
		}
	}

	if (opt[1][v] <= n)
		printf("%d\n" , opt[1][v]);
	else	printf("IMPOSSIBLE\n");
}

int	main()
{
//	freopen("A-small-attempt0.in" , "r" , stdin);
	freopen("Alarge.out" , "w" , stdout);
	freopen("A-large.in" , "r" , stdin);

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
