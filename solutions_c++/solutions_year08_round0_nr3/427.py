#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
using namespace std;

char buf[200];

const long double pi = 3.141592653589793238462643383;

long double csec(long double R, long double d){
	long double b = (R*R*acos(d/R)-d*sqrt(R*R-d*d))/2;
	return b;
}

long double sqarea(long double R,long double x, long double y,long double g){
	if( (x+g)*(x+g) + (y+g)*(y+g) <= R ) return g*g;
	long double x1 = min( x+g, sqrt(R*R-y*y));
	long double y1 = min( y+g, sqrt(R*R-x*x));
	long double x2 = min( x+g, sqrt(R*R-y1*y1));
	long double y2 = min( y+g, sqrt(R*R-x1*x1));
	long double A = (x2-x)*(y1-y);
	A += csec( R, x2 ) - csec( R,x1) - y*(x1-x2);
	return A;
}

double fly(){
	double f, R, t, r, g;
	gets(buf); sscanf(buf, "%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
	f/=R, t/=R,r/=R, g/=R;

	long double TA  = pi/8;
	long double ta = 0;
	long double ir = 1-t-f;
	long double gp = g -2*f;
	long double rp = 2*r+2*f;

	if( ir <= 0 || gp <= 0 ) return 1.;

	for( long double y = r + f; 2*y*y < ir; y+=gp+rp){
		long double xmx = sqrt( ir*ir - y*y);
		ta += sqarea( ir, y, y, gp)/2;
		for( long double x = y+rp+gp; x < xmx; x+= rp+gp){
			ta += sqarea( ir, x, y, gp);
		}
	}
	return 1.-ta/TA;
}

int main(){
	freopen("Cin.txt","r",stdin);
	freopen("Cout.txt","w",stdout);

	int N;
	gets(buf); sscanf(buf,"%d", &N);

	for(int nc = 1; nc <= N; ++nc){
		fprintf(stderr,"%d / %d\r",nc,N);
		double r = fly();
		printf( "Case #%d: %8.6f\n", nc, r);
	}
}
