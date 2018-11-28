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
	int A[101][101];
	double WP[101];
	double OWP[101];
	double OOWP[101];
	char ch;
	int B[101];
	int W[101];

	double owps, oowps;
	double RPI[101];


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
		fscanf(fpr, "%d", &N);
		fscanf(fpr, "%c", &ch);
		memset((void*)A, N*N, sizeof(int));
		memset((void*)B, N, sizeof(int));
		memset((void*)W, N, sizeof(int));
		for (j=0; j<N; j++)
		{
			B[j] = 0;
			W[j] = 0;
			for (k=0; k<N+1; k++)
			{
				fscanf(fpr, "%c", &ch);
				if (ch == '0') 
				{
					A[j][k] = 0;
					B[j] = B[j] + 1;
				}
				else if (ch == '1')
				{
					A[j][k] = 1;
					B[j] = B[j] + 1;
					W[j] = W[j] + 1;
				}
				else if (ch == '.')
				{
					A[j][k] = -1;
				}
				else
					break;
			}
			if (B[j] == 0)
				WP[j] = 0;
			else
				WP[j] = W[j]*1.0/B[j];
		}

		for (j=0; j<N; j++)
		{
			owps = 0;
			for (k=0; k<N; k++)
			{
				if (A[j][k] >= 0)
				{
					if (B[k] > 1)
						owps = owps + (W[k]-A[k][j])*1.0/(B[k]-1);
				}
			}
			if (B[j] == 0)
				OWP[j] = 0;
			else
				OWP[j] = owps / B[j];
		}

		for (j=0; j<N; j++)
		{
			oowps = 0;
			for (k=0; k<N; k++)
			{
				if (A[j][k] >= 0)
				{
					oowps = oowps + OWP[k];
				}
			}
			if (B[j] == 0)
				OOWP[j] = 0;
			else
				OOWP[j] = oowps / B[j];
		}


		for (j=0; j<N; j++)
		{
			RPI[j] = 0.25*WP[j] + 0.50*OWP[j] + 0.25*OOWP[j];
		}

		fprintf(fpw, "Case #%d:\n", i+1);
		for (j=0; j<N; j++)
			fprintf(fpw, "%.12lf\n", RPI[j]);
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