#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
#define   max(a,b)    ((a)>(b)?(a):(b))
#define   min(a,b)    ((a)<(b)?(a):(b))
#define   sqr(a)         ((a)*(a))
#define   rep(i,a,b)  for(i=(a);i<(b);i++)
#define   REP(i,n)     rep(i,0,n)
#define   inf         1000000000
#define   pi       3.14159265358979
FILE *fin;
FILE *fout;
int N;
double f,R,t,r,g;
typedef   struct Pot 
{
	double x;
	double y;
	Pot & operator==(Pot a)
	{
		x=a.x;
		y=a.y;
		return *this;
	}
}Pot;
double mydistance(Pot a,Pot b)
{
	return sqrt(sqr(a.x-b.x)+sqr(a.y-b.y));
}
double cross(Pot va,Pot vb)
{
	return va.x*vb.x+va.y*vb.y;
}
double xmul(Pot va,Pot vb)
{
	return va.x*vb.y-vb.x*va.y;
}
double gets4(Pot xs,Pot xx)
{
	Pot zero;
	zero.x=0;
	zero.y=0;
	double cosa=fabs(cross(xs,xx)/(mydistance(xs,zero)*mydistance(xx,zero)));
	double a=acos(cosa);
	double s1=a*(R-t-f)*(R-t-f)/2;
	double s2=fabs(xmul(xs,xx))/2;
	return  s1-s2;
}
double getarea(Pot lx,Pot rx,Pot ls,Pot xs,Pot xx)
{
    double  S=0;
    double s1=0;
	double sa1=xs.x-lx.x;
	double sb1=xs.y-lx.y;
	s1=sa1*sb1;
	double s2=0;
	double sa2=xx.x-xs.x;
	double sb2=xx.y-lx.y;
	s2=sa2*sb2;
	double s3=0;
	double sa3=xx.x-xs.x;
	double sb3=xs.y-xx.y;
	s3=sa3*sb3/2;
	double s4=0;
    s4=gets4(xs,xx);
 
	S=s1+s2+s3+s4;
	return S;
}
int main()
{
   	fin=fopen("C-small-attempt0.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
    fscanf(fin,"%d\n",&N);
    int round=1;
	for (round=1;round<=N;round++)
	{
       fscanf(fin,"%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
	   if (2*f>=g||f+t>=R)
	   {
		   printf("Case #%d: %lf\n",round,1.0);
		   fprintf(fout,"Case #%d: %lf\n",round,1.0);
		   continue;
	   }
	   Pot bg;
	   bg.x=r;
	   bg.y=r;
	   double aqbound=sqr(R-t)-sqr(r);
	   double qbbbd=sqr(R-t);
	   double Sc=0;
	   double TS=pi*R*R/4;
	   for (double x=bg.x;sqr(x)<aqbound;x+=(2*r+g))
	   {
		   for (double y=bg.y;sqr(y)<aqbound;y+=(2*r+g))
		   {
                if (x*x+y*y<qbbbd)
                {
					Pot low;
					low.x=x;
					low.y=y;
					Pot high;
					high.x=x+g;
					high.y=y+g;
					if (high.x*high.x+high.y*high.y<=qbbbd)
					{
                         double rr=g-2*f;
						 Sc+=rr*rr;
					}
					else 
					{
                        Pot lx=low;
						lx.x+=f;
                        lx.y+=f;
						double iqbbbd=sqr(R-t-f);
						if (lx.x*lx.x+lx.y*lx.y>=iqbbbd)
						{
							continue;
						}
						Pot rx;
						rx.y=lx.y;
						double bdxx=sqrt(iqbbbd-rx.y*rx.y);
						rx.x=min(lx.x+g-2*f,bdxx);
						Pot ls;
						ls.x=lx.x;
						double bdyy=sqrt(iqbbbd-ls.x*ls.x);
						ls.y=min(lx.y+g-2*f,bdyy);
						Pot xs;
						xs.y=ls.y;
						xs.x=sqrt(iqbbbd-xs.y*xs.y);
						Pot xx;
						xx.x=rx.x;
						xx.y=sqrt(iqbbbd-xx.x*xx.x);
						 Sc+=getarea(lx,rx,ls,xs,xx);
					}
                }
		   }
	   }
//	   printf("SC is %lf   TS is  %lf \n",Sc,TS);
	   printf("Case #%d: %.6lf\n",round,1.0-(Sc/TS));
	   fprintf(fout,"Case #%d: %.6lf\n",round,1.0-(Sc/TS));
	}
}