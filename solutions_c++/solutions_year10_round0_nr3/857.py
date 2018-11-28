#include <cstdio>

const int NMAX = 10000;

long long group[NMAX], max[NMAX], ind[NMAX];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int CountTest;

	scanf("%d", &CountTest);
	for (int index = 0; index < CountTest; ++index)
	{
		int n;
		long long r, k;

		scanf("%lld%lld%d", &r, &k, &n);
		for (int i = 0; i < n; ++i)
			scanf("%lld", &group[i]);

		for (int i = 0; i < n; ++i)
		{
			if (group[i] > k)
			{
				max[i] = 0;
				ind[i] = i;
				continue;
			}

			long long sum = group[i], j;
			for (j = (i + 1) % n; j % n != i && sum + group[j % n] <= k; ++j)
				sum += group[j % n];

			ind[i] = j % n;			
			max[i] = sum;
		}

		long long res = 0, start = 0;
		for (int i = 0; i < r; ++i)
		{
			res += max[start];
			start = ind[start];
		}

		printf("Case #%d: %lld\n", index + 1, res);
	}

	return 0;
}