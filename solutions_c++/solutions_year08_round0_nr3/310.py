#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdlib>

using namespace std;

#define sz(v) ((int)(v).size())
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef double D;

template<class T>T abs(T x) { return (x>0) ? x : -x; }
template<class T>T sqr(T x) { return x*x;            }

const double pi=2*asin(1.);
const double eps=1e-8;

struct P {
	D x,y;
	P() {}
	P(D x, D y): x(x), y(y) {}
	P operator +(P a) {
		return P(x+a.x, y+a.y);
	}
	P operator -(P a) {
		return P(x-a.x, y-a.y);
	}
	D operator *(P a) {
		return x*a.y-y*a.x;
	}
	D dist() {
		return sqrt(sqr(x)+sqr(y));
	}
};

bool cross(P a, P b, D r, P &res) {
	D x0=a.x;
	D y0=a.y;
	D al=(b-a).x;
	D be=(b-a).y;
	
	D A=al*al+be*be;
	D B=2*x0*al+2*y0*be;
	D C=x0*x0+y0*y0-r*r;

	D d=B*B-4*A*C;
	if (d<-eps) 
		return false;
	if (d<0)
		d=0;
	
	D t=(-B+sqrt(d))/(2*A);
	if (0-eps<t && t<1+eps) {
		res=P(x0+al*t,y0+be*t);
		D d=res.dist();
		return true;
	}
	t=(-B-sqrt(d))/(2*A);
	if (0-eps<t && t<1+eps) {
		res=P(x0+al*t,y0+be*t);
		return true;
	}
	return false;
}

D getArea(vector<P> a, D r) {
	vector<P> b;
	vector<P> c;
	for (int i=0; i<sz(a); i++) {
		if (a[i].dist()<r+eps)
			b.pb(a[i]);
		P tmp;
		if (cross(a[i],a[(i+1)%sz(a)],r,tmp)) {
			b.pb(tmp);
			c.pb(tmp);
		}
	}
	D res=0;
	for (int i=1; i<sz(b); i++)
		for (int j=i+1; j<sz(b); j++)
			if ((b[i]-b[0])*(b[j]-b[0])>eps)
				swap(b[i],b[j]);
	for (int i=0; i<sz(b); i++) 
		res+=b[i]*b[(i+1)%sz(b)];
	res=0.5*abs(res);
	int bestI=-1, bestJ=-1;
	D bestD=-1;
	for (int i=0; i<sz(c); i++)
		for (int j=i+1; j<sz(c); j++)
			if ((c[i]-c[j]).dist()>bestD) {
				bestD=(c[i]-c[j]).dist();
				bestI=i;
				bestJ=j;
			}
	if (bestD>-eps) {
		D al=2*asin(bestD/2/r);
		D Sall=0.5*al*sqr(r);
		D Str=0.5*sin(al)*sqr(r);
		D s=Sall-Str;
		res+=s;
	}
	return res;
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

	int tn;
	cin>>tn;
	for (int tst=0; tst<tn; tst++) {
		fprintf(stderr,"Case #%d: ",tst+1);
		printf("Case #%d: ",tst+1);
		D f,R,t,r,g;
		cin>>f>>R>>t>>r>>g;
		vector<D> x;
		double cur=r;
		while (cur+eps<R) {
			x.pb(cur);
			cur+=g+2*r;
		}
		double area=0;
		for (int i=0; i<sz(x); i++)
			for (int j=0; j<sz(x); j++) {
				if (2*f+eps>g) continue;
				vector<P> p;
				p.pb(P(x[i]+f,x[j]+f));
				p.pb(P(x[i]+g-f,x[j]+f));
				p.pb(P(x[i]+g-f,x[j]+g-f));
				p.pb(P(x[i]+f,x[j]+g-f));
				area+=getArea(p,R-t-f);
			}
		area*=4;
		printf("%.6lf\n",1-area/pi/R/R);
	}

	return 0;
}
