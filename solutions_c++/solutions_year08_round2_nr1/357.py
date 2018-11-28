#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

struct tree
{
	__int64 x;
	__int64 y;
} mas[100001];

int mCmp(const void *arg1, const void *arg2)
{
	if (((struct tree *)arg1)->x > ((struct tree *)arg2)->x)
		return 1;
	if (((struct tree *)arg1)->x < ((struct tree *)arg2)->x)
		return -1;
	if (((struct tree *)arg1)->y > ((struct tree *)arg2)->y)
		return 1;
	if (((struct tree *)arg1)->y < ((struct tree *)arg2)->y)
		return -1;
	
	return 0;
}

int main()
{
	FILE *in, *out;
	__int64 x, y, n, A, B, C, D, x0, y0, N, M, xc, yc, total;
	int i, j, k, z;
	struct tree tr;

	in = fopen("input.txt", "rt");
	out = fopen("output.txt", "wt");

	fscanf(in, "%I64d", &N);
	for (z = 0; z < N; z++)
	{
		fscanf(in, "%I64d %I64d %I64d %I64d %I64d %I64d %I64d  %I64d", &n, &A, &B, &C, &D, &x0, &y0, &M);
		mas[0].x = x0;
		mas[0].y = y0;
		for (i = 1; i < n; i++)
		{
			mas[i].x = ((A * mas[i-1].x + B) % M);
			mas[i].y = ((C * mas[i-1].y + D) % M);
		}

		qsort(mas, n, sizeof(struct tree), mCmp);

		total = 0;
		for (i = 0; i < n; i++)
			for (j = i+1; j < n; j++)
				for (k = j+1; k < n; k++)
				{
					tr.x = mas[i].x + mas[j].x + mas[k].x;
					tr.y = mas[i].y + mas[j].y + mas[k].y;
					if (tr.x%3 == 0 && tr.y%3 == 0)
					{
						/*tr.x /= 3;
						tr.y /= 3;
						if (bsearch(&tr, mas, n, sizeof(struct tree), mCmp))*/
							total++;		
					}
				}

		fprintf(out, "Case #%d: %I64d\n", z+1, total);
	}

	fclose(in);
	fclose(out);
	return 0;
}