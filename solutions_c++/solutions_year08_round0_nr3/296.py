#include <cstdio>
#include <cmath>
#include <iostream>
using namespace std;
int kd;
const double pi=3.1415926535897932384626433832795;
const double eps=1e-16;
double f,R,t,r,g;
double ts,rs,gs,k,p;
double ans;
double sqr(double a) {
	return a*a;
}
bool lesseq(double a, double b) {
	return b-a>=-eps;
}
double ft(double x) {
	double fs,sc;
//	cerr << R-ts << ' ' << x << '\n';
//	cerr << sqr(R-ts) << ' ' << sqr(x) << '\n';
//	cerr << lesseq(sqr(R-ts),sqr(x)) << '\n';
//	cerr << x/2 << ' ' << sqrt(sqr(R-ts)-sqr(x)) << '\n';
//	cerr << "!!! " << x/2*sqrt(sqr(R-ts)-sqr(x)) << '\n';
	if (lesseq(sqr(R-ts),sqr(x))) fs=0; else fs=x/2*sqrt(sqr(R-ts)-sqr(x));
	if (lesseq(R-ts,x)) sc=sqr(R-ts)/2*pi/2; else sc=sqr(R-ts)/2*asin(x/(R-ts));
//	cerr << fs << ' ' << sc << '\n';
	return fs+sc;
}
double tegr(double a, double b, int j) {
//	cerr << b << ' ' << a << '\n';
//	cerr << ft(b) << ' ' << ft(a) << ' ' << '\n';
	return ft(b)-ft(a)-(b-a)*(k*(j-1)+rs);
}
double doit(int i, int j) {
	double a1,a2;
	if (lesseq(sqr(R-ts),sqr(k*(i-1)+rs)+sqr(k*(j-1)+rs))) return 0;
	a1=sqr(R-ts)-sqr(k*j-rs);
//	cerr << a1 << '\n';
	if (lesseq(a1,0)) {
//		cerr << sqr(R-ts)-sqr(k*(j-1)+rs) << '\n';
		a2=sqrt(sqr(R-ts)-sqr(k*(j-1)+rs));
//		cerr << a2 << '\n';
		if (a2>k*i-rs) return tegr(k*(i-1)+rs,k*i-rs,j); else return tegr(k*(i-1)+rs,a2,j);
	} else {
		a1=sqrt(a1);
		if (a1>k*i-rs) return sqr(gs);
		if (a1<k*(i-1)+rs) {
			a2=sqrt(sqr(R-ts)-sqr(k*(j-1)+rs));
			if (a2>k*i-rs) return tegr(k*(i-1)+rs,k*i-rs,j); else return tegr(k*(i-1)+rs,a2,j);
		}			
		return gs*(a1-(k*(i-1)+rs))+tegr(a1,k*i-rs,j);
	}
}
void solve(int ii) {
	int i,j,c;
	ts=t+f;
	rs=r+f;
	gs=g-2*f;
	k=gs+2*rs;
	if (lesseq(R,ts) || lesseq(gs,0)) ans=1; else {
		c=int((R-ts)/k)+1;
//		cerr << R-ts << '\n';
//		cerr << rs+gs << '\n';
		p=0;
		for (i=1; i<=c; ++i)
			for (j=1; j<=c; ++j)
				if (i<=j) {
//					cerr << doit(i,j) << '\n';
					p+=doit(i,j);
				}  else {
//					cerr << doit(j,i) << '\n';
					p+=doit(j,i);
				}
		ans=1-p/(pi*sqr(R)/4);
	}
	printf("Case #%d: %.6lf\n",ii,ans);
}
int main() {
	int i;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&kd);
	for (i=1; i<=kd; ++i) {
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
		solve(i);
	}
	return 0;
}