#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <sstream>
#include <iostream>
#include <queue>
#include <cassert>
#include <cmath>

#define mp make_pair
#define sz(v)((int)((v).size()))
#define all(v) v.begin(),v.end()
#define pb push_back

using namespace std;

typedef pair<int,int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T x){return x>0 ? x:(-x);}
template<class T> T sqr(T x){return x*x;}

const double pi=3.1415926535897932384626433832795;
const int maxn=1100;
const double eps=1E-9;


struct point{
	double x,y;
	point(){}
	point(double x,double y):x(x),y(y){}
	point operator-(point p)
	{
		return point(x-p.x,y-p.y);
	}
	double operator*(point p)
	{
		return x*p.y-y*p.x;
	}
	double len()
	{
		return sqrt(sqr(x)+sqr(y));
	}
};

point sp[maxn];/*This is stack*/
int h;

point gp;

bool cmp(point p,point q)
{
	if((p-gp).len()<eps)
	{
		if((q-gp).len()<eps)
			return false;
		return true;
	}
	if((q-gp).len()<eps)
		return false;
	return (p-gp)*(q-gp)<-eps;
}

vector<point> ConvexHull(vector<point> v)
{
	h=0;
	double xx=v[0].x,yy=v[0].y;	
	for(int i=0;i<sz(v);i++){
		if(v[i].x<xx-eps || (abs(v[i].x-xx)<eps && v[i].y<yy-eps))
			xx=v[i].x,yy=v[i].y;
	}
	gp=point(xx,yy);
	sort(v.begin(),v.end(),&cmp);
	return v;
}

double f,R,t,r,g;

bool inside(double x,double y)
{
	return x*x+y*y<R*R+eps;
}

double Angle(point p,point q)
{
	double sn=(p*q)/(p.len()*q.len());
	return abs(asin(sn));
}

bool between(double a,double b,double c)
{
	if(a>b) swap(a,b);
	return c>a-eps && c<b+eps;
}

void Crosser(point p,point q,vector<point>& res)
{
	bool fl=false;
	if(abs(p.x-q.x)>eps)
	{
		swap(p.x,p.y);
		swap(q.x,q.y);
		fl=true;
	}
	point r;

	r.x=p.x;
	r.y=sqrt(R*R-r.x*r.x);
	if(!between(p.y,q.y,r.y))
		r.y=-r.y;

	if(fl) swap(r.x,r.y);
	res.push_back(r);
}

double GetCross(double x1,double y1,double x2,double y2)
{
	vector<point> v;
	bool i11=inside(x1,y1);
	bool i12=inside(x1,y2);
	bool i21=inside(x2,y1);
	bool i22=inside(x2,y2);
	if(i11) v.push_back(point(x1,y1));
	if(i12) v.push_back(point(x1,y2));
	if(i21) v.push_back(point(x2,y1));
	if(i22) v.push_back(point(x2,y2));
	vector<point> cp;
	if(i11 ^ i12)
	{
		Crosser(point(x1,y1),point(x1,y2),cp);
	}
	if(i12 ^ i22)
	{
		Crosser(point(x1,y2),point(x2,y2),cp);
	}
	if(i22 ^ i21)
	{
		Crosser(point(x2,y2),point(x2,y1),cp);
	}
	if(i21 ^ i11)
	{
		Crosser(point(x2,y1),point(x1,y1),cp);
	}
	// cp must contain exactly 2 points
	assert(sz(cp)==2);
	double alpha=Angle(cp[0],cp[1]);
	double res=sqr(R)*0.5*(alpha-sin(alpha));
	for(int i=0;i<sz(cp);i++)
		v.push_back(cp[i]);
	v=ConvexHull(v);
	double sq=0.0;
	for(int i=0;i<sz(v);i++)
	{
		sq+=v[i]*v[(i+1)%sz(v)];
	}
	sq*=0.5;
	sq=abs(sq);
	res+=sq;
	return res;
}

int main()
{
	int tc;
	cin >> tc;
	for(int ic=0;ic<tc;ic++){		
		cin >> f >> R >> t >> r >> g;
		double _R=R;
		double res=0.0;

		r+=min(f,g*0.5);
		g-=2.0*f;
		if(g<0) g=0;
		t+=f;
		t=min(t,R);
		R-=t;

		for(int i=-maxn;i<=maxn;i++)
		{
			if((r+(i+0.0)*(2.0*r+g))>R+eps || (r+g+(i+0.0)*(2.0*r+g))<-R-eps)
				continue;
			for(int j=-maxn;j<=maxn;j++)
			{
				double x1=r+(i+0.0)*(2.0*r+g);
				double x2=x1+g;
				double y1=r+(j+0.0)*(2.0*r+g);
				double y2=y1+g;
				bool i11=inside(x1,y1);
				bool i12=inside(x1,y2);
				bool i21=inside(x2,y1);
				bool i22=inside(x2,y2);
				if(!i11 && !i12 && !i21 && !i22) continue;
				if(i11 && i12 && i21 && i22)
				{
					res+=g*g;
					continue;
				}
				res+=GetCross(x1,y1,x2,y2);
			}
		}

		res/=pi*_R*_R;
		res=1.0-res;
		printf("Case #%d: %.6lf\n",ic+1,res);
	}
	return 0;
}
