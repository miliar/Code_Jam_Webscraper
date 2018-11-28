#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <memory.h>
#include <iostream.h>

#define PARA_N 101 

int main(void)
{
	FILE *fpr;
	FILE *fpw;

	int caseNum;
	int N=0;
	int i,j,k;
	char A[51][51];
	int nR, nC;
	char ch;
	bool flag;

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
		fscanf(fpr, "%d", &nR);
		fscanf(fpr, "%d", &nC);
		fscanf(fpr, "%c", &ch);
		memset((void*)A, 51*51, sizeof(char));
		flag = true;

		for (j=0; j<nR; j++)
		{
			for (k=0; k<nC; k++)
			{
				fscanf(fpr, "%c", &ch);
				A[j][k] = ch;
			}
			fscanf(fpr, "%c", &ch);
		}

		for (j=0; j<nR; j++)
		{
			for (k=0; k<nC; k++)
			{
				if (A[j][k] == '#')
				{
					if ((A[j][k+1] == '#') &&(A[j+1][k] == '#') && (A[j+1][k+1] == '#') && (k+1 < nC) && (j+1 < nR))
					{
						A[j][k] = '/';
						A[j][k+1] = '\\';
						A[j+1][k] = '\\';
						A[j+1][k+1] = '/';
					}
					else
					{
						flag = false;
						break;
					}
				}
			}
			if (flag == false)
			{
				break;
			}
		}

		fprintf(fpw, "Case #%d:\n", i+1);
		if (flag)
		{
			for (j=0; j<nR; j++)
			{
				for (k=0; k<nC; k++)
				{
					fprintf(fpw, "%c", A[j][k]);
				}
				fprintf(fpw, "\n");
			}
		}
		else
		{
			fprintf(fpw, "Impossible\n");
		}
	}


	fclose(fpr);
 	fclose(fpw);
	return 0;
}

int sign(int x)
{
	if (x>0) return 1;
	else if (x<0) return -1;
	else return 0;
}