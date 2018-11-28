// program.cpp : Defines the entry point for the console application.
//

// BEGIN CUT HERE
#pragma warning(disable:4786)
#include <stdafx.h>
// END CUT HERE
#include <string>
#include <map>
#include <set>
#include <vector>
#include <deque>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <numeric>
using namespace std;


double calcareatmp(double xx,double yy,double r)
{
	if(yy>r) return 0.0;
	if(xx>r) xx=r;
	double tx=sqrt(r*r-yy*yy);
	double ans;
	if(xx<tx)
	{
		double py=sqrt(r*r-xx*xx);
		double sita=asin(xx/r);
		ans=sita*r*r/2.0+xx*py/2.0-xx*yy;
	}
	else
	{
		double sita=acos(yy/r);
		ans=sita*r*r/2.0-tx*yy/2.0;
	}
	return ans;
}

double calcarea(double xs,double xe,double ys,double r)
{
	return calcareatmp(xe,ys,r)-calcareatmp(xs,ys,r);
}

void process(int num)
{
	double f,R,t,r,g;

	cerr<<num<<endl;
	cin>>f>>R>>t>>r>>g;

	if(g<2.0*f||R-t<f)
	{
		cout<<"Case #"<<num<<": "<<1.0<<endl;
		return;
	}

	double ww=r+f,gg=g-2.0*f,rr=R-t-f;
	double area=calcarea(0,ww,0,rr);
	for(double xs=ww+gg;xs<=rr;xs+=2.0*ww+gg) area+=calcarea(xs,xs+2.0*ww,0,rr);
	

	for(double ys=ww;ys<=rr;ys+=2.0*ww+gg) area+=calcarea(0,ww,ys,rr)-calcarea(0,ww,ys+gg,rr);
	for(double xs=ww+gg;xs<=rr;xs+=2.0*ww+gg)
		for(double ys=ww;ys<=rr;ys+=2.0*ww+gg)
		{
			double ta=calcarea(xs,xs+2.0*ww,ys+gg,rr);
			double tb=calcarea(xs,xs+2.0*ww,ys,rr);
			area+=tb-ta;
			if(tb<1e-9) break;
		}
	
	double ans=1.0-(acos(-1.0)*rr*rr-area*4.0)/(acos(-1.0)*R*R);
	cout<<"Case #"<<num<<": "<<ans<<endl;
}

int main(void)
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++) process(i);
	return 0;
}