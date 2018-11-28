
	#include <stdio.h>
	#include <stdlib.h>
	#include <memory.h>
	#include <algorithm>
	using namespace std;
	/*
		
	*/

	long long a[100010], b[100010];
	int n;

	void work()
	{
		scanf("%d", &n);
		for (int i = 1; i <= n; i ++)
			scanf("%I64d", &a[i]);
		for (int j = 1; j <= n; j ++)
			scanf("%I64d", &b[j]);
		sort(a + 1, a + n + 1);
		sort(b + 1, b + n + 1);
		long long ans = 0;
		for (int i = 1; i <= n; i ++)
			ans += (a[i] * b[n + 1 - i]);
		printf("%I64d\n", ans);
	}

	int main()
	{
		freopen("A-large.in", "r", stdin);
		freopen("b.out", "w", stdout);
		int tests;
		scanf("%d", &tests);
		for (int i = 1; i <= tests; i ++)
		{
			printf("Case #%d: ", i);
			work();
		}
		return 0;
	}
