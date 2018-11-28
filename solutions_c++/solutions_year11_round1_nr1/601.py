#include <stdio.h>

int gcd(int a, int b)
{
	while (b!=0)
	{
		a = a % b;
		a = a ^ b;
		b = a ^ b;
		a = a ^ b;
	}

	return a;
}

int main()
{
	int i, j, t, T, pg, pd, wd, d, wg, g;
	long long n;

	freopen("1.txt", "rb", stdin);
	freopen("outa.txt", "wb", stdout);
	scanf("%d", &T);
	for (t=1; t<=T; t++)
	{
		scanf("%lld%d%d", &n, &pd, &pg);

		if (pg == 100 && pd != 100)
		{
			printf("Case #%d: Broken\n", t);
			continue;
		}

		d = 100;
		wd = pd;
		i = gcd(d, wd);
		d = d / i;

		if (d <= n)
			printf("Case #%d: Possible\n", t);
		else
			printf("Case #%d: Broken\n", t);
	}

	return 0;
}