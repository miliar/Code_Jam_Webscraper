#include<cstdio>

int main()
{
    freopen("C-large.in","r", stdin);
    freopen("output.txt","w",stdout);
	int cases;
	scanf("%d" , &cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		int n;
		scanf("%d" , &n);
		int xsum = 0;
		int sum = 0;
		int minimum = 0x7fffffff;
		for (int i = 0; i < n; ++i)
		{
			int x;
			scanf("%d" , &x);
			xsum ^= x;
			sum += x;
			if (x < minimum) minimum = x;
		}
		printf("Case #%d: ", ca);
		if (xsum) puts("NO"); else printf("%d\n", sum - minimum);
	}
}
