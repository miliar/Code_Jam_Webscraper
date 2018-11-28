#include <stdio.h>
#include <stdlib.h>
#include <string.h>

FILE *fpIn, *fpOut;

int Compute(int R, int k, int N, int *la)
{
	int earn = 0;

	int *la2 = (int *) malloc(N * sizeof(int));
	memcpy(la2, la, N * sizeof(int));

	int *la3 = (int *) malloc(N * sizeof(int));

	for (int _R = 0; _R < R; ++_R) // do R times
	{
		int fill = 0;

		//for (int i = 0; i < N; ++i)
		//	printf("%d ", la2[i]);
		//printf("\n");

		int _n;
		for (_n = 0; _n < N; ++_n)
			if ((fill + la2[_n]) <= k)
				fill += la2[_n];
			else
				break;

		earn += fill;

		//printf("fill=%d, _n=%d\n", fill, _n);
		//system("pause");

		int j = 0;
		for (int i = _n; i < N; ++i)
			la3[j++] = la2[i]; // copy the last section to front

		for (int i = 0; i < _n; ++i)
			la3[j++] = la2[i];

		for (int i = 0; i < N; ++i)
			la2[i] = la3[i];
	}

	return earn;
}

int main()
{
	fpIn = fopen("c:\\gcj\\in_c2", "r");
	fpOut = fopen("c:\\gcj\\out_c2", "w");

	int numOfTestCase;
	fscanf(fpIn, "%d\n", &numOfTestCase);

	for (int caseId = 1; caseId <= numOfTestCase; ++caseId)
	{
		int R, k, N;
		fscanf(fpIn, "%d %d %d\n", &R, &k, &N);

		int *la = (int *) malloc(N * sizeof(int));
		for (int i = 0; i < N; ++i)
			fscanf(fpIn, "%d", &la[i]);

		fprintf(fpOut, "Case #%d: ", caseId);
		int cost = Compute(R, k, N, la);
		fprintf(fpOut, "%d", cost);

		fprintf(fpOut, "\n");
	}

	return 0;
}