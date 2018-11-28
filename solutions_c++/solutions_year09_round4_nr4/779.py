#include <iostream>
#include <cmath>
using namespace std;

int t;
struct point {
	double x;
	double y;
	double R;
}p[ 1000 ];

int n;

double Max( double a, double b ) {
	return a > b ? a : b;
}

double X ( point A, point B ) {
	double d = (A.x - B.x) * ( A.x - B.x ) + (A.y - B.y ) * ( A.y - B.y );
	d = sqrt( d );
	d += A.R + B.R;
	return d / 2;
}

int main() {
	int i, T;



	freopen ( "D-small.in", "r", stdin );
	freopen ( "D-small.out", "w", stdout );


	scanf("%d", &t);
	T = t;
	while( t-- ) {
		scanf("%d", &n);
		for(i = 0; i < n; i++) {
			scanf("%lf %lf %lf", &p[i].x, &p[i].y, &p[i].R );
		}
		printf("Case #%d: ", T - t);

		if( n == 1 ) {
			printf("%.10lf\n", p[0].R );
		}else if( n == 2 ) {
			printf("%.10lf\n", p[0].R > p[1].R ? p[0].R : p[1].R );
		}else if( n == 3 ) {
			double A = Max( X( p[0], p[1] ), p[2].R );
			double B = Max( X( p[0], p[2] ), p[1].R );	
			double C = Max( X( p[2], p[1] ), p[0].R );

			if( B < A )
				A = B;
			if( C < A )
				A = C;

			printf("%.10lf\n", A );
		}
	}
	return 0;
}