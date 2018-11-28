// Using libUtil from libGlov (Graphics Library of Victory) available at http://bigscreensmallgames.com/libGlov
#include "utils.h"
#include "file.h"
#include "strutil.h"
#include "assert.h"
#include "array.h"
#include <string.h>
#include <stdio.h>
#include <stdarg.h>
#include <conio.h>
#include "rand.h"
#include <vector>
using namespace std;

int cmpD(const void *a, const void *b)
{
	const double *d1 = (const double *)a;
	const double *d2 = (const double *)b;
	double dd = *d2 - *d1;
	if (dd<0)
		return -1;
	if (dd>0)
		return 1;
	return 0;
}

char *doC(char **&toks)
{
	static char buf[1024];
	double q[31][4];
	int ns = atoi(*toks++);
	int nq = atoi(*toks++);
	for (int i=0; i<nq; i++)
	{
		for (int j=0; j<4; j++)
		{
			sscanf(*toks++, "%lf", &q[i][j]);
		}
	}
	int p[31] = {0};
	double r[8192];
	int nr=0;
	while (true)
	{
		double v=1.0;
		for (int i=0; i<nq; i++)
		{
			v *= q[i][p[i]];
		}
		p[0]++;
		int i;
		for (i=0; p[i]==4; i++)
		{
			p[i]=0;
			p[i+1]++;
		}
		r[nr++] = v;
		if (i==nq)
			break;
	}
	qsort(r, nr, sizeof(double), cmpD);
	double rr=0;
	for (int i=0; i<ns && i < nr; i++)
	{
		rr += r[i];
	}
	sprintf(buf, "%1.7f", rr);
	return buf;
}
