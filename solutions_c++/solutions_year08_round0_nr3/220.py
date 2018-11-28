#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

double PI;

double f, R, t, r, g, orgS;
double R2, TOTAL;

const double INC = 0.0000001;

double formula(double x)
{
	return x * sqrt( R*R - x*x ) / 2.0 + R*R/2.0 * asin( x / R);
}
double integral(double a, double b)
{
	return formula(b) - formula(a);
}
double getS( double x, double y)
{
	double rightB, topB, rightBy;
	double s = 0;
	rightB = x + g;
	topB = min( y + g, sqrt(R*R - x*x) );
	rightBy = 
	 (R - rightB > 0) ? max(y, sqrt( R*R - rightB * rightB)) : y;
	double res = integral(rightBy, topB) - (topB - rightBy) * x;
//	printf("%lf\n", res);
	return res + (rightBy - y) * g;
#if 0
	for(double c = y; c <= topB; c += INC){
		s += (min(rightB, sqrt(R*R-c*c)) - x) * INC;
	}
#endif
	return s;
}
int main()
{
	int caseN;
	PI = acos(-1);
	scanf("%d",&caseN);
	for(int cc=0;cc < caseN;cc++){
		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
		orgS = PI * R * R;

		g = max(0.0, g - 2*f);
		r = r + f;
		R = max(0.0, R - f - t);
		R2 = R*R;
		TOTAL = 0;
		for(double x= r; x <= R;x += g+2*r){
			for(double y=r;y <= R;y += g+2*r){
				double dis = x*x + y*y;
				if(dis > R2)
					break;
				double hx = x+g;
				double hy = y+g;
				if( hx * hx + hy * hy <= R2){
					TOTAL += g*g;
				}else{
					TOTAL += getS( x ,y);
				}
			}
		}
		printf("Case #%d: %.6lf\n", cc+1, 1 - TOTAL / (orgS / 4.0));
	}
}
