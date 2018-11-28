#include <stdio.h>

#define NMAX 1100

int t, test, n, a[NMAX], b[NMAX];

int main()
{
	FILE *fin, *fout;
	fin = fopen("date.in", "rt");
	fout = fopen("date.out", "wt");
	fscanf(fin, "%d", &t);
	for (test = 1; test <= t; test++)
	{
		fscanf (fin, "%d", &n);
		int i, j, s= 0;
		for (i = 0; i < n; i++)
			fscanf(fin, "%d %d", a+i, b+i);
		for (i = 0; i < n-1; i++)
			for (j = i + 1; j < n; j++)
				if ( (a[i] - a[j]) * (b[i] - b[j]) < 0) s++;
		fprintf(fout, "Case #%d: %d\n", test, s);
	}
		
fclose(fin);
fclose(fout);
return 0;
}
