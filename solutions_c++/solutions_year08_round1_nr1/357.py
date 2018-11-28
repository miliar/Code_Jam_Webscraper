#include <stdio.h>
#define NMax 1000
#define INF 1000000000

FILE *fin, *fout;

int v1[NMax], v2[NMax], n;
int p1[NMax], p2[NMax];
int profit[2 * NMax];


int v[NMax], uz[NMax];
int best = INF;
int one, i;

void bkt(int k)
{
	if (k == n)
	{
		//end

		one = 0;
		for (i = 0; i < n; i++)
			one += v1[i] * v2[v[i]];

		if (one < best)
			best = one;
	}
	else
	{
		for (v[k] = 0; v[k] < n; v[k]++)
		{
			if (!uz[v[k]])
			{
				uz[v[k]] = 1;
				bkt(k+1);
				uz[v[k]] = 0;
			}
		}
	}
}

int main()
{
	int T, test, i, j, gets_better = 1;
	fin = fopen("date.in", "rt");
	fout = fopen("date.out", "wt");

	fscanf(fin, "%d", &T);

	for (test = 1; test <= T; test++)
	{		
		fscanf(fin, "%d", &n);
		for (i = 0; i < n; i++)
			fscanf(fin, "%d", &v1[i]);
		for (i = 0; i < n; i++)
			fscanf(fin, "%d", &v2[i]);


		for (i = 0; i < n; i++)
			uz[i] = 0;

		best = INF;
		bkt(0);

		fprintf(fout, "Case #%d: %d\n", test, best);
	}

		/*for (i = 0; i < n; i++)
		{
			p1[i] = i;
			p2[i] = i;
		}

		while (gets_better)
		{
			for (i = 0; i < 2*n; i++)
			{
				profit[i] = -INF;
				pr[i] = -1;
			}

			for (i = 0; i < n; i++)
				make_profit(i, 0);

			maxi = n;
			for (i = n; i < 2*n; i++)
			{
				if (profit[i] > profit[maxi])				
					maxi = i;
			}

			if (profit[maxi] > 0)
				rebuilt(maxi);

		}*/

	fclose(fin);
	fclose(fout);
	return 0;
}
