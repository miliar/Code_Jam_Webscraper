#include<stdio.h>
#include<string.h>

int	r, k, n;
__int64	f[3000], a[3000];
int	p[3000];

int	main()
{
	freopen("da.in", "r", stdin);
	freopen("da.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt ++)
	{
		memset(f, 0, sizeof(f));
		memset(p, 0, sizeof(p));
		scanf("%d%d%d", &r, &k, &n);
		for (int i = 1; i <= n; i ++)
		{
			scanf("%I64d", &a[i]);
			a[i + n] = a[i];
		}
		for (int i = 1; i <= n; i ++)
		{
			for (int j = i; j <= i + n - 1; j ++)
			{
				if (f[i] + a[j] <= k) 
				{
					f[i] += a[j];
					p[i] = j;
					if (p[i] > n) p[i] -= n;
				} else break;
			}
		}
		int flag = 1; __int64 tot = 0;
		for (int i = 1; i <= r; i ++)
		{
			tot += f[flag];
			flag = p[flag] + 1;
			if (flag > n) flag -= n;
		}
		printf("Case #%d: %I64d\n", tt, tot);

	}
	
	return 0;
}
