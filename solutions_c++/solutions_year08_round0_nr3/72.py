#include <algorithm>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

#define MAX_N 100

inline double sq(double x) { return x * x; }
inline double dist(double x,double y){return sqrt(sq(x)+sq(y));}
inline double mysqrt(double x) { return x < 0. ? 0. : sqrt(x); } // double rounding errors.

double solve(void)
{
	double f,R,t,r,g;
	scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
//	printf("%lf %lf %lf %lf %lf\n",f,R,t,r,g);

	if(f * 2. >= g) return 1.;

	double total = 0.;
	double bucket = g - f * 2.;
	bucket *= bucket;

	const double q(R-t); // the radius of the inside circle

	if(q <= f) return 1.;

	for(double i=r;i<q;i+=2.*r+g)
		for(double j=r;dist(i,j)<q;j+=2.*r+g)
		{
			if(dist(i+g,j+g) <= q)
				total += bucket;
			else
			{
				double Q = q-f;
				double I1 = i+f;
				double I2 = i+g-f;
				double J1 = j+f;
				double J2 = j+g-f;

				if(dist(I1,J1)>=Q)continue;

				double lower = (dist(I1,J2)>=Q?I1:sqrt(sq(Q)-sq(J2)));
				double upper = (dist(I2,J1)<=Q?I2:sqrt(sq(Q)-sq(J1)));

				total += (lower - I1) * (J2 - J1);
				// total += (I2 - upper) * (J2 - J1); // this is on the OUTSIDE

				// f(x)=sqrt(r^2-x^2)
				// F(x)=(asin(x/r)*r^2+x*sqrt(r^2-x^2))/2
#define F(x) ((asin(x/Q)*sq(Q)+x*mysqrt(sq(Q)-sq(x)))/2.)
 				total += (F(upper) - F(lower)) - (upper - lower) * J1;
			}
		}

	return 1. - (total / (atan(1) * R * R));
}

int main(void)
{
	int n;

	scanf("%d",&n);

	for(int i=0;i<n;i++)
		printf("Case #%d: %.6lf\n",i+1,solve());

	return 0;
}
