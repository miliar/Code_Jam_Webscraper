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
#include <complex>

using namespace std;

typedef complex <double> cd;

void solve (cd z1, cd z2, cd x1, cd x2, cd& a, cd& b)
{
	cd D = z1 - z2;
	cd d1 = x1 - x2;
	cd d2 = z1 * x2 - z2 * x1;

	a = d1 / D;
	b = d2 / D;
}

double ccabs (cd c)
{
	return sqrt (c.real () * c.real () + c.imag () * c.imag ());
}

bool try_find (vector <cd> z, vector <cd> x, cd& a, cd& b, int i1, int i2)
{
	cd z1 = z [0];
	cd z2 = z [1];

	cd x1 = x [i1];
	cd x2 = x [i2];

	solve (z1, z2, x1, x2, a, b);

	if (ccabs (a * z [2] + b - x [3 - i1 - i2]) < 1e-9) return true;
	return false;
}

cd ONE (1, 0);

void find_trans (vector <cd> z, vector <cd> x, cd& aa, cd& bb)
{
	cd mina, minb;

	double maxabs = 0;

	int i1 ,i2;

	for (i1 = 0; i1 < 3; i1 ++)
	{
		for (i2 = 0; i2 < 3; i2 ++)
		{
			if (i2 == i1) continue;
			cd a (0, 0), b (0, 0);
			if (try_find (z, x, a, b, i1, i2))
			{
				double d = ccabs (ONE - a);
				if (d > maxabs)
				{
					mina = a;
					minb = b;
					maxabs = d;
				}
			}
		}
	}

	aa = mina;
	bb = minb;
}

int main ()
{
	FILE* fin, *fout;

	fin = stdin;
	fout = stdout;

	int i = 0, n = 0;
	fscanf (fin, "%d", &n);
	//n = 1;

	for (i = 0; i < n; i ++)
	{
		int x = 0, y = 0;
		int j = 0;

		vector <cd> z, xx;

		for (j = 0; j < 3; j ++)
		{
			fscanf (fin, "%d%d", &x, &y);
			z.push_back (cd (x, y));
		}

		for (j = 0; j < 3; j ++)
		{
			fscanf (fin, "%d%d", &x, &y);
			xx.push_back (cd (x, y));
		}


		cd a (0, 0), b (0, 0);

		find_trans (z, xx, a, b);

		cd c = ONE - a;

		if (sqrt (c.real () * c.real () + c.imag () * c.imag ()) > 1e-8)
		{
			cd ans = b / c;
			
			fprintf (fout, "Case #%d: %lf %lf\n", i + 1, ans.real (), ans.imag ());
		}
		else
		{
			fprintf (fout, "Case #%d: No solution\n", i + 1, a.real (), a.imag (), b.real (), b.imag ());

		}

	}

	fclose (fin);
	fclose (fout);

	return 0;
}
