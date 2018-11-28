#include <stdio.h>
long long a[500000], c[500000];
long long b[100];
int main()
{
	int ncase, pcase;
	long long i, j, n, m, x, y, z;
	long long total;
	scanf("%d", &ncase);
	for (pcase = 1; pcase <= ncase; pcase++)
	{
		scanf("%lld %lld %lld %lld %lld", &n, &m, &x, &y, &z);
		for (i = 0; i < m; i++)
		{
			scanf("%u", &b[i]);
		}
		for (i = 0; i < n; i++)
		{
			a[i] = b[i % m];
			b[i % m] = ((x % z) * (b[i % m] % z) + (y % z) * ((i + 1) % z)) % z;
//			b[i % m] = (x * b[i % m] + y * (i + 1)) % z;
		}
		total = 1;
		c[0] = 1;
		for (i = 1; i < n; i++)
		{
			c[i] = 1;
			for (j = 0; j < i; j++)
			{
				if (a[j] < a[i])
				{
					c[i] += c[j];
					if (c[i] >= 1000000007) c[i] %= 1000000007;
				}
			}
			total += c[i];
			if (total >= 1000000007) total %= 1000000007;
		}
		printf ("Case #%d: %lld\n", pcase, total);
	}
	return 0;
}
