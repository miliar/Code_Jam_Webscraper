#include <stdio.h>
#include <math.h>

__int64 prob2(int ng[1000], int nN, int nk, int nR);

int main(void)
{
	FILE *fp;
	FILE *fpo;
	
	int nT;
	int nN;
	int nk;
	int nR;
	int ng[1000];
	__int64 rt;

	int i,j;

	fp = fopen("C-small-attempt0.in.txt", "r");
	fpo = fopen("output_inwq_prob2_small.out.txt", "w");


	fscanf(fp, "%d\a", &nT);

	for (i = 0; i < nT; i++)
	{
		printf("%d\n",i);
		fscanf(fp, "%d %d %d\n", &nR, &nk, &nN);
		for (j = 0; j < nN; j++)
		{
			fscanf(fp, "%d ", &ng[j]);
		}
		rt = prob2(ng, nN, nk, nR);
		fprintf(fpo, "Case #%d: %lld\n", i+1, rt);
	}

	fclose(fp);
	fclose(fpo);

	return 0;
}

__int64 prob2(int ng[1000], int nN, int nk, int nR)
{
	__int64 result = 0;
	__int64 ri[1001];
	int rik[1001];
	int i, j;
	int k = 0;
	__int64 unitk = 0;
	ri[0] = 0;
	int rk;
	__int64 valv;
	__int64 round;
	int n;

	for (i=1; i<1001; i++)
	{
		for (j=1; j<i; j++)
		{
			if (k == rik[j])
			{
				unitk = ri[i-1] - ri[j-1];
				rk = i-j;
				break;
			}
		}
		rik[i] = k;
		ri[i] = ri[i-1];
		valv = ri[i-1]+nk;
		n = 0;
		while (ri[i] <= valv && n <= nN)
		{
			ri[i] = ri[i] + ng[k];
			k = (k+1)%nN;
			n++;
		}
		k = (k+nN-1)%nN;
		ri[i] = ri[i] - ng[k];
	}

	round = __int64(((nR-j+1)/rk));

	if (round > 0)
	{
		result = round*unitk + ri[(nR-j+1)%rk+j-1];
	}
	else
	{
		result = ri[nR];
	}

	return result;
}
