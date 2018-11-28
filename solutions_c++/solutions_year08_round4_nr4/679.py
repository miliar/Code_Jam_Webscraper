// perm.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <algorithm>
#include <cstdio>
#include <cstring>

char a[1001], b[1001];

int main()
{
	FILE *fin = fopen("smallin.txt", "r");
	FILE *fout = fopen("smallout.txt", "w");

	int t, nt;
	fscanf (fin, "%d\n", &t);
	for (nt = 1; nt <= t; ++nt)
	{
		int k;
		fscanf (fin, "%d\n", &k);
		fgets(a, 1001, fin);
		int v[5], i, l;

		for (i = 0; i < k; ++i) v[i] = i;

		l = strlen(a);
		if (a[l - 1] == '\n') l--;
		int sol = 1<<29;
		do
		{
			for (i = 0; i < l; i++)
			{
				int sg = i - i % k;
				b[i] = a[sg + v[i % k]];
			}

			int ng = 1;
			for (i = 1; i < l; ++i)
				ng += (b[i] != b[i - 1] ? 1 : 0);
			sol = std::min(sol, ng);
		} while (std::next_permutation(v, v + k));

		fprintf (fout, "Case #%d: %d\n", nt, sol);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}

			
		