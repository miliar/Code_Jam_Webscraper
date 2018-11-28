#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace::std;

int main()
{
	int i, j, x, p, sum, Min, n, t;

	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	for (i = 1, scanf("%d", &t); i <= t; ++i)
	{
		printf("Case #%d: ", i);
		Min = 2147483647;
		sum = p = 0;
		for (j = 1, scanf("%d", &n); j <= n; ++j)
		{
			scanf("%d", &x);
			sum += x;
			p ^= x;
			Min = min(Min, x);
		}
		if (p) printf("NO\n");
		else printf("%d\n", sum - Min);
	}

	return 0;
}