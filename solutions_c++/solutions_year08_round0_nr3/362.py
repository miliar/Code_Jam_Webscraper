// GCJ08c.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <math.h>

using namespace std;

double Prob;

typedef unsigned long UL;
double f,R,t,r,g;
double sizep;

void SimulateCirc()
{
	if(g<=2*f)
	{
		Prob=1.0;
		return;
	}
	//double numstr=(R-t)/(2*r+g);
	//UL numsim=numstr*1000000;
	double sizep=R/10000000;//R/numsim;

	double sizeg=min(sizep,(g-2*f)/1000000);
	double sizer=min(sizep,(2*(r+f))/1000000);

	double h=R-t-f;

	double hit=0;
	double nonhit=0;
	//go line-by-line
	double i=0;
	while(i<h)
	{

		
		double nexti=min(i+r+f,h);
		for(;i<nexti;i+=sizer)
		{
			double k=sqrt(R*R-i*i);
			hit+=k*sizer;
		}

		nexti=min(i+g-f-f,h);
		for(;i<nexti;i+=sizeg)
		{
			double k=sqrt(R*R-i*i);
			double p=sqrt(h*h-i*i);
			double j=0;
			while(j<p)
			{
				double nextj=min(j+r+f,p);
				double add=nextj-j;
				hit+=add*sizeg;
				j=nextj;
				nextj=min(j+g-f-f,p);
				add=nextj-j;
				nonhit+=add*sizeg;
				j=nextj;
				nextj=min(j+r+f,p);
				add=nextj-j;
				hit+=add*sizeg;
				j=nextj;
			}
			hit+=(k-p)*sizeg;
		}

		nexti=min(i+r+f,h);
		for(;i<nexti;i+=sizer)
		{
			double k=sqrt(R*R-i*i);
			hit+=k*sizer;
		}
	}
	for(;i<R;i+=sizer)
	{
		double k=sqrt(R*R-i*i);
		hit+=k*sizer;
	}
	Prob=hit/(nonhit+hit);
}

int _tmain(int argc, char* argv[])
{
	int N;
	cin>>N;
	for(int i=1;i<=N;++i)
	{
		Prob=0;
		cin>>f>>R>>t>>r>>g;
		SimulateCirc();
		printf("Case #%d: %.6lf\n", i,Prob); 
	}

	return 0;
}

