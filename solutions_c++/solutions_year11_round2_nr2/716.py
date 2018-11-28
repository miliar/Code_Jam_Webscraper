//
//  main.cpp
//  GoJam
//
//  Created by Dina Shvayakova on 11-05-17.
//  Copyright 2011 PPX Services. All rights reserved.
//

#include <assert.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>


struct Vendor	{
	double pos;
	int num;
} static V[200];

static int C;
static double D;


double max(double a, double b)	{
	return a>b ? a:b;
}

bool check(float R)	{
	double prev = -10000000000.0;
	for(int i=0; i<C; ++i)	{
		double first = max(prev, V[i].pos-R);
		double last = first + (V[i].num-1) * D;
		if(last > V[i].pos + R)
			return false;
		prev = last + D;
	}
	return true;
}


int main (int argc, const char * argv[])
{
    int i,T=0;
    FILE *const fi = fopen("input.txt","r");
    FILE *const fo = fopen("output.txt","w");
    fscanf(fi,"%d\n",&T);
    for(i=0; i<T; ++i)  {
		C=0; D=0.0;
		fscanf(fi,"%d%lf",&C,&D);
		int j, total = 0;
		for(j=0; j<C; ++j)	{
			fscanf(fi,"%lf%d", &V[j].pos, &V[j].num);
			total += V[j].num;
		}
		double a = total * D * 0.5, b = 0.0;
		while( fabs(a-b) > 1e-6)	{
			double c = 0.5 * (a+b);
			if(check(c)) a=c;
			else b=c;
		}
		fprintf(fo,"Case #%d: %lf\n", i+1, 0.5*(a+b));
	}
    fclose(fi);
    fclose(fo);
	return 0;
}

