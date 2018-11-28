#include <stdio.h>
#include <math.h>
int main()
{
	int ncase, pcase;
	int n, m, a;
	int x, x1, x2, x3, y, y1, y2, y3;
	int u, v;
	int t;
	bool found = false;
	scanf("%d", &ncase);
	for (pcase = 1; pcase <= ncase; pcase++)
	{
		scanf("%d %d %d", &n, &m, &a);
		found = false;
		/*
		for (x1 = 0; x1 <= n; x1++)
			for (y1 = 0; y1 <= m; y1++)
			*/
		x1 = 0;
		y1 = 0;
				for (x2 = 0; x2 <= n; x2++)
					for (y2 = 0; y2 <= m; y2++)
						for (x3 = 0; x3 <= n; x3++)
							for (y3 = 0; y3 <= m; y3++)
							{
								u = x2 - x1;
								v = y2 - y1;
								x = x3 - x1;
								y = y3 - y1;
								t = abs(u * y - x * v);
								if (t == a)
								{
									found = true;
									goto out;
								}
							}
out:
		printf("Case #%d: ", pcase);
		if (found)
		{
			printf("%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3);
		}else
		{
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}