#include <cstdio>

using namespace std;

#define LIMIT 1000000

int is_prime[LIMIT + 1];

void init()
{
	is_prime[2] = true;
	for (int i = 3;i <= LIMIT;i += 2)
	{
		int b = false;
		for (int j = 3;j * j <= i;j++)
		{
			if (i % j == 0)
			{
				b = true;
				break;
			}
		}

		if (!b)
			is_prime[i] = true;
	}
}

long long log(long long v, long long b)
{
	long long ret = 0;
	for (;v;ret++, v /= b);

	return ret - 1;
}

long long ans(long long N)
{
	if (N == 1)
		return 0LL;
	long long ret = 1;

	ret += log(N, 2) - 1;

	for (long long i = 3;i * i <= N;i += 2)
	{
		if (!is_prime[i])
			continue;
		ret += log(N, i) - 1;
	}

	return ret;
}

int main()
{
	init();
	int t;
	scanf("%d", &t);
	for (int ti = 1;ti <= t;ti++)
	{
		fprintf(stderr, "Case %d\n", ti);

		long long N;
		scanf("%lld", &N);

		printf("Case #%d: %lld\n", ti, ans(N));
	}
	return 0;
}
