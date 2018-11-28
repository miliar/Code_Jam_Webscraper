#include <stdio.h>
#define inf (1000000000000LL)

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long t, l;
	scanf("%lld", &t);
	for (l = 1; l <= t; ++l)
	{
		long long n, x = 0, m = inf, s = 0;
		scanf("%lld", &n);
		while (n--)
		{
			long long c;
			scanf("%lld", &c);
			x ^= c;
			if (m > c)
				m = c;
			s += c;
		}
		printf("Case #%lld: ", l);
		if (x != 0)
			printf("NO\n");
		else
			printf("%lld\n", s - m);
	}
	return 0;
}
