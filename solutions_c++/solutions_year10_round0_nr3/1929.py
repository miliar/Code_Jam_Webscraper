#include <cstdio>

int main()
{
	int i, j, l, idx;
	int T, R, k, N;
	long long res;
	int t[1000];
	long long g[1000], v[1000];

	scanf("%d", &T);

	for (l = 1 ; l <= T ; l++)
	{
		scanf("%d", &R);
		scanf("%d", &k);
		scanf("%d", &N);

		for (j = 0 ; j < N ; j++)
		{
			scanf("%lld", &g[j]);
			v[j] = 0;
		}

		for (i = 0 ; i < N ; i++)
		{
			j = i;
			do
			{
				v[i] += g[j];

				if (++j >= N)
				{
					j = 0;
				}

				t[i] = j;
			}
			while ((j != i) && (v[i] + g[j] <= k));
		}

		idx = 0;
		res = 0;
		for (i = 0 ; i < R ; i++)
		{
			res += v[idx];
			idx = t[idx];
		}

		printf("Case #%d: %lld\n", l, res);
	}

	return 0;
}
