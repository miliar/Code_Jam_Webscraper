#include <cstdio>

void test()
{
	int n, q, sum = 0, m = 1e9, all = 0;
	scanf("%d", &n);
	while(n--)
	{
		scanf("%d", &q);
		if(q < m) m = q;
		sum += q;
		all ^= q;
	}
	if(all != 0) printf("NO\n");
	else printf("%d\n", sum-m);
}

int main()
{
	int tt;
	scanf("%d", &tt);
	for(int i = 1; i <= tt; i++)
	{
		printf("Case #%d: ", i);
		test();
	}
}
