#include <stdio.h>

int main ()
{
	freopen("D-large (1).in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int k;
	scanf("%d", &k);
	for (int j = 1; j <= k; j++)
	{
		int n, a, s = 0;
		scanf("%d", &n);
		for (int i = 1; i <= n; i++)
		{
			scanf("%d", &a);
			if (a != i) 
			{
				s++;
			}
		}
		printf("Case #%d: %d.000000\n", j, s);
	}
	return 0;
}
