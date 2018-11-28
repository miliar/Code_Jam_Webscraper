#include <vector>
#include <set>
#include <string>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <iostream>
#include <cassert>
#include <cctype>
#include <cmath>
#include <map>
#include <deque>
#include <algorithm>

using namespace std;

const double EPS = 1.0E-11;

double ci_bla( double a, double x ) {
	double tmp = a*a-x*x;
	if( tmp < 0.0 ) tmp = 0.0;

	//cout << "ci_bla :" << x << ' ' << x/a << endl;
	return x/2.0 * sqrt( tmp ) + a*a/2.0 * asin( x/a );
}

double ci( double u, double v, double a ) {
	assert( a > 0.0 && fabs(u) <= a+EPS && fabs(v) <= a+EPS );
	return ci_bla( a, v ) - ci_bla( a, u );
}

int main() {
	int cases;
	double f, R, t, r, g;
	
	cin >> cases;
	for( int caseid = 1; caseid <= cases; ++caseid ) {
		cin >> f >> R >> t >> r >> g;
		
		double area = 0.0;
		if( g <= 2.0*f ) {
			cout << "Case #" << caseid << ": 1.0\n";
			continue;
		}
		
		for( int i = 0; ; ++i ) {
			double x0 = r + i*(g+2.0*r) + f;
			if( x0 >= R-t-f-EPS ) break;
			double x1 = x0 + g - 2.0*f;
			
			for( int j = 0; ; ++j ) {
				double y0 = r + j*(g+2.0*r) + f;
				if( x0*x0 + y0*y0 >= (R-t-f)*(R-t-f)-EPS ) break;
				double y1 = y0 + g - 2.0*f;
				
				if( x1*x1 + y1*y1 <= (R-t-f)*(R-t-f)+EPS ) {
					area += (g-2.0*f)*(g-2.0*f);
					continue;
				}
				
				//cout << x0 << ' ' << y0 << ' ' << x1 << ' ' << y1 << endl;
				
				int up_inc = (x0*x0+y1*y1 <= (R-t-f)*(R-t-f)+EPS );
				int right_inc = (x1*x1+y0*y0 <= (R-t-f)*(R-t-f)+EPS );
				
				if( up_inc && right_inc ) {
					double tmp = (R-t-f)*(R-t-f)-y1*y1;
					if( tmp < 0.0 ) tmp = 0.0;
					tmp = sqrt( tmp );
					//cout << "case up+right; tmp = " << tmp << endl;
					//cout << "up+right (tmp) : " << (tmp-x0)*(g-2.0*f) << ' ' <<  fabs(ci( tmp, x1, R-t-f ))  << ' ' << (x1-tmp)*y0 << endl;
					area += (tmp-x0)*(g-2.0*f) + fabs(ci( tmp, x1, R-t-f )) - (x1-tmp)*y0;
				} else if( right_inc ) {
					//cout << "case right\n";
					area += fabs(ci( x0, x1, R-t-f )) - (x1-x0)*y0;
				} else if( up_inc ) {
					//cout << "case up\n";
					area += fabs( ci( -y1, -y0, R-t-f ) ) - (y1-y0)*x0;
				} else {
					//cout << "case nix\n";
					double tmp = (R-t-f)*(R-t-f)-y0*y0;
					if( tmp < 0.0 ) tmp = 0.0;
					tmp = sqrt( tmp );
					area += fabs( ci( x0, tmp, R-t-f ) ) - (tmp-x0)*y0;
				}
			}
		}
		area *= 4;
		cout << "Case #" << caseid << ": ";
		double nhit = area / (R*R*M_PI);
		printf( "%.20f\n", 1.0-nhit );
	}
	return 0;
}

