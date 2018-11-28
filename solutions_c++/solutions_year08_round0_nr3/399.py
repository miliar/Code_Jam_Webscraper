#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <list>
#include <map>
#include <set>
using namespace std;
#define all(a) (a).begin(),(a).end()
#define mset(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define sz(a) a.size()
#define rep(i,n) for(i=0; i<n; i++)
#define forr(i,a,b) for(i=a; i<=b; i++)
#define ford(i,a,b) for(i=a; i>=b; i--)
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define X first
#define Y second
#define eps 1e-14
typedef long long ll;
typedef vector<int> VI;
const double pi=2*acos(0);

FILE* fi; FILE* fo;
int i,j, u,n;
double f,R,t,t2,r,g, s,s0, xa,ya, xb,yb, xo,yo;

double sq(double x, double y)
{	if(x*x+y*y>=t*t) return 0;
	yo=sqrt(t2-x*x); xo=sqrt(t2-y*y);
	return (t2*acos((xo*x+yo*y)/t2)-x*(yo-y)-y*(xo-x))/2; }

int main()
{
	fi=fopen("c-small.in","r"); //large
	fo=fopen("c-small.res","w");
	fscanf(fi,"%d",&n);
	rep(u,n)
	{
		fscanf(fi,"%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
		g-=2*f; r+=f; 
		t=R-t-f; t2=t*t;
		s=0;
		if(t<=eps || g<=eps) { fprintf(fo,"Case #%d: 1.000000\n",u+1); continue; }
		xa=r;
		while(xa*xa+r*r<=t2)
		{
			ya=r; xb=xa+g;
			while(xa*xa+ya*ya<=t2)
			{
				yb=ya+g;
				if(xb*xb+yb*yb<=t2) s+=g*g;
				else
				{
					s+=(sq(xa,ya)-sq(xa,yb)-sq(xb,ya));
				}
				ya=yb+2*r;
			}
			xa=xb+2*r;
		}
		s0=pi*R*R;
		fprintf(fo,"Case #%d: %.6lf\n",u+1,(s0-4*s)/s0);
	}
	fclose(fi); fclose(fo);
//	getchar();
	return 0;
}
