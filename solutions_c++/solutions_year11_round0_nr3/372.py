#include <stdio.h>
#include <stdlib.h>

#define FOR(i, N)	for (int i=0; i<N; ++i)

namespace
{
	const int cMaxN = 1000;
}

int solve(int N, int *list)
{
	{
		int x_sum = 0;
		FOR (i, N) x_sum ^= list[i];

		if (x_sum == 0)
		{
			int sum = 0;
			int min = 1000000;
			FOR (i, N)
			{
				sum += list[i];
				if (min > list[i]) min = list[i];
			}

			return sum - min;
		}
	}
	return 0;
}

int main()
{
	int T = 0; scanf("%d", &T);

	FOR (t, T)
	{
		int N = 0; scanf("%d", &N);
		int list[cMaxN];

		FOR (n, N) scanf("%d", &list[n]);

		int result = solve(N, list);

		if (result == 0) printf("Case #%d: NO\n", t+1);
		else printf("Case #%d: %d\n", t+1, result);
	}

}
