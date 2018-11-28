#include<iostream>
#include<string>
#include<sstream>
#include<map>
#include<cmath>
using namespace std;
#define oo 1e100
#define eps 1e-15
#define MAXN 70
#define ZERO(x) ( fabs((x))<eps )

struct POINT
{
	double x,y,z,vx,vy,vz;
	POINT()
	{
		x=y=z=vx=vy=vz=0;
	}
}cen;


int N;

double cal_dist ( double t )
{
	double x=cen.x+cen.vx*t,y=cen.y+cen.vy*t,z=cen.z+cen.vz*t;
	return sqrt(x*x+y*y+z*z);
}

POINT make_center ( )
{
	int i;
	POINT a;
	double x,y,z,vx,vy,vz;
	for ( i=0 ; i<N ; i++ )
	{
		scanf("%lf%lf%lf%lf%lf%lf",&x,&y,&z,&vx,&vy,&vz);
		a.x+=x;
		a.y+=y;
		a.z+=z;
		a.vx+=vx;
		a.vy+=vy;
		a.vz+=vz;
	}
	a.x/=N;
	a.y/=N;
	a.z/=N;
	a.vx/=N;
	a.vy/=N;
	a.vz/=N;
	return a;
}

int cmp ( double t )
{
	if ( t<-eps )
		return -1;
	if ( t>eps )
		return 1;
	return 0;
}

double ts ( )
{
	int i;
	double l=0,r=oo,mid1,mid2,t1,t2;
	while ( r-l>eps )
	{
		mid1=l+1.0/3.0*(r-l);
		mid2=l+2.0/3.0*(r-l);
		t1=cal_dist(mid1);
		t2=cal_dist(mid2);
		if ( cmp(t1-t2)>0 )
		{
			l=mid1;
		}
		else
			if ( cmp(t1-t2)<0 )
			{
				r=mid2;
			}
			else
			{
				l=mid1;
				r=mid2;
			}
	}
	return r;
}
int main ( )
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas,n,i,k;
	double dis,ti;
	scanf("%d",&cas);
	for ( k=1 ; k<=cas; k++ )
	{
		scanf("%d",&N);
		cen=make_center();
		if ( ZERO(cen.vx) && ZERO(cen.vy) && ZERO(cen.vz) )
		{
			ti=0;
			dis=cal_dist(0);
		}
		else
		{
			ti=ts();
			dis=cal_dist(ti);
		}
		printf("Case #%d: %.10lf %.10lf\n",k,dis,ti);
	}
}