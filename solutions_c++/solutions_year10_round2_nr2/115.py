
	#include <cstdlib>
	#include <cstdio>
	#include <string>
	#include <algorithm>
	#include <iostream>

	using namespace std;

	int N, n, k, b, t;
	int a[105], c[105];

	int work()
	{
		scanf("%d%d%d%d", &n, &k, &b, &t);
		for (int i = 0; i < n; i ++)
			scanf("%d", &a[i]);
		for (int i = 0; i < n; i ++)
			scanf("%d", &c[i]);
		int j = n - 1, ans = 0;
		for (int i = n - 1; i >= 0 && k > 0; i --)
		{
			if (a[i] + c[i] * t >= b)
			{
				k --;
				ans += (j - i);
				j --;
			}
		}
		if (k > 0)	printf("IMPOSSIBLE\n");
		else	printf("%d\n", ans);
	}

	int main()
	{
		freopen("B-large.in", "r", stdin);
		freopen("B.out", "w", stdout);
		scanf("%d", &N);
		for (int i = 1; i <= N; i ++)
		{
			printf("Case #%d: ", i);
			work();
		}
		return 0;
	}
