#include <cstdio>
#include <cstring>

const	int	limitSize	= 50000 + 10;

int		n , k;
char		S	[limitSize];

int		cost	[20][20];

void	init()
{
	scanf("%d" , &k);
	scanf("%s" , S); n = strlen(S);
}

void	process()
{
	int	i , j;
	int	p;

	memset(cost , 0 , sizeof(cost));
	for (i = 0; i < k; i ++)
		for (j = 0; j < k; j ++)
		{
			for (p = 0; p < n; p += k)
				if (S[p + i] != S[p + j]) cost[i][j] ++;
		}
}

int	st , ed;
int	ret;
int	base;

int	opt	[1<<16][16];

inline	void	renew(int& x , int x0)
{
	if (x0 < x) x = x0;
}

void	calc()
{
	int	p;

		
	memset(opt , 0x3f , sizeof(opt));
	//opt[(1<<st) | (1<<ed)][st] = 0;
	opt[(1<<st)][st] = 0;

	int	stat , top = (1 << k) , i;
	for (stat = 1; stat < top; stat ++)
	{
		for (p = 0; p < k; p ++)
		{
			if (opt[stat][p] <= n)
			{
				for (i = 0; i < k; i ++)
					if ( 0 == (stat & (1<<i)) )
					{
						renew(opt[stat | (1<<i)][i] , opt[stat][p] + cost[p][i]);
					}
			}
		}
	}

	for (ed = 0; ed < k; ed ++)
	{
		if (ed == st) continue;
		base = 1;
		for (p = k; p < n; p += k)
			if (S[p - k + ed] != S[p + st]) base ++;
		renew(ret , opt[top - 1][ed] + base);
	}

	//for (p = 0; p < k; p ++)	renew(ret , opt[top - 1][p] + base + cost[p][ed]);
	 
}

void	solve()
{
	ret = n;

	for (st = 0; st < k; st ++)
	{
		calc();
	}

	printf("%d\n" , ret);
}

int	main()
{
	freopen("D-large.in" , "r" , stdin);
	freopen("D_large.out" , "w" , stdout);
	
	int	t , caseNo;

	scanf("%d" , &caseNo);
	for (t = 1; t <= caseNo; t ++)
	{
		printf("Case #%d: " , t);
		init();
		process();
		solve();
	}

	return 0;
}
