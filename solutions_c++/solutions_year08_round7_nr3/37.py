#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int dec(const void *a, const void *b)
{
	double aa = *(double *)a;
	double bb = *(double *)b;

	if (bb < aa) return -1;
	else if (bb > aa) return 1;

	return 0;
}

int dec2(const void *a, const void*b)
{
	int POS=1;
	double *aa = (double *)a;
	double *bb = (double *)b;

	for(int i=0; i<4; i++)
	{
		if (*aa > *bb) return POS;
		if (*aa < *bb) return -POS;
	}

	return 0;
}

int main()
{
	int i,N,M,Q,j;
	double d[30][4];

	scanf("%d", &N);

	for (int cs=1; cs<=N; cs++)
	{
		scanf("%d %d", &M, &Q);

		for (i=0;i<Q;i++)
			scanf("%lf %lf %lf %lf", d[i], d[i]+1, d[i]+2, d[i]+3);

		for (i=0;i<Q;i++)
			qsort(d[i], 4, sizeof(double), dec);

		qsort(d, Q, sizeof(double)*4, dec2);

		/*
		for (i=0;i<Q;i++)
			printf("%lf %lf %lf %lf\n", d[i][0], d[i][1], d[i][2], d[i][3]);
		*/
		
		double prob[16*16*16];
		double tmp_prob=0.0;
		int ttl = pow(4,Q);
		for (i=0;i<ttl;i++)
		{
			// break i up into base Q
			int t=i;
			tmp_prob = 1.0;
			for(j=Q-1;j>=0;j--)
			{
				tmp_prob *= d[j][t%4];
				t/=4;
			}
			
			prob[i] = tmp_prob;
			//printf("%d %lf %lf\n", i, tmp_prob, prob);
		}

		qsort(prob, ttl, sizeof(double), dec);
		
		double p = 0.0;
		for (i=0;i<M && i<ttl;i++)
			p += prob[i];

		if (p > 1.0) p = 1.0;
		printf("Case #%d: %lf\n", cs, p);
	}

	return 0;
}
