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

int main ()
{
	FILE* fin, *fout;

	fin = stdin;
	fout = stdout;

	int i = 0, n = 0;
	fscanf (fin, "%d", &n);

	vector <__int64> x, y;

	for (i = 0; i < n; i ++)
	{

		int l = 0, j = 0;
		int u = 0;
		fscanf (fin, "%d", &l);
		x.clear ();
		y.clear ();

		for (j = 0; j < l;j ++)
		{
			fscanf (fin, "%d", &u);
			x.push_back (u);
		}
		for (j = 0; j < l;j ++)
		{
			fscanf (fin, "%d", &u);
			y.push_back (u);
		}

		sort (x.begin (), x.end ());
		sort (y.begin (), y.end ());
		reverse (y.begin (), y.end ());

		__int64 s = 0;

		for (j = 0; j < l; j ++)
			s += x [j] * y [j];

		//fprintf (fout, "Case #%d: %d\n", i + 1, u);
		fprintf (fout, "Case #%d: ", i + 1);
		cout << s <<endl;
	}


	fclose (fin);
	fclose (fout);

	return 0;
}
