#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

FILE
	*fpi = fopen("B-small.in", "r"),
	*fpo = fopen("B-small.out", "w");

int
	T,
	L,
	P,
	C;

int intpow(int b, int e)
{
	int
		res = 1;

	while (e--)
		res *= b;

	return (res);
}

int main(int argc, char *argv[])
{
	fscanf(fpi, "%d", &T);
	for (int i = 0; i < T; i++)
	{
		fscanf(fpi, "%d", &L);
		fscanf(fpi, "%d", &P);
		fscanf(fpi, "%d", &C);

		int
			load = 0;

		while (true)
		{
			if (L * C >= P)
				break;

			int
				X = (int)pow(P * L, 0.5);

			if (pow((double)X, 2) < P * L)
				X++;

			P = X;
			load++;
		}

		fprintf(fpo, "Case #%d: %d\n", i + 1, load);
	}

	fclose(fpi);
	fclose(fpo);
	return 0;
}
