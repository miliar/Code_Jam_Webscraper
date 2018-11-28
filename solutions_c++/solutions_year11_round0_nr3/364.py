#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

FILE
	*fpi = fopen("C-large.in", "r"),
	*fpo = fopen("C-large.out", "w");

int
	T;

int main(int argc, char *argv[])
{
	fscanf(fpi, "%d", &T);
	for (int i = 0; i < T; i++)
		{
		int
			N,
			nMin = 1000001,
			nCandyValue,
			nSum = 0,
			nXorSum = 0;

		fscanf(fpi, "%d", &N);
		for (int j = 0; j < N; j++)
			{
			fscanf(fpi, "%d", &nCandyValue);

			if (nCandyValue < nMin)
				nMin = nCandyValue;

			nSum += nCandyValue;
			nXorSum ^= nCandyValue;
			}

		if (nXorSum)
			fprintf(fpo, "Case #%d: NO\n", i + 1);
		else
			fprintf(fpo, "Case #%d: %d\n", i + 1, nSum - nMin);
		}

	fclose(fpi);
	fclose(fpo);
	return 0;
}
