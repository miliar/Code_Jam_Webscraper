#include<stdio.h>

long n, k;
int t;

	int main()
	{
		FILE *in = fopen("input.in", "r");
		FILE *out = fopen("bigA.out", "w");
		fscanf(in, "%d", &t);
		for (int numTest = 1; numTest <= t; numTest++)
		{
			fscanf(in, "%ld %ld", &n, &k);
			long s = 1 << n;
			if ((k + 1) % s == 0)
				fprintf (out, "Case #%d: ON\n", numTest);
			else
				fprintf (out, "Case #%d: OFF\n", numTest);
		}
		fclose(out);

		return 0;
	}