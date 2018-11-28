// Using libUtil from libGlov (Graphics Library of Victory) available at http://bigscreensmallgames.com/libGlov
#include "utils.h"
#include "file.h"
#include "strutil.h"
#include "MathUtil.h"
#include "assert.h"
#include "array.h"
#include <string.h>
#include <stdio.h>
#include <stdarg.h>
#include <conio.h>
#include "rand.h"
#include <vector>
using namespace std;

static int n;
static int ships[1001][4];
static double x, y, z;

static void score(int &worsti, double &worstv)
{
	double secondworstv;
	int secondworsti=-1;
	for (int i=0; i<n; i++) {
		double d = ABS(ships[i][0] - x) + ABS(ships[i][1] - y) + ABS(ships[i][2] - z);
		d /= ships[i][3];
		if (i==0 || d > worstv)
		{
			secondworstv = worstv;
			secondworsti = worsti;
			worsti = i;
			worstv = d;
		} else if (i==1 || d > secondworstv)
		{
			secondworstv = d;
			secondworsti = i;
		}
	}
}

double doit()
{
	double worstv;
	int worsti=-1;

	score(worsti, worstv);
	double x0=x, y0=y, z0=z;
	double x1=ships[worsti][0];
	double y1=ships[worsti][1];
	double z1=ships[worsti][2];
	double p0=0;
	double p1=1;
	double v0 = worstv;
	x = x1; y=y1; z=z1;
	double v1;
	score(worsti, v1);
	double r=v0;
#if 0
	for (int i=0; i<100; i++) {
		double m0 = (p0 + p1)/3;
		double m1 = (p0 + p1)/3*2;
		x = x0 + (x1-x0)*m0;
		y = y0 + (y1-y0)*m0;
		z = z0 + (z1-z0)*m0;
		double vm0;
		score(worsti, vm0);
		x = x0 + (x1-x0)*m1;
		y = y0 + (y1-y0)*m1;
		z = z0 + (z1-z0)*m1;
		double vm1;
		score(worsti, vm1);
		if (vm0 < vm1) {
			p1 = m1;
			v1 = vm1;
			r = vm0;
		} else {
			p0 = m0;
			v0 = vm0;
			r = vm1;
		}
	}
#else
	p0=0; p1=1;
	for (int i=0; i<100; i++) {
		double m0 = (p0 + p1)/3;
		double m1 = (p0 + p1)/3*2;
		x = x0 + (x1-x0)*m0;
		//y = y0 + (y1-y0)*m0;
		//z = z0 + (z1-z0)*m0;
		double vm0;
		score(worsti, vm0);
		x = x0 + (x1-x0)*m1;
		//y = y0 + (y1-y0)*m1;
		//z = z0 + (z1-z0)*m1;
		double vm1;
		score(worsti, vm1);
		if (vm0 < vm1) {
			p1 = m1;
			v1 = vm1;
			r = vm0;
		} else {
			p0 = m0;
			v0 = vm0;
			r = vm1;
		}
	}
	p0=0; p1=1;
	for (int i=0; i<100; i++) {
		double m0 = (p0 + p1)/3;
		double m1 = (p0 + p1)/3*2;
		//x = x0 + (x1-x0)*m0;
		y = y0 + (y1-y0)*m0;
		//z = z0 + (z1-z0)*m0;
		double vm0;
		score(worsti, vm0);
		//x = x0 + (x1-x0)*m1;
		y = y0 + (y1-y0)*m1;
		//z = z0 + (z1-z0)*m1;
		double vm1;
		score(worsti, vm1);
		if (vm0 < vm1) {
			p1 = m1;
			v1 = vm1;
			r = vm0;
		} else {
			p0 = m0;
			v0 = vm0;
			r = vm1;
		}
	}
	p0=0; p1=1;
	for (int i=0; i<100; i++) {
		double m0 = (p0 + p1)/3;
		double m1 = (p0 + p1)/3*2;
		//x = x0 + (x1-x0)*m0;
		//y = y0 + (y1-y0)*m0;
		z = z0 + (z1-z0)*m0;
		double vm0;
		score(worsti, vm0);
		//x = x0 + (x1-x0)*m1;
		//y = y0 + (y1-y0)*m1;
		z = z0 + (z1-z0)*m1;
		double vm1;
		score(worsti, vm1);
		if (vm0 < vm1) {
			p1 = m1;
			v1 = vm1;
			r = vm0;
		} else {
			p0 = m0;
			v0 = vm0;
			r = vm1;
		}
	}
#endif
	return r;
}

char *doC(char **&toks)
{
	n = atoi(*toks++);
	for (int i=0; i<n; i++) {
		for (int j=0; j<4; j++) {
			ships[i][j] = atoi(*toks++);
		}
	}
	x=y=z=0;
	for (int i=0; i<n; i++) {
		x+=ships[i][0];
		y+=ships[i][1];
		z+=ships[i][2];
	}
	x/=(double)n;
	y/=(double)n;
	z/=(double)n;
	double r;
	for (int i=0; i<1000; i++) {
		r = doit();
		//printf("  %1.7f", r);

	}
	//printf("\n");
	static char buf[1024];
	sprintf(buf, "%1.7f", r);
	return buf;
}
