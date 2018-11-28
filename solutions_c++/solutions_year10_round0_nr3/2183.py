#include <stdio.h>
#include <stdlib.h>

double theme(double r, double k, int n, double g[]);

int main(void)
{
	int t, n, i, j;
	double r, k;
	double *g;
	scanf("%d\n", &t);
	for(i = 1; i <= t; i++)
	{
		scanf("%lf %lf %d\n", &r, &k, &n);
		g = (double *) malloc(n * sizeof(double));
		for(j = 0; j < n; j++)
		{
			scanf("%lf ", &g[j]);
		}
		scanf("\n");
		printf("Case #%d: %.0f\n", i, theme(r,k,n,g));
	}
	return 0;
}

double theme(double r, double k, int n, double g[])
{
	double i, j;
	int pos = 0;
	int count = 0;
	double riders;
	double euro = 0.0;
	for(i = 0; i < r; i++)
	{
		riders = 0.0;
		while(count < n)
		{
			riders += g[pos];			
			if(riders > k)
			{
				riders -= g[pos];
				break;
			}
			pos++;
			pos %= n;
			count++;
		}
		euro += riders;
		count = 0;
	}
	return euro;
}

