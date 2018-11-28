#include <stdio.h>

int main()
{
int ca;

	freopen("D-large.in" , "r" , stdin);
	freopen("D-large.out" , "w" , stdout);
	scanf("%d" , &ca);
	for (int cas = 1; cas <= ca; cas ++)
	{
		int n;
		scanf("%d" , &n);
		int a[1010] , b[1010] = {0};
		double res = 0;
		for (int i = 1; i <= n; i ++) scanf("%d" , &a[i]);
		for (int i = 1; i <= n; i ++)
			if (b[i] == 0)
			{
				int s = 1;
				int k = i;
				b[i] = 1;
				while (a[k] != i)
				{
					s ++;
					k = a[k];
					b[k] = 1;
				}
				if (s == 1) s = 0;
				res += s;
			}
		printf("Case #%d: %.6lf\n" , cas , res);
	}
	return 0;
}