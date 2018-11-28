#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define MAXN 1024

int prox[MAXN];
unsigned long long ciclo[MAXN];
unsigned long long total;
int g[MAXN];

int main (void)
{
	int cases, ini;
	unsigned int r, n, k, i;

	scanf ("%d", &cases);

	for (int t = 1; t <= cases; t++)
	{
		scanf ("%u %u %u", &r, &k, &n);

		for (i = 0; i < n; i++)
		{
			scanf ("%d", &g[i]);
		}

		memset (ciclo, 0, sizeof(ciclo));

		total = 0;
		ini = 0;

		for (i = 0; i < r; i++)
		{
			unsigned int tp = 0;
			int j = ini;

			if (ciclo[j] == 0)
			{
				for ( ; tp + g[ini] <= k && (tp == 0 || ini != j); ini = (ini + 1) % n)
				{
					tp += g[ini];
				}
				prox[j] = ini;
				ciclo[j] = tp;
			}
			else
			{
				tp = ciclo[j];
				ini = prox[j];
			}

			total += tp;
		}

		printf ("Case #%d: %I64u\n", t, total);
	}

	return 0;
}
