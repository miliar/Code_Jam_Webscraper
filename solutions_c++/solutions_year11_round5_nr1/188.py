#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
const double PI=3.141592653589793,EPS=1e-9,INF=1e100;
struct vect
{
	double x,y;
	vect(double a=0.0,double b=0.0):x(a),y(b) {}
	vect operator+(vect a)
	{
		return vect(x+a.x,y+a.y);
	}
	vect operator-(vect a)
	{
		return vect(x-a.x,y-a.y);
	}
	double operator*(vect a) //Dot Product
	{
		return x*a.x+y*a.y;
	}
	double operator/(vect a) //Cross Product
	{
		return x*a.y-y*a.x;
	}
	vect operator*(double a)
	{
		return vect(x*a,y*a);
	}
	vect operator/(double a)
	{
		return vect(x/a,y/a);
	}
	vect operator-()
	{
		return vect(-x,-y);
	}
	bool operator<(vect a) const
	{
		return y+EPS<a.y||(y-EPS<a.y&&x+EPS<a.x);
	}
	bool operator==(vect a) const
	{
		return fabs(x-a.x)<EPS&&fabs(y-a.y)<EPS;
	}
	bool operator!=(vect a) const
	{
		return fabs(x-a.x)>EPS||fabs(y-a.y)>EPS;
	}
	double length()
	{
		return sqrt(x*x+y*y);
	}
	bool iszero()
	{
		return fabs(x)<EPS&&fabs(y)<EPS;
	}
	vect rotate(double a)
	{
		double c=cos(a),s=sin(a);
		return vect(x*c-y*s,x*s+y*c);
	}
	vect unit()
	{
	    return *this/length();
	}
};
double radian(vect a,vect b) //[0,PI*2)
{
	double r=atan2(a/b,a*b);
	return r<-EPS?r+PI*2:r;
}
int dbcmp(double a,double b)
{
	return b-a>EPS?-1:a-b>EPS;
}
bool dbzero(double a)
{
	return fabs(a)<EPS;
}
double angle(double a,double b)
{
	double c=b-a;
	while(c<0.0) c+=PI*2.0;
	return c;
}
//Solve p+u*s=q+v*t
//Return value: -1=same line,0=no intersection,1=ok
int ll_intersect(vect &p,vect &q,vect &u,vect &v,double &s,double &t)
{
	double d=v.x*u.y-u.x*v.y;
	double d1=v.x*(q.y-p.y)-v.y*(q.x-p.x),d2=u.x*(q.y-p.y)-u.y*(q.x-p.x);
	if(fabs(d)<EPS)
	{
		if(fabs(d1)<EPS)
		{
			s=t=0.0;
			if(fabs(u.x)>EPS) s=(q.x-p.x)/u.x;
			else if(fabs(u.y)>EPS) s=(q.y-p.y)/u.y;
			else if(fabs(v.x)>EPS) t=(p.x-q.x)/v.x;
			else if(fabs(v.y)>EPS) t=(p.y-q.y)/v.y;
			else return 0;
			return (fabs(u.x)<EPS&&fabs(u.y)<EPS)||(fabs(v.x)<EPS&&fabs(v.y))<EPS?1:-1;
		}
		return 0;
	}
	s=d1/d;
	t=d2/d;
	return 1;
}
double area(vector<vect> &low,vector<vect> &up)
{
	//for(int i=0;i<(int)low.size();i++) printf("low: %lf,%lf\n",low[i].x,low[i].y);
	//for(int i=0;i<(int)up.size();i++) printf("up: %lf,%lf\n",up[i].x,up[i].y);
	double ret=low.front()/up.front()+up.back()/low.back();
	for(int i=1;i<(int)low.size();i++)
	{
		ret+=low[i]/low[i-1];
	}
	for(int i=1;i<(int)up.size();i++)
	{
		ret+=up[i-1]/up[i];
	}
	return fabs(ret)*0.5;
}
double cut(vector<vect> &low,vector<vect> &up,double x)
{
	//printf("cut %lf:\n",x);
	vector<vect> tlow,tup;
	for(int i=0;i<(int)low.size();i++)
	{
		if(low[i].x<x+EPS)
		{
			tlow.push_back(low[i]);
		}
		else
		{
			tlow.push_back(vect(x,(low[i].y-low[i-1].y)/(low[i].x-low[i-1].x)*(x-low[i-1].x)+low[i-1].y));
			break;
		}
	}
	for(int i=0;i<(int)up.size();i++)
	{
		if(up[i].x<x+EPS)
		{
			tup.push_back(up[i]);
		}
		else
		{
			tup.push_back(vect(x,(up[i].y-up[i-1].y)/(up[i].x-up[i-1].x)*(x-up[i-1].x)+up[i-1].y));
			break;
		}
	}
	return area(tlow,tup);
}
void solve()
{
	double w;
	int L,U,G;
	scanf("%lf%d%d%d",&w,&L,&U,&G);
	vector<vect> low(L),up(U);
	for(int i=0;i<L;i++)
	{
		scanf("%lf%lf",&low[i].x,&low[i].y);
	}
	for(int i=0;i<U;i++)
	{
		scanf("%lf%lf",&up[i].x,&up[i].y);
	}
	double all=area(low,up);
	//printf("all=%lf\n",all);
	//printf("cut %lf %lf\n",cut(low,up,5.0),cut(low,up,10.0));
	//return;
	for(int i=1;i<G;i++)
	{
		//printf("i=%d\n",i);
		double a=0.0,b=w;
		while(b-a>1e-9)
		{
			double x=(a+b)*0.5;
			double z=cut(low,up,x);
			//printf("cut %lf: %lf %lf\n",x,z);
			if(z<all*(double)i/(double)G) a=x; else b=x;
		}
		printf("%.9lf\n",a);
	}
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int cs=1;cs<=t;cs++)
	{
		printf("Case #%d:\n",cs);
		solve();
	}
}
