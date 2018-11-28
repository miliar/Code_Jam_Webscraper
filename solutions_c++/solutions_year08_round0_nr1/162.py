#define _USE_MATH_DEFINES

#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

char s [200] = {0};
vector <string> searchers;
int best [1100][110] = {{0}};

int bins_ (string val, int beg, int end)
{
	if (end - beg <= 1)
	{
		if (searchers [beg] == val) return beg;
		else return -1;
	}
	int m = (beg + end) / 2;
	if (searchers [m] <= val) return bins_ (val, m, end);
	else return bins_ (val, beg, m);
}

int bins (string val)
{
	return bins_ (val, 0, searchers.size ());
}

int main ()
{
	FILE* fin, *fout;

	fin = stdin;
	fout = stdout;

	int i= 0, n = 0;

	fscanf (fin, "%d", &n);

	for (i = 0; i < n; i ++)
	{
		int ns = 0, nq = 0;
		int j = 0, k = 0;

		fscanf (fin, "%d\n", &ns);

		searchers.clear ();

		for (j = 0; j < ns; j ++)
		{
			fgets (s, 190, fin);
			string s1 (s);
			searchers.push_back (s1);
		}

		sort (searchers.begin (), searchers.end ());

		fscanf (fin, "%d\n", &nq);
		
		for (j = 0; j < ns; j ++)
		{
			best [0][j] = 0;
			for (k = 1; k <= nq; k ++)
				best [k][j] = 1000000;
		}

		for (j = 1; j <= nq; j ++)
		{
			fgets (s, 190, fin);
			string query (s);

			int bad_idx = bins (query);

			int min_val = 1000000;

			for (k = 0; k < ns; k ++)
			{
				if (min_val > best [j - 1][k]) min_val = best [j - 1][k];
			}

			for (k = 0; k < ns; k++)
			{
				if (k == bad_idx) continue;
				best [j][k] = min (min_val + 1, best [j - 1][k]);
			}
		}

		int ans  = 1000000;
		for (j  =0; j < ns; j ++)
			if (best [nq][j] < ans) ans = best [nq][j];

		fprintf (fout, "Case #%d: %d\n", i + 1, ans);

	}

	fclose (fin);
	fclose (fout);

	return 0;
}
