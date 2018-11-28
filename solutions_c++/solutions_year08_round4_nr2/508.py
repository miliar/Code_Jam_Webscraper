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

int data [2501] = {0};

int main ()
{
	FILE* fin, *fout;

	fin = stdin;
	fout = stdout;


	int i = 0, n = 0;
	fscanf (fin, "%d", &n);

	for (i = 0; i < n; i ++)
	{
		int h, w, a;
		fscanf (fin, "%d%d%d", &w, &h, &a);
		int j = 0, k = 0;
		memset (data, 0, sizeof (data));
		for (j = 0; j <= h; j ++)
		{
			for (k = 0; k <= w; k ++)
			{
				data [k*j] = j;
				if (k*j == a) break;
			}
			if (k <= w)
			{
				fprintf (fout, "Case #%d: %d %d %d %d %d %d\n", i + 1, 0, 0, k, 0, k, j);
				break;
			}
		}
		if (j <= h) continue;

		data [0] = 0;

		for (j = 0; j + a <= h * w; j ++)
		{
			if (data [j] != 0 && data [j + a] != 0)
			{
				fprintf (fout, "Case #%d: %d %d %d %d %d %d\n", i + 1, 0, 0, (j + a) / data [j + a], data [j], j / data [j], data [j + a]);
				break;
			}
		}
		if (j + a > h * w)
			fprintf (fout, "Case #%d: IMPOSSIBLE\n", i + 1);
	}



	fclose (fin);
	fclose (fout);

	return 0;
}
