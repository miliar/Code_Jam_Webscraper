#include <cstdio>
#include <cstring>
#include <cmath>
int t,ii,n;
const int c=510;
struct point {
	double x,y,z;
	point (double a=0, double b=0, double c=0) {
		x=a;
		y=b;
		z=c;
	}
};
double operator * (const point &a, const point &b) {
	return a.x*b.x+a.y*b.y+a.z*b.z;
}
point operator * (const point &a, double k) {
	return point (a.x*k,a.y*k,a.z*k);
}
point operator / (const point &a, double k) {
	return a*(1.0/k);
}
point operator + (const point &a, const point &b) {
	return point (a.x+b.x,a.y+b.y,a.z+b.z);
}
void operator += (point &a, const point &b) {
	a=a+b;
}
void operator /= (point &a, const double k) {
	a=a/k;
}
double sqr(double a) {
	return a*a;
}
double dist2(point a, point b) {
	return sqr(a.x-b.x)+sqr(a.y-b.y)+sqr(a.z-b.z);
}
point p[c],v[c];
double dmin,tmin;
void test(double t) {
	point center(0,0,0);
	point zero(0,0,0);
	int i;
	point temp;
	for (i=1; i<=n; ++i) {
		temp=p[i]+v[i]*t;
		center+=temp;
	}
	center/=n;
	double d=dist2(zero,center);
	if (d<dmin || d==dmin && t<tmin) {
		dmin=d;
		tmin=t;
	}
}
int main() {
	int i;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&t);
	for (ii=1; ii<=t; ++ii) {
		scanf("%d",&n);
		for (i=1; i<=n; ++i) scanf("%lf%lf%lf%lf%lf%lf",&p[i].x,&p[i].y,&p[i].z,&v[i].x,&v[i].y,&v[i].z);
		dmin=1e15;
		test(0);
		double t;
/*
		for (i=1; i<=n; ++i) if (v[i]*v[i]!=0) {
			t=-(p[i]*v[i])/(v[i]*v[i]);
			if (t>0) test(t);
		}
*/
		point pp(0,0,0),vv(0,0,0);
		for (i=1; i<=n; ++i) pp+=p[i];
		for (i=1; i<=n; ++i) vv+=v[i];
		pp/=n;
		vv/=n;
		if (vv*vv!=0) {
			t=-(pp*vv)/(vv*vv);
			if (t>0) test(t);
		}
		printf("Case #%d: %.8lf %.8lf\n",ii,sqrt(dmin),tmin);
	}
	return 0;
}