#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#define REP(i,u) for(int i=0;i<u;i++)
#define FOR(i,z,u) for(int i=(z);i<=(u);i++)
#define FORO(i,z,u,p) for(int i=(z);i<=(u);i=i+(p))
#define PI 3.14159265358979323846
#define SQ(aa) ((aa)*(aa))
#define EPS 10e-20
#define eps EPS
using namespace std;

int N;
double res,ff,R,t,r,g,inR,wStr,side;
double Sall;
bool zved;

double oo;
inline double f(double x)
{
	if(x+EPS>inR) return 0.0;
	double ret=sqrt(SQ(inR)-SQ(x))-oo;
	if(ret+EPS<0) return 0.0;
	if(ret-EPS>g) return g;
	return ret;
}


inline double simpson(double a,double b)
{
	return (abs(b-a)/6.0)*(f(a)+4.0*f((a+b)/2.0)+f(b));
}

double simpson(double a,double b,double o)
{
	oo=o;
	double ret=0.,krok=(b-a)/1000000.,od=a,pom;
	while(od+EPS+krok<b)
	{
		pom=simpson(od,od+krok);
		if(pom<EPS) break;
		ret+=pom;
		od+=krok;
	}
	return ret;	 
}

int main() 
{
	cin>>N;
	REP(p,N)
	{
		res=0.;
		cin>>ff>>R>>t>>r>>g;
		Sall=PI*SQ(R);
		wStr=2*r+2*ff;
		inR=R-t-ff;
		g=g-2*ff;

		if(inR+EPS<0.0 || g+EPS<0.0) 
		{
			printf("Case #%d: 1.000000\n",p+1);
			continue;
		}

		double pos=(g+wStr),pr=0.;
    for(double x=wStr/2;x+EPS<inR;x+=pos)
			for(double y=wStr/2;y+EPS<inR;y+=pos)
			{
				if(sqrt(SQ(x+g)+SQ(y+g))+EPS<inR)
					pr+=SQ(g);
				else
					pr+=simpson(y,y+g,x);
			}

		pr*=4;
		printf("Case #%d: %.6lf\n",p+1,1.0-pr/Sall);
	}
	return 0;
}
