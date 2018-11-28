#include <cstdio>
#include <cstring>
#include <algorithm>
//#include <iostream>
using namespace std;
const int c=1024;
int tt,ii;
double s,r;
struct rec {
	int a,b;
	double s;
	rec (int aa=0, int bb=0, double ss=0) {
		a=aa;
		b=bb;
		s=ss;
	}
};
bool operator < (const rec &a, const rec &b) {
	return a.s<b.s;
}
bool cmp(const rec &a, const rec &b) {
	return a.a<b.a;
}
rec m[c+c];
int x;
double t;
int n;
int main() {
	scanf("%d",&tt);
	int i;
	for (ii=1; ii<=tt; ++ii) {
		printf("Case #%d: ",ii);
		scanf("%d%Lf%Lf%Lf%d",&x,&s,&r,&t,&n);
		for (i=1; i<=n; ++i) scanf("%d%d%Lf",&m[i].a,&m[i].b,&m[i].s);
		sort(m+1,m+n+1,cmp);
		m[0]=rec(0,m[1].a,0);
		for (i=1; i<n; ++i) m[i+n]=rec(m[i].b,m[i+1].a,0);
		m[n+n]=rec(m[n].b,x,0);
		sort(m,m+n+n+1);
//		for (i=0; i<=n+n; ++i) cerr << m[i].a << ' ' << m[i].b << ' ' << m[i].s << '\n';
		double ans=0;
		double dt=t,ddt,ds;
		for (i=0; i<=n+n; ++i) {
			ddt=min(dt,(m[i].b-m[i].a)/(m[i].s+r));
			ds=ddt*(m[i].s+r);
			dt-=ddt;
			ans+=ddt+(m[i].b-m[i].a-ds)/(m[i].s+s);									
		}
		printf("%.9Lf\n",ans);
//		cerr << '\n';
	}
	return 0;
}