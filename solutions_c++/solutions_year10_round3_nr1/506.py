#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

FILE
	*fpi = fopen("A-large.in", "r"),
	*fpo = fopen("A-large.out", "w");

int
	T,
	N,
	A[1000],
	B[1000];

int main(int argc, char *argv[])
{
	fscanf(fpi, "%d", &T);
	for (int i = 0; i < T; i++)
	{
		fscanf(fpi, "%d", &N);
		for (int j = 0; j < N; j++)
		{
			fscanf(fpi, "%d", &A[j]);
			fscanf(fpi, "%d", &B[j]);
		}

		int
			intersect = 0;

		for (int j = 0; j < N - 1; j++)
			for (int k = j + 1; k < N; k++)
				if ((A[k] > A[j] && B[k] < B[j]) || (A[k] < A[j] && B[k] > B[j]))
					intersect++;

		fprintf(fpo, "Case #%d: %d\n", i + 1, intersect);
	}

	fclose(fpi);
	fclose(fpo);
	return 0;
}
