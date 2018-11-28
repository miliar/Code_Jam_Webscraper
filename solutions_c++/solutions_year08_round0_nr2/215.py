#include <stdio.h>
#include <stdlib.h>
#define NMax 505

struct time
{
	int h, m;
};

struct train
{
	time s, f;
};

FILE *fin, *fout;
train a[NMax], b[NMax];
time aready[NMax], bready[NMax];


int na, nb, n, t;
int asolved[NMax], bsolved[NMax];

train ax, bx;
int difTime(time x, time y)
{	return (y.h - x.h) * 60 + y.m - x.m; }

int comp_f(const void *aa, const void *bb)
{
	ax = *(train*)aa;
	bx = *(train*)bb;
	return (-difTime(ax.f, bx.f));
}
int comp_s(const void *aa, const void *bb)
{
	ax = *(train*)aa;
	bx = *(train*)bb;
	return (-difTime(ax.s, bx.s));
}
time adMin(time x, int min)
{
	x.m += min;
	return x;
}

int main()
{
	int i, j;

	fin = fopen("input.txt", "rt");
	fout = fopen("output.txt", "wt");

	fscanf(fin, "%d", &n);

	for (int test = 1; test <= n; test++)
	{
		fscanf(fin, "%d\n%d %d\n", &t, &na, &nb);

		for (i = 0; i < na; i++)
			fscanf(fin, "%d:%d %d:%d\n", &a[i].s.h, &a[i].s.m, &a[i].f.h, &a[i].f.m);

		for (i = 0; i < nb; i++)
			fscanf(fin, "%d:%d %d:%d\n", &b[i].s.h, &b[i].s.m, &b[i].f.h, &b[i].f.m);

		qsort(a, na, sizeof(a[0]), comp_f);
		qsort(b, nb, sizeof(b[0]), comp_f);

		for (i = 0; i < nb; i++)
			aready[i] = adMin(b[i].f, t);
		for (i = 0; i < na; i++)
			bready[i] = adMin(a[i].f, t);

		qsort(a, na, sizeof(a[0]), comp_s);
		qsort(b, nb, sizeof(b[0]), comp_s);

		for (i = 0; i < na || i < nb; i++)
			asolved[i] = bsolved[i] = 0;
		
		j = 0;
		for (i = 0; i < na && j < nb; i++)
		{
			if (difTime(a[i].s, aready[j]) <= 0)
			{
				asolved[i] = 1;
				j++;
			}
		}

		j = 0;
		for (i = 0; i < na; i++)
		{
			if (!asolved[i])
				j++;
		}
		fprintf(fout, "Case #%d: %d ", test, j);

		
		j = 0;
		for (i = 0; i < nb && j < na; i++)
		{
			if (difTime(b[i].s, bready[j]) <= 0)
			{
				bsolved[i] = 1;
				j++;
			}
		}

		

		j = 0;
		for (i = 0; i < nb; i++)
		{
			if (!bsolved[i])
				j++;
		}
		fprintf(fout, "%d\n", j);

		
	}

	return 0;
}
