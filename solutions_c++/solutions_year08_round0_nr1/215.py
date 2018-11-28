#include <stdio.h>
#include <string.h>

#define SMax 105
#define QMax 1005
#define LMax 1005
#define INF 1000000000

int n, q, s;
char engines[SMax][LMax];
char querys[QMax][LMax];

int c1[SMax], c2[SMax];

FILE *fin, *fout;

int main()
{
	int test, i, j, k;

	fin = fopen("input.txt", "rt");
	fout = fopen("output.txt", "wt");

	fscanf(fin, "%d", &n);

	for (test = 1; test <= n; test++)
	{
		fscanf(fin, "%d\n", &s);
		for (i = 0; i < s; i++)
			fgets(engines[i], LMax, fin);
		fscanf(fin, "%d\n", &q);
		for (i = 0; i < q; i++)
			fgets(querys[i], LMax, fin);		

		for (i = 0; i < s; i++)
		{
			if (!strcmp(querys[0], engines[i]))
				c1[i] = INF;
			else
				c1[i] = 0;
			
			c2[i] = INF;
		}

		for (i = 1; i < q; i++) // first i queryes
		{
			//from c1 to c2

			for (j = 0; j < s; j++)
				c2[j] = INF;

			for (j = 0; j < s; j++) // using last search j
			{
				if (!strcmp(engines[j], querys[i]))
				{
					//change needed
					for (k = 0; k < s; k++)
					{
						if (k != j && c2[k] > c1[j] + 1)
							c2[k] = c1[j] + 1;
					}							
				}
				else
				{
					//no change
					if (c2[j] > c1[j])
						c2[j] = c1[j];
				}
			}
			
			for (j = 0; j < s; j++)
				c1[j] = c2[j];
		}


		k = INF;
		for (i = 0; i < s; i++)
		{
			if (k > c1[i])
				k = c1[i];
		}

		fprintf(fout, "Case #%d: %d\n", test, k);
	}

	return 0;
}

