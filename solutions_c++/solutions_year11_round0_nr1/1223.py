#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <memory.h>

#define PARA_N 101 

int OneStep(int xB, int xO, int cL, int cB, int cO, int &xB1, int &xO1);
int sign(int x);


int main(void)
{
	FILE *fpr;
	FILE *fpw;

	int caseNum;
	int n;
	int List[PARA_N];
	int BList[PARA_N];
	int OList[PARA_N];
	char color;
	int pos;

	int i, j;
	int k, kO, kB;
	int xB, xO;
	int step;

	fpr = fopen("A-large.in", "r");
	if (!fpr) 
	{
		printf("fail to open the input file!\n");
		return 0;
	}

	fpw = fopen("A-large.out", "w");
	if (!fpw)
	{
		printf("fail to open the output file!\n");
		return 0;
	}
	
	fscanf(fpr, "%d", &caseNum);

	for (i=0; i<caseNum; i++)
	{
		fscanf(fpr, "%d ", &n);
		k=0;
		kO=0;
		kB=0;
		memset(List, 0, PARA_N*sizeof(int));
		memset(BList, 0, PARA_N*sizeof(int));
		memset(OList, 0, PARA_N*sizeof(int));

		for (j=0; j<n; j++)
		{
			fscanf(fpr, "%c", &color);
			fscanf(fpr, "%d ", &pos);
			if (color == 'O') 
			{
				List[k] = pos;
				OList[kO] = pos;
				k++;
				kO++;
			}
			else
			{
				List[k] = -pos;
				BList[kB] = -pos;
				k++;
				kB++;
			}
		}

		k=0;
		kB=0;
		kO=0;
		step=0;
		xB = -1;
		xO = 1;
		while(List[k]!=0)
		{
			step = step + OneStep(xB, xO, List[k], BList[kB], OList[kO], xB, xO);
			if (List[k]>0) kO++;
			else kB++;
			k++;
		}

		fprintf(fpw, "Case #%d: %d\n", i+1, step);
	}

	fclose(fpr);
	fclose(fpw);
	return 0;
}

int OneStep(int xB, int xO, int cL, int cB, int cO, int &xB1, int &xO1)
{
	int stepB=0;
	int stepO=0;
	int step=0;

	if (cB == 0) stepB = 0;
	else stepB = int(fabs(cB-xB));

	if (cO == 0) stepO = 0;
	else stepO = int(fabs(cO-xO));

	if (cL > 0)
	{
		stepO = stepO+1;
		xO1 = cL;

		if (stepO >= stepB) xB1 = cB;
		else xB1 = sign(cB-xB)*stepO+xB;

		step = stepO;
	}
	else
	{
		stepB = stepB+1;
		xB1 = cL;

		if (stepB >= stepO) xO1 = cO;
		else xO1 = sign(cO-xO)*stepB+xO;

		step = stepB;
	}

	return step;
}

int sign(int x)
{
	if (x>0) return 1;
	else if (x<0) return -1;
	else return 0;
}