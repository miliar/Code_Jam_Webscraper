#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <cctype>
#include <cmath>

#define mp make_pair
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define sz(v) ((int)(v.size()))

using namespace std;

typedef long long int64;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<string> vs;

template<class T> T abs(T x){return x>0 ? x:(-x);}
template<class T> T sqr(T x){return x*x;}

const double eps=1E-9;
const double delta=1E-8;

struct point
{
	double x,y,z;
	double p;
	point(double x=0,double y=0,double z=0,double p=0):x(x),y(y),z(z),p(p){}
	void read()
	{
		cin >> x >> y >> z;
	}
	double len()
	{
		return sqrt(x*x+y*y+z*z);
	}
};

struct Position
{
	double a[4][2];
	Position()
	{
		for(int i=0;i<4;i++)
			a[i][0]=-1E10,a[i][1]=1E10;
	}
	bool empty()
	{
		for(int i=0;i<4;i++)
			if(a[i][1]-a[i][0]<eps) return true;
		return false;
	}
};

vector<point> v;
vector<double> p;
int n;

void cross(double x1,double x2,double y1,double y2,double& z1,double& z2)
{
	vector<pair<double,int> > v;
	v.push_back(mp(x1,1));
	v.push_back(mp(x2,1));
	v.push_back(mp(y1,2));
	v.push_back(mp(y2,2));
	sort(all(v));
	int nw=0;
	z1=0.0;
	z2=0.0;
	for(int i=0;i<sz(v);i++)
	{
		nw^=v[i].second;
		if(nw==3)
		{
			z1=v[i].first;
			z2=v[i+1].first;
		}
	}
}

Position cross(Position a,point b)
{
	for(int i=0;i<4;i++)
	{
		double c1,c2,q1,q2;
		double x0=b.x;
		double y0=b.y;
		double z0=b.z;
		double p=b.p;
		if(i==0)
		{
			q1=p+x0+y0+z0;
			q2=x0+y0+z0-p;
		}
		else if(i==1)
		{
			q1=x0+y0-z0+p;
			q2=x0+y0-z0-p;
		}
		else if(i==2)
		{
			q1=x0-y0-z0+p;
			q2=x0-y0-z0-p;
		}
		else if(i==3)
		{
			q1=x0-y0+z0+p;
			q2=x0-y0+z0-p;
		}
		else throw 57;
		cross(a.a[i][0],a.a[i][1],q1,q2,c1,c2);
		a.a[i][0]=c1;
		a.a[i][1]=c2;
	}
	return a;
}

bool check(double P)
{
	for(int i=0;i<sz(v);i++)
		v[i].p=p[i]*P;
	Position cur;
	for(int i=0;i<sz(v);i++)
	{
		cur=cross(cur,v[i]);
		if(cur.empty()) return false;
	}
	if(cur.empty()) return false;
	return true;
}


int main()
{
	int tc;
	cin >> tc;
	for(int ic=0;ic<tc;ic++)
	{
		printf("Case #%d: ",ic+1);
		p.clear();
		v.clear();
		cin >> n;
		for(int i=0;i<n;i++)
		{
			point q;
			q.read();
			v.push_back(q);
			double x;
			cin >> x;
			p.push_back(x);
		}
		double up=1E20,down=0.0,t;
		while(up-down>delta)
		{
			t=(up+down)*0.5;
			if(check(t))
				up=t;
			else
				down=t;
		}
		printf("%.6lf",(up+down)*0.5);
		printf("\n");
	}
	return 0;
}
