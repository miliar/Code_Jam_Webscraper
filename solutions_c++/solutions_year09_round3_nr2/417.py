#include <cstdio>
#include <cmath>

using namespace std;

#define REP(i,n) for (int i=0;i<(n);i++)
typedef long double ld;

struct pt
{
	ld x,y,z;
};

pt c;
pt v;

ld dist(double t)
{
	pt r;
	r.x = c.x + v.x*t;
	r.y = c.y + v.y*t;
	r.z = c.z + v.z*t;
	return (ld)r.x*r.x+r.y*r.y+r.z*r.z;
}

ld minv;
ld thet;

#define EPS 0.0000000000001

void trisearch(double st, double en, int count)
{
	for (int cnt=0;cnt<1000000;cnt++) {
		double d = (en-st)/3;
		if ( d < EPS ) break;
		double t1 = st+d;
		double t2 = t1+d;

		ld v1 = dist(t1);
		ld v2 = dist(t2);
		if (v1<minv || ( abs(v1-minv)<EPS && t1<thet) ) {
			minv=v1; thet=t1;
		}
		if (v2<minv) {
			minv=v2; thet=t2;
		}
		if (v1<v2 || abs(v1-v2)<EPS) en=t2;
		else st=t1;
	}
}


int main()
{
	int tc;
	scanf("%d", &tc);
	for (int tno=1; tno<=tc;tno++)
	{
		int n;
		scanf("%d", &n);

		v.x=v.y=v.z=c.x=c.y=c.z=0.0;

		REP(i,n) {
			int x,y,z,vx,vy,vz;
			scanf("%d %d %d %d %d %d", &x, &y, &z, &vx, &vy, &vz);
			c.x+=x;
			c.y+=y;
			c.z+=z;
			v.x+=vx;
			v.y+=vy;
			v.z+=vz;
		}

		minv=1e+100;

		trisearch(0,1000000,0);

		minv = sqrt(minv/n/n);

		printf("Case #%d: %.6Lf %.6f\n", tno, minv, thet);
	}
	return 0;
}