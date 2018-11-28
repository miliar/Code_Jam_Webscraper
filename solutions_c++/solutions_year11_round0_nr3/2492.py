#include<cstdio>
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t, tt;
	scanf("%d", &t);
	for(tt = 0; tt < t; ++tt)
	{
		int i, k, n;
		int sum = 0, min = 1000*1000;
		int pr = 0;
		scanf("%d", &n);
		for(i = 0; i < n; ++i)
		{
			scanf("%d", &k);
			pr ^= k;
			sum += k;
			if(k < min)
				min = k;
		}
		printf("Case #%d: ", tt+1);
		if(pr != 0)
			printf("NO\n");
		else
			printf("%d\n", sum - min);
	}
	return 0;
}