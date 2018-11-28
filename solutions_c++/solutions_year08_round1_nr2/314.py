#include <stdio.h>
#define INF 100000

FILE *fin, *fout;

int n, m;

int likes[2][100][15];

int best[15], bestM = INF;
int v[15], i, j, k, ok[100];


void bkt(int k)
{
	if (k == n)
	{
		for (i = 0; i < m; i++)
			ok[i] = 0;

		for (i = 0; i < m; i++) //any customer
		{
			for (j = 0; j < n; j++) //any flavour
				if (likes [v[j]] [i] [j])
					ok[i] = 1;
		}

		for (i = 0; i < m; i++)
		{
			if (ok[i] == 0)
				return;
		}

		k = 0;
		for (i = 0; i < n; i++)
			k += v[i];

		if (k < bestM)
		{
			bestM = k;
			for (i = 0; i < n; i++)
				best[i] = v[i];
		}
	}
	else
	{
		v[k] = 0;
		bkt(k+1);
		v[k] = 1;
		bkt(k+1);
	}
}

int main()
{
	int T, ind, type;
	fin = fopen("date.in", "rt");
	fout = fopen("date.out", "wt");

	fscanf(fin, "%d", &T);

	for (int test = 1; test <= T; test++)
	{
		printf("test = %d\n", test);
		fscanf(fin, "%d %d", &n, &m);

		for (i = 0; i < 100; i++)
		{
			for (j = 0; j < 15; j++)
				likes[0][i][j] = likes[1][i][j] = 0;
		}

		for (i = 0; i < m; i++)
		{
			fscanf(fin, "%d", &k);
			for (j = 0; j < k; j++)
			{
				fscanf(fin, "%d %d", &ind, &type);

				likes[type][i][ind-1] = 1;
			}
		}

		bestM = INF;
		bkt(0);

		fprintf(fout, "Case #%d: ", test);

		if (bestM == INF)
			fprintf(fout, "IMPOSSIBLE\n");
		else
		{
			for (i = 0; i < n; i++)
				fprintf(fout, "%d ", best[i]);
			
			fprintf(fout, "\n");
		}
	}

	fclose(fin);
	fclose(fout);
	return 0;
}
