#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
const long double maxnum=1e30;
const long double limit=1e-8;
int n;
long double sx,sy,sz,vx,vy,vz;
double ans,st;
void init()
{
	cin >>n;
	sx=sy=sz=vx=vy=vz=0;
	long double x,y,z,dx,dy,dz;
	for (int i=0;i<n;i++)
	{
		cin >>x>>y>>z>>dx>>dy>>dz;
		sx+=x;
		sy+=y;
		sz+=z;
		vx+=dx;
		vy+=dy;
		vz+=dz;
	}
	sx/=n;
	sy/=n;
	sz/=n;
	vx/=n;
	vy/=n;
	vz/=n;
}
long double sqr(long double x)
{
	return x*x;
}
long double Count(long double t)
{
	long double x=sx+vx*t,y=sy+vy*t,z=sz+vz*t;
	return sqrt(sqr(x)+sqr(y)+sqr(z));
}
void solve()
{
	long double l=0,r=maxnum,m1,m2,d1,d2;
	while (r-l>limit)
	{
		m1=l+(r-l)/3;
		m2=r-(r-l)/3;
		d1=Count(m1);
		d2=Count(m2);
		if (d1>d2)
			l=m1;
		else
			r=m2;
	}
	st=(l+r)/2;
	ans=Count(st);	
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int t;
	cin >>t;
	for (int i=1;i<=t;i++)
	{
		init();
		solve();
		printf("Case #%d: %.8lf %.8lf\n",i,ans,st);
	}
	return 0;
}
