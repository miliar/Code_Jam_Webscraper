#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a):(-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))

#define pii pair < int, int >
#define MP make_pair
#define X first
#define Y second 

#define eps 1e-9
#define mpi 3.1415926535897932384626433832795

double _f, _R, _t, _r, _g;
double R;

#define inCircle(x, y) ( sqr(x) + sqr(y) < sqr(R) + eps )



int main () {
	int i, j, T;
	double x, y;

	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%lf%lf%lf%lf%lf", &_f, &_R, &_t, &_r, &_g);

		R = _R - _t - _f;

		double Sfly = 0.0;
		pair < double, double > A, B;

		double w = _g - _f - _f;
		double step = _g + _r + _r;

		for (x = _r + _f; x < R + eps; x += step) {
			for (y = _r + _f; inCircle(x,y); y += step) {
				if( inCircle(x + w, y + w) ) Sfly += sqr( w );
				else {
					if ( inCircle( x, y+w ) ) A = MP( sqrt( sqr(R) - sqr(y+w) ), y + w );
					else A = MP( x, sqrt( sqr(R) - sqr(x) ) );

					if ( inCircle( x+w, y ) ) B = MP( x + w, sqrt( sqr(R) - sqr(x+w) ) );
					else B = MP( sqrt( sqr(R) - sqr(y) ), y );

					double alpha = atan2( A.Y, A.X ) - atan2( B.Y, B.X );

					double Ssect = sqr(R) * alpha * 0.5;
					double Str = 0.5 * sin(alpha) * sqrt( sqr(A.X) + sqr(A.Y) ) * sqrt( sqr(B.X) + sqr(B.Y) );
					double Ssegm = Ssect - Str;

					double S1 = 0.5 * (A.X - x) * (A.Y - y);
					double S2 = 0.5 * (B.X - x) * (B.Y - y);
					double S3 = 0.5 * fabs( (A.X - x) * (B.Y - y) - (B.X - x) * (A.Y - y) );
					//S3 = 0.5 * fabs( A.X*B.Y + B.X*y + x*A.Y - A.Y*B.X - B.Y*x - y*A.X );

					Sfly += Ssegm + S1 + S2 + S3;
				}
			}
		}

		double P = 1.0 - (4.0 * Sfly) / (mpi * sqr(_R));
		
		printf("Case #%d: %.6lf\n", cas, P);
	}



	return 0;
}