// code.cpp : Defines the entry point for the console application.
//
#define _CRT_SECURE_NO_WARNINGS 1
#include "stdafx.h"

#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>

#define MAX(A,B) (A>B ? A : B)

using namespace std;


#define MAXC 200

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fi,*fo;
	int ttt,ti;

	long c,d,i;

	int ok;
	long p[MAXC],v[MAXC];

	long double l,r,m;
	long double last,first,lastinit;


	fi=fopen("Bs.in","r");
	fo=fopen("B.out","w");

	fscanf(fi,"%d",&ttt);
	for (ti=0;ti<ttt;ti++)
	{
		fscanf(fi,"%ld%ld",&c,&d);
		for (i=0;i<c;i++) fscanf(fi,"%ld%ld",&p[i],&v[i]);
		l=0;
		r=1000;
		r*=r; r*=r; r*=r;
		lastinit=-r;

		m=(l+r)/2;
		while (r-l>0.0000000001)
		{
			ok=1;
			last=lastinit;
			for (i=0;i<c;i++)
			{
				first=MAX(p[i]-m,last+d);
				last=first+d*(v[i]-1);
				if (last>p[i]+m) { ok=0; break; }
			}

			if (ok) r=m;
			else l=m;
			m=(l+r)/2;
		}

		fprintf(fo,"Case #%d: %lf\n",ti+1,l);


	}
	fclose(fi);
	fclose(fo);
	return 0;
}

