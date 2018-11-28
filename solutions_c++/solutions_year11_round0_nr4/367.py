#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

FILE
	*fpi = fopen("D-large.in", "r"),
	*fpo = fopen("D-large.out", "w");

int
	T;

int main(int argc, char *argv[])
{
	fscanf(fpi, "%d", &T);
	for (int i = 0; i < T; i++)
		{
		int
			N,
			nVal,
			nCorrect = 0;

		fscanf(fpi, "%d", &N);
		for (int j = 1; j <= N; j++)
			{
			fscanf(fpi, "%d", &nVal);

			if (nVal == j)
				nCorrect++;
			}

		fprintf(fpo, "Case #%d: %f\n", i + 1, (float)N - nCorrect);
		}

	fclose(fpi);
	fclose(fpo);
	return 0;
}
