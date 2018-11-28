#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <fstream>
using namespace std;
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define pi 2*acos(0.0)
#define mp make_pair
//#define x first
//#define y second
#define sqr(a) (a)*(a)
#define pii pair<int,int>
#define pdd pair<double,double>
#define sz(c) (int)((c).size())
#define inf 1000000000
#define all(c) (c).begin(), (c).end()
#define vi vector<int>
#define vpii vector< pii >
#define vpdd vector< pdd >
#define L(s) (int)((s).end()-(s).begin())
#define ll long long
#define C(a,b) memset((a),(b),sizeof((a)))
inline double D(double px,double py)
{
	return (sqrt(sqr(px)+sqr(py)));
}
inline double s3(double px,double py,double qx,double qy)
{
	return (fabs(px*qy-qx*py)/2.0);
}
inline double s2(double px,double py,double qx,double qy,double r)
{
	double a1=atan2(py,px);
	double a2=atan2(qy,qx);
	return ((r*r)*fabs(a1-a2)/2.0);
}
inline double sd(double px,double py,double qx,double qy,double rx,double ry,double r)
{
	double d1=s2(qx,qy,rx,ry,r);
	double d2=s3(px,py,qx,qy);
	double d3=s3(px,py,rx,ry);
	return (d1-d2-d3);
}
double g,R,r,t,f,S,x,y,px,py,qx,qy,r1x,r1y,r2x,r2y,r3x,r3y,r4x,r4y;
int n,i,j;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>n;
	for(int cnt=0;cnt<n;cnt++)
	{
		cin>>f>>R>>t>>r>>g;
		S=0;
		for(x=r;x<R-t;x+=g+2*r)
			for(y=r;y<R-t;y+=g+2*r)
				if (g<2*f)
					continue;
				else
				{
					px=x+f;
					py=y+f;
					qx=x+g-f;
					qy=y+g-f;
					if (D(px,py)>=R-t-f);
					else
					if (D(qx,qy)<=R-t-f)
						S+=(px-qx)*(py-qy);
					else
					if (D(px,qy)>=R-t-f&&D(qx,py)>=R-t-f)
					{
						r1x=px;
						r1y=sqrt(sqr(R-t-f)-sqr(r1x));
						r2y=py;
						r2x=sqrt(sqr(R-t-f)-sqr(r2y));
						S+=sd(px,py,r1x,r1y,r2x,r2y,R-t-f);
					}
					else
					if (D(px,qy)>=R-t-f&&D(qx,py)<=R-t-f)
					{
						r1x=px;
						r1y=sqrt(sqr(R-t-f)-sqr(r1x));
						r2y=py;
						r2x=sqrt(sqr(R-t-f)-sqr(r2y));
						r3x=qx;
						r3y=sqrt(sqr(R-t-f)-sqr(r3x));
						S+=sd(px,py,r1x,r1y,r2x,r2y,R-t-f)-sd(qx,py,r2x,r2y,r3x,r3y,R-t-f);
					}
					else
					if (D(px,qy)<=R-t-f&&D(qx,py)>=R-t-f)
					{
						r1x=px;
						r1y=sqrt(sqr(R-t-f)-sqr(r1x));
						r2y=py;
						r2x=sqrt(sqr(R-t-f)-sqr(r2y));
						r3y=qy;
						r3x=sqrt(sqr(R-t-f)-sqr(r3y));
						S+=sd(px,py,r1x,r1y,r2x,r2y,R-t-f)-sd(px,qy,r1x,r1y,r3x,r3y,R-t-f);
					}
					else
					if (D(px,qy)<=R-t-f&&D(qx,py)<=R-t-f)
					{
						r1x=px;
						r1y=sqrt(sqr(R-t-f)-sqr(r1x));
						r2y=py;
						r2x=sqrt(sqr(R-t-f)-sqr(r2y));
						r3y=qy;
						r3x=sqrt(sqr(R-t-f)-sqr(r3y));
						r4x=qx;
						r4y=sqrt(sqr(R-t-f)-sqr(r4x));
						S+=sd(px,py,r1x,r1y,r2x,r2y,R-t-f)-sd(px,qy,r1x,r1y,r3x,r3y,R-t-f)-sd(qx,py,r2x,r2y,r4x,r4y,R-t-f);
					}
				}
				S=((pi*R*R)/4.0-S)/(pi*R*R/4.0);
				printf("Case #%d: %0.8f\n",cnt+1,S);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}