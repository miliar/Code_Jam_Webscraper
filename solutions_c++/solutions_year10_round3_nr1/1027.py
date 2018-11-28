#include <stdio.h>
#include <math.h>



int main(void)
{
	FILE *fp;
	FILE *fpo;
	
	int nT;
	int nN;

	int A[1000];
	int B[1000];

	int i, j, k;
	int nS;

	fp = fopen("A-large.in.txt", "r");
	fpo = fopen("output_inwq_prob1_large.txt", "w");


	fscanf(fp, "%d\a", &nT);

	for (i = 0; i < nT; i++)
	{
		fscanf(fp, "%d\n", &nN);

		for (j = 0; j < nN; j++)
		{
			fscanf(fp, "%d %d\n", &A[j], &B[j]);
		}

		nS = 0;

		for (k = 0; k < nN; k++)
		{
			for (j = 0; j < nN; j++)
			{
				if (k == j)
				{
					continue;
				}

				if ((A[k] > A[j] && B[k] < B[j]) || (A[k] < A[j] && B[k] > B[j]))
				{
					nS = nS + 1;
				}
			}
		}

		fprintf(fpo, "Case #%d: %d\n", i+1, nS/2);
	}

	fclose(fp);
	fclose(fpo);

	return 0;
}



