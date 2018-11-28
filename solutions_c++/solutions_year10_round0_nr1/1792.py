#include<stdio.h>

int	n, k, m;

int	main()
{
	freopen("da.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	scanf("%d", &m);
	for (int i = 1; i <= m; i ++)
	{
		scanf("%d%d", &n, &k);
		int t = 1;
		for (int j = 1; j <= n; j ++)
		{
			t = t * 2;
		}
		if ((k + 1) % t == 0)
		{
			printf("Case #%d: ON\n", i);
		}
		else
		{
			printf("Case #%d: OFF\n", i);
		}
	}
	
	return 0;
}
