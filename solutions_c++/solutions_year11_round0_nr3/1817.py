#include<cstdio>
#include<cstdlib>
#include<cstring>

int main()
{
	int T, cas;
	scanf("%d", &T);
	for(cas = 1; cas <= T; cas ++)
	{
		int i, n, a[1001], ch, min, sum;
		scanf("%d", &n);
		sum = ch = 0;
		min = 1000000000;
		for(i = 0; i < n; i ++)
		{
			scanf("%d", &a[i]);
			ch ^= a[i];
			if(min > a[i])min = a[i];
			sum += a[i];
		}
		if(ch == 0)
		{
			printf("Case #%d: %d\n", cas, sum-min);
		}
		else {
			printf("Case #%d: NO\n", cas);
		}
	}
	return 0;
}
