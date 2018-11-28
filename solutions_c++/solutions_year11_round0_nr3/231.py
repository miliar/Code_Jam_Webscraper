#include<stdio.h>

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int ntest, n, x;
	scanf("%d", &ntest);
	for(int test = 1; test <= ntest; test++)
	{
		scanf("%d", &n);
		int XOR = 0, MIN = 100000000, total = 0;
		for(int i=0; i<n; i++)
		{
			scanf("%d", &x);
			XOR ^= x; total += x;
			if(MIN > x) MIN = x;
		}

		printf("Case #%d: ", test);
		if(XOR != 0) printf("NO\n");
		else printf("%d\n", total - MIN);
	}

	return 0;
}
