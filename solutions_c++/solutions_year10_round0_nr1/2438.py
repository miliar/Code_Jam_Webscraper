#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>

int main ()
{
	int T, N, K;
//	int map[36];
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);

	scanf ("%d", &T);

	for (int cas = 1; cas <= T; cas++)
	{
		scanf ("%d%d", &N, &K);

/*		for (int i = 0; i < 32; i++)
			map[i] = i * 2 + 1;

		if (N > K)
			printf ("Case #%d: OFF\n", cas);
		else if (map[N-1] == K)
			printf ("Case #%d: ON\n", cas);
		else if (map[N-1] < K)
		{
			if ((K - map[N-1]) % 2 == 0)
				printf ("Case #%d: ON\n", cas);
			else
				printf ("Case #%d: OFF\n", cas);
		}
		else
			printf ("Case #%d: OFF\n", cas);*/
			if (K % (int)pow(2, N) == (int)pow(2, N) - 1)
				printf ("Case #%d: ON\n", cas);
			else
				printf ("Case #%d: OFF\n", cas);
	}
}
