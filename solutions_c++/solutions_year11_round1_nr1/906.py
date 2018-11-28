#include <stdio.h>

int gcd(int x, int y)
{
	if (y == 0)
		return x;
	else
		return gcd(y, x % y);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, pd, pg;
	__int64 n;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		scanf("%I64d %d %d", &n, &pd, &pg);
		if ((pg == 100 && pd != 100) || (pg == 0) && pd != 0)
		{
			printf("Case #%d: Broken\n", i);
			continue;
		}
		int gg = gcd(pd, 100);
		gg = 100 / gg;
		if (gg <= n)
			printf("Case #%d: Possible\n", i);
		else
			printf("Case #%d: Broken\n", i);
	}
	return 0;
}