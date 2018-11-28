#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main()
{
	FILE *in, *out;
	int N, M, A, C;
	int x1, x2, x3, y1, y2, y3, z, flag;
		
	in = fopen("input.txt", "rt");
	out = fopen("output.txt", "wt");

	fscanf(in, "%d", &C);
	for (z = 0; z < C; z++)
	{
		fscanf(in, "%d %d %d", &N, &M, &A);
		printf("%d\n", z);	
		flag = 0;
		if (N*M < A)
			goto VAL;
		for (x1 = 0; x1 <= N; x1++)
			for (y1 = 0; y1 <= M; y1++)
				for (x2 = 0; x2 <= N; x2++)
					for (y2 = 0; y2 <= M; y2++)
						for (x3 = 0; x3 <= N; x3++)
							for (y3 = 0; y3 <= M; y3++)
							{
								if (abs (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) == A)
								{
									flag = 1;
									goto VAL;
								}
							}

VAL:
		if (flag == 1)
			fprintf(out, "Case #%d: %d %d %d %d %d %d\n", z+1, x1, y1, x2, y2, x3, y3);
		else
			fprintf(out, "Case #%d: IMPOSSIBLE\n", z+1);
	}

	fclose(in);
	fclose(out);
	return 0;
}