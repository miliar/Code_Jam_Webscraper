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
	int Sean[PARA_N];
	int xor, min, sum;

	int i, j;

	fpr = fopen("C-large.in", "r");
	if (!fpr) 
	{
		printf("fail to open the input file!\n");
		return 0;
	}

	fpw = fopen("C-large.out", "w");
	if (!fpw)
	{
		printf("fail to open the output file!\n");
		return 0;
	}
	
	fscanf(fpr, "%d", &caseNum);

	for (i=0; i<caseNum; i++)
	{
		memset(List, 0, PARA_N*sizeof(int));
		memset(Sean, 0, PARA_N*sizeof(int));

		fscanf(fpr, "%d", &n);

		xor = 0;
		min = 1000001;
		sum = 0;

		for (j=0; j<n; j++)
		{
			fscanf(fpr, "%d", &List[j]);
			if (List[j] < min) min = List[j];
			xor = xor^List[j];
			sum = sum+List[j];
		}
	
		if (xor != 0)
			fprintf(fpw, "Case #%d: NO\n", i+1);
		else
			fprintf(fpw, "Case #%d: %d\n", i+1, sum-min);
	}

	fclose(fpr);
	fclose(fpw);
	return 0;
}
