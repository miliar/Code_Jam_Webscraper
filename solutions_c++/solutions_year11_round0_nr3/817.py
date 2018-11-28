#include <stdio.h>

int main ()
{
	//freopen("C-large (1).in", "r", stdin);
	//freopen("C-large (1).out", "w", stdout);
	int ca;
	scanf("%d", &ca);
	int cas = 0;
	while (ca--)
	{
		int n;
		scanf("%d", &n);
		int sum = 0;
		int xx = 0;
		int minx = 0x7fffffff;
		while (n--)
		{
			int x;
			scanf("%d", &x);
			xx ^= x; sum += x;
			if (x < minx) minx = x;
		}
		printf("Case #%d: ", ++cas);
		if (xx == 0) printf("%d\n", sum - minx);
		else printf("NO\n");
	}
	return 0;
}
			
