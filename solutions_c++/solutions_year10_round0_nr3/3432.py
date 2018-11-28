#include <stdio.h>

long long groups[1010];
long long mem[1010];
long long runs[1010];

long long t, r, k, n;

int main()
{
	scanf("%lld", &t);
	for (long long z = 0; z < t; z++)
	{
		scanf("%lld %lld %lld", &r, &k, &n);
		for (long long i = 0; i < n; i++)
		{
			scanf("%lld", &groups[i]);
			mem[i] = -1;
			runs[i] = 0;
		}

		long long money = 0;
		long long start = 0;
		long long left = k;
		bool end = false;
		for (long long i = 1; i <= r; i++)
		{
			bool first = true;
			long long actual = start;
			long long total = 0;

			if ((end) && (mem[actual] != -1))
			{
				long long q = (r - i + 1) / (i - 1 - runs[actual]);
				long long m = money - mem[actual];
				i += q * (i - 1 - runs[actual]);
				money += q * m;
			}

			if (i > r) break;

			while (1)
			{
				if ((!first) && (actual == start)) break;
				first = false;
				if (total + groups[actual] > k) break;
				total += groups[actual];
				actual = (actual + 1) % n;
			}
			money += total;
			if (mem[actual] == -1)
			{
				mem[actual] = money;
				runs[actual] = i;
			}
			else end = true;
			start = actual;

		}
		printf("Case #%lld: %lld\n", z + 1, money);
	}
	return 0;
}
