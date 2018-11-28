#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<int(b);++i)
#define SZ(v) ((int)v.size())
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define ALL(v) (v).begin(),(v).end()
#define SS stringstream
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define SQR(x) (x)*(x)

#define EPS 1e-9

#define PI 3.14159265358979323846

double SQRT_2=sqrt(2.0);

double count(double x,double r)
{
	return 0.5*(x*sqrt(r*r-x*x) +r*r*asin(x/r));
}

double solve(double a,double b,double r,double d)
{
	if(a>r||b>r||d>r)
		return 0;
		
	return (count(b,r)-count(a,r))-d*(b-a);
}

struct point
{
	double x,y;
};

double abso(point A)
{
	return sqrt(SQR(A.x)+SQR(A.y));
}

bool isIn(point A,double r)
{
	return abso(A)<=r+EPS;
}

bool isOut(point A,double r)
{
	return abso(A)>r-EPS;
}


int main()
{
freopen ("C-large.in","r",stdin);
freopen ("out.txt","w",stdout);
	int N;
	cin>>N;
	double f,R,t,r,g,innerR,ans,S,d,Rogr,sina,sqside,x,y;
	point A,B,C,D;

	FOR(kk,0,N)
	{
		cin>>f>>R>>t>>r>>g;
		ans=1.0;
		S=0;
		innerR=R-t;
		sqside=2*r+g;
		
		Rogr=innerR-f;
		if(g<=2*f+EPS)
			goto L;

		D.x=r+f;
		D.y=r+f;

		A.x=D.x;
		A.y=D.y+g-2*f;

		B.y=A.y;
		B.x=A.x+g-2*f;

		C.x=B.x;
		C.y=D.y;


		for(;D.x<Rogr+EPS;D.x+=sqside)
		{
			for(D.y=r+f;isIn(D,Rogr);D.y+=sqside)
			{
				A.x=D.x;
				A.y=D.y+g-2*f;

				B.y=A.y;
				B.x=A.x+g-2*f;

				C.x=B.x;
				C.y=D.y;


				if(isIn(B,Rogr))
					S+=SQR(g-2*f);
				else
					if(isOut(A,Rogr)&&isIn(C,Rogr))
						S+=solve(D.x,C.x,Rogr,D.y);
					else
						if(isIn(A,Rogr)&&isOut(C,Rogr))
							S+=solve(D.y,A.y,Rogr,D.x);
							else
							if(isOut(A,Rogr)&&isOut(C,Rogr))
							{
								x=sqrt(SQR(Rogr)-SQR(D.y));
								S+=solve(D.x,x,Rogr,D.y);
							}
							else
								if(isIn(A,Rogr)&&isIn(C,Rogr))
								{
									x=sqrt(SQR(Rogr)-SQR(A.y));
									S+=solve(x,C.x,Rogr,D.y);
									S+=(A.y-D.y)*(x-D.x);
								}
													
			}
			D.y=r+f;
		}

		ans-=(S/((PI/4.0)*R*R));
	
L:		cout<<"Case #"<<kk+1<<": ";
		printf("%.6f\n",ans);
	}
	return 0;
}

