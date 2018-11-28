#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <memory.h>

#define PARA_N 1001

int main(void)
{
	FILE *fpr;
	FILE *fpw;

	int caseNum;
	int n;
	int List[PARA_N];
	int Sort[PARA_N];
	int t;
	int i, j, k;

	fpr = fopen("D-large.in", "r");
	if (!fpr) 
	{
		printf("fail to open the input file!\n");
		return 0;
	}

	fpw = fopen("D-large.out", "w");
	if (!fpw)
	{
		printf("fail to open the output file!\n");
		return 0;
	}
	
	fscanf(fpr, "%d\n", &caseNum);

	for (i=0; i<caseNum; i++)
	{
		memset(List, 0, PARA_N*sizeof(int));

		fscanf(fpr, "%d\n", &n);

		if (n>0) 
		{
			for (j=0; j<n; j++)
			{
				fscanf(fpr, "%d ", &List[j]);
				Sort[j] = List[j];
			}
		}

		for (j=0; j<n; j++)
		{
			for (k=j+1; k<n; k++)
			{
				if (Sort[k] < Sort[j])
				{
					t = Sort[k];
					Sort[k] = Sort[j];
					Sort[j] = t;
				}
			}
		}

		k = 0;
		for (j=0; j<n; j++)
		{
			if (List[j] != Sort[j]) k++;
		}

		fprintf(fpw, "Case #%d: %.6f\n", i+1, k*1.0);
	}

	fclose(fpr);
	fclose(fpw);
	return 0;
}
