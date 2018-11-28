#include <stdio.h>

int main()
{
	int cas;
	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out" , "w" , stdout);
	scanf("%d" , &cas);
	for (int ca = 1; ca <= cas; ca ++)
	{
		int x , s , r , t , n;
		int L[120] = {0};
		scanf("%d %d %d %d %d" , &x , &s , &r , &t , &n);
		L[0] = x;
		for (int i = 0; i < n; i ++)
		{
			int b , e , w;
			scanf("%d %d %d" , &b , &e , &w);
			L[w] += e - b;
			L[0] -= e - b;
		}
		double tt = t;
		double res = 0;
		for (int i = 0; i <= 100; i ++)
			if (L[i] > 0)
			{
				if (tt > 1e-7)
				{
					if (1.0 * L[i] / (i + r) <= tt)
					{
						res += 1.0 * L[i] / (i + r);
						tt -= 1.0 * L[i] / (i + r);
					}
					else
					{
						res += tt + 1.0 * (L[i] - (i+r)*tt) / (i + s);
						tt = 0;
					}
				}
				else
					res += 1.0 * L[i] / (i + s);
			}
		printf("Case #%d: %lf\n" , ca , res);
	}
	return 0;
}