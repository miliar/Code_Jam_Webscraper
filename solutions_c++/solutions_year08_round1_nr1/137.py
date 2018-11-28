
	#include <stdio.h>
	#include <stdlib.h>
	#include <memory.h>
	#include <algorithm>
	using namespace std;
	/*
		
	*/

	int a[100010], b[100010], n;

	void work()
	{
		scanf("%d", &n);
		for (int i = 1; i <= n; i ++)
			scanf("%d", &a[i]);
		for (int j = 1; j <= n; j ++)
			scanf("%d", &b[j]);
		for (int i = 1; i < n; i ++)
			for (int j = i + 1; j <= n; j ++)
				if (a[i] > a[j])
		{
			a[0] = a[i]; a[i] = a[j]; a[j] = a[0];
		}
		for (int i = 1; i < n; i ++)
			for (int j = i + 1; j <= n; j ++)
				if (b[i] > b[j])
		{
			b[0] = b[i]; b[i] = b[j]; b[j] = b[0];
		}
		int ans = 0;
		for (int i = 1; i <= n; i ++)
			ans += a[i] * b[n + 1 - i];
		printf("%d\n", ans);
	}

	int main()
	{
		freopen("A-small-attempt0.in", "r", stdin);
		freopen("a.out", "w", stdout);
		int tests;
		scanf("%d", &tests);
		for (int i = 1; i <= tests; i ++)
		{
			printf("Case #%d: ", i);
			work();
		}
		return 0;
	}
