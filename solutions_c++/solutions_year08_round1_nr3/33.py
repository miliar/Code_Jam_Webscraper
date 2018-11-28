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

struct cplx5
{
	int re, im;

	cplx5 () {re = im = 0;}
	cplx5 (int i) {re = i; im = 0;}
	cplx5 (int i, int j) {re = i; im = j;}
};

cplx5 operator* (const cplx5& a, const cplx5& b)
{
	cplx5 ret = 0;
	ret.re = a.re * b.re + a.im * b.im * 5;
	ret.re %= 1000;
	ret.im = a.re * b.im + a.im * b.re;
	ret.im %= 1000;

	return ret;
}

cplx5 pow (const cplx5 & a, int n)
{
	cplx5 ret  =1;
	cplx5 sq = a;

	while (n > 0)
	{
		if (n % 2) ret = ret* sq;
		sq =sq* sq;
		n /= 2;
	}

	return ret;
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
		int t = 0;
		fscanf (fin, "%d", &t);
		cplx5 r (3, 1);
		cplx5 p = pow (r, t);
		t = 2*(p.re) - 1;
		t %= 1000;

		fprintf (fout, "Case #%d: ", i + 1);
		if (t < 10) fprintf (fout,"0");
		if (t < 100) fprintf (fout, "0");
		fprintf (fout, "%d\n", t);
	}

	fclose (fin);
	fclose (fout);

	return 0;
}
