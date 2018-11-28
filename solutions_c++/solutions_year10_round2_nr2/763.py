#include <stdio.h>
#include <math.h>



int main(void)
{
	FILE *fp;
	FILE *fpo;
	
	int nC;
	int nN;
	int nK;
	int nB;
	int nT;
	int x[50];
	int v[50];
	double t[50];
	int npK;
	int nnK;

	int i, j;
	int nS;

	fp = fopen("B-large.in.txt", "r");
	fpo = fopen("output_inwq_prob2_large.out.txt", "w");


	fscanf(fp, "%d\a", &nC);

	for (i = 0; i < nC; i++)
	{
		fscanf(fp, "%d %d %d %d\n", &nN, &nK, &nB, &nT);
		nS = 0;
		npK = 0;
		for (j = 0; j < nN; j++)
		{
			fscanf(fp, "%d", &x[j]);
		}
		for (j = 0; j < nN; j++)
		{
			fscanf(fp, "%d", &v[j]);
		}

		for (j = 0; j < nN; j++)
		{
			t[j] = double(nB-x[j]) / double(v[j]);
		}

		j = nN - 1;
		nnK = 0;

		while(j>=0)
		{
			if (t[j] <= nT)
			{
				nnK = nnK + 1;
				nS = nS + npK;	
			}
			else
			{
				npK = npK + 1;
			}

			if (nnK >= nK)
			{
				break;
			}
			j--;
		}

		if (nnK >= nK)
		{
			fprintf(fpo, "Case #%d: %d\n", i+1, nS);
		}
		else
		{
			fprintf(fpo, "Case #%d: IMPOSSIBLE\n", i+1);
		}
	}

	fclose(fp);
	fclose(fpo);

	return 0;
}



