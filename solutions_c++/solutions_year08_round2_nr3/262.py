#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int mas[5001];

int main()
{
	FILE *in, *out;
	int i, t, K, N, z, n;
	int cur, ind, dd;
	
	in = fopen("input.txt", "rt");
	out = fopen("output.txt", "wt");

	fscanf(in, "%d", &N);
	for (z = 0; z < N; z++)
	{
		fscanf(in, "%d", &K);

		for (i = 0; i <= K; i++)
			mas[i] = 0;

		cur = 1;
		for (i = 1; i <= K; i++)
		{
			ind = i;
			while (1)
			{
				if (mas[cur] == 0)
				{
					ind--;
					if (ind == 0)
						break;
				}
				cur++;
				if (cur == K+1)
					cur = 1;
			}
			mas[cur] = i;
		}
		
		fscanf(in, "%d", &n);
		fprintf(out, "Case #%d: ", z+1);
		for (i = 0; i < n; i++)
		{
			fscanf(in, "%d", &dd);
			fprintf(out, " %d", mas[dd]);
		}
		fprintf(out, "\n");
		printf("%d", z);
	}

	fclose(in);
	fclose(out);
	return 0;
}