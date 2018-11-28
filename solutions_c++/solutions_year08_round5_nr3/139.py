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

int h, w;

char cl [20][20] = {{0}};

int best [20][1024] = {{0}};

bool adm (int mask)
{
	int i = 0;
	for (i = 0; i < w - 1; i ++)
		if (((mask & (1 << i)) != 0) && ((mask & (1 << (i+ 1))) != 0))
			return false;

	return true;
}

bool nobr (int mask, int row)
{
	int i = 0;
	for (i = 0; i < w; i ++)
		if (((mask & (1 << i)) != 0) && (cl [row][i] == 'x'))
			return false;

	return true;
}

bool adm2 (int back, int front)
{
	int i = 0;
	for (i = 0; i < w - 1; i ++)
		if (((back & (1 << i)) != 0) && ((front & (1 << (i+ 1))) != 0))
			return false;
	for (i = 0; i < w - 1; i ++)
		if (((front & (1 << i)) != 0) && ((back & (1 << (i+ 1))) != 0))
			return false;

	return true;
}

int bitcnt (int mask)
{
	int i = 0, ans = 0;
	for (i = 0; i < w; i ++)
		if ((mask & (1 << i)) != 0)
			ans ++;
	return ans;
}

int main ()
{
	FILE* fin, *fout;

	fin = stdin;
	fout = stdout;

	int i = 0, n = 0;
	fscanf (fin, "%d", &n);

	for (i = 0; i < n; i ++)
	{
		fscanf (fin, "%d%d", &h, &w);
		int j = 0, k = 0, l = 0;

		for (j = 0; j < h; j ++)
			fscanf (fin, "%s", cl [j]);

		memset (best, 0, sizeof (best));

		for (j = 0; j < (1 << w); j ++)
		{
			if (adm (j) && nobr (j, 0)) best [0][j] = bitcnt (j);
		}

		for (j = 1; j < h; j ++)
		{
			for (k = 0; k < (1 << w); k ++)
			{
				if (!adm (k)) continue;
				if (!nobr (k, j)) continue;
				int ms = 0;
				for (l = 0; l < (1 << w); l ++)
				{
					if (adm2 (l, k) && ms < best [j - 1][l])
						ms = best [j - 1][l];
				}
				best [j][k] = ms + bitcnt (k);
			}
		}

		int ans = 0;

		for (j = 0; j < (1 << w); j ++)
		{
			if (ans < best [h - 1][j])
				ans = best [h - 1][j];
		}


		fprintf (fout, "Case #%d: %d\n", i + 1, ans);
	}

	fclose (fin);
	fclose (fout);

	return 0;
}
