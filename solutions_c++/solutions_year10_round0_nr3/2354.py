#include <cstdio>
#include <cstring>
#include <iostream>

int main ()
{
	int T, R, K, N;
	int group[12];
	freopen ("C-small.in", "r", stdin);
	freopen ("C-small.out", "w", stdout);

	scanf ("%d", &T);
	for (int c = 1; c <= T; c++)
	{
		int money = 0;

		scanf ("%d%d%d", &R, &K, &N);
		for (int i = 0; i < N; i++)
			scanf ("%d", &group[i]);

		int pos = 0;
		int sum = 0;
		int limit = 0;
		for (int i = 0; i < R; i++)
		{
			sum = 0;
			limit = 0;
			while (sum <= K && sum + group[pos] <= K && limit < N)
			{
				sum += group[pos];
				limit++;
				pos++;
				if (pos == N)
					pos = 0;
				if (sum == K)
					break;
			}
			money += sum;
		}
		printf ("Case #%d: %d\n", c, money);
	}
}
