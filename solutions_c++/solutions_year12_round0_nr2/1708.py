#include <iostream>

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");

int T;
int N, S, p;

int maxim(int x, int y)
{
	if (x < y) return y;
	return x;
}

int main()
{
	fscanf(f, "%d", &T);
	for (int i = 0; i < T; ++i)
	{
		fscanf(f, "%d %d %d", &N, &S, &p);
		int min1 = maxim(3 * p - 2, 0); //bun si nici nu e surprinzator;
		int min2 = maxim(3 * p - 4, 0); //bun dar surprinzator;

		int total = 0;
		int surpinzator = 0;
		int poateFiSurprinzator = 0;
		for (int j = 0; j < N; ++j)
		{
			int x;
			fscanf(f, "%d", &x);
			if (x == 0)
			{
				if (p == 0)
				{
					total++;
				}
			}
			else if (x >= min1) 
			{
				total++;
			}
			else if (x >= min2 && surpinzator < S)
			{
				total++;
				surpinzator++;
			}
			if ((x >= 3 * p - 4))// && (x <= 3 * p + 4))
			{
				poateFiSurprinzator++;
			}
		}

		if ((surpinzator == S) || (surpinzator < S && poateFiSurprinzator >= S))
		{	
			fprintf(g, "Case #%d: %d\n", i + 1, total);
		}
		else
		{
			fprintf(g, "Case #%d: %d\n", i + 1, total);
		}
	}

	fclose(f);
	fclose(g);

	return 0;
}