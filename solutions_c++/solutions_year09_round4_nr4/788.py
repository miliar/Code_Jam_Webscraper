#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

int t, n, neuz[ 45 ];
double x[ 45 ], y[ 45 ], r[ 45 ];
double X, Y;

/*void provjeri( double R ) {
	for( int i = 0; i < n; ++i ) {
		double rx = x[ i ] - X;
		double ry = y[ i ] - Y;
		double L = sqrt( rx * rx + ry * ry ) + r[ i ];
		neuz[ i ] = ( L <= R );
	}
}*/

int pokriva( int a, int b, int c, double R ) {
	int nz[ 3 ]; nz[ 0 ] = a;
	nz[ 1 ] = b; nz[ 2 ] = c;
	double L; X = 0; Y = 0;
	
	for( int i = 0; i < 300; ++i ) {
		int ind = -1; double maxl = -1;
		for( int j = 0; j < 3; ++j ) {
			double rx = x[ nz[ j ] ] - X;
			double ry = y[ nz[ j ] ] - Y;
			L = sqrt( rx * rx + ry * ry ) + r[ nz[ j ] ];
			if( L > maxl ) { maxl = L; ind = nz[ j ]; }
		}
		
		L += 1e-7;
		X = x[ ind ] + ( X - x[ ind ] ) * ( ( R - r[ ind ] ) / ( L - r[ ind ] ) );
		Y = y[ ind ] + ( Y - y[ ind ] ) * ( ( R - r[ ind ] ) / ( L - r[ ind ] ) );
	}
	
	for( int i = 0; i < n; ++i ) {
		double rx = x[ i ] - X;
		double ry = y[ i ] - Y;
		L = sqrt( rx * rx + ry * ry ) + r[ i ] - 1e-7;
		if( L <= R ) neuz[ i ] = 1;
	}
	
	for( int i = 0; i < 3; ++i ) {
		double rx = x[ nz[ i ] ] - X;
		double ry = y[ nz[ i ] ] - Y;
		L = sqrt( rx * rx + ry * ry ) + r[ nz[ i ] ];
		if( L > R ) return( 0 );
	}
	
	return( 1 );
}

int pronadji( double R ) {
	double L = 0; //neuz[ 1 ] = 1;
	
	for( int i = 0; i < 300; ++i ) {
		int ind = -1; double maxl = -1;
		for( int j = 0; j < n; ++j ) {
			if( neuz[ j ] ) continue;
			double rx = x[ j ] - X;
			double ry = y[ j ] - Y;
			L = sqrt( rx * rx + ry * ry ) + r[ j ];
			if( L > maxl ) { maxl = L; ind = j; }
		}
		
		if( ind == -1 ) break;
		
		L += 1e-7;
		X = x[ ind ] + ( X - x[ ind ] ) * ( ( R - r[ ind ] ) / ( L - r[ ind ] ) );
		Y = y[ ind ] + ( Y - y[ ind ] ) * ( ( R - r[ ind ] ) / ( L - r[ ind ] ) );
	}
	
	printf( "[%lf %lf]\n", X, Y );
	//return( 1 ); 
	for( int i = 0; i < n; ++i ) {
		if( neuz[ i ] ) continue;
		double rx = x[ i ] - X;
		double ry = y[ i ] - Y;
		L = sqrt( rx * rx + ry * ry ) + r[ i ] - 1e-7;
		if( L > R ) return( 0 );
	}
	
	return( 1 );
}

int solve( double R ) {
	for( int a = 0; a < n; ++a )
		for( int b = a; b < n; ++b )
			for( int c = b; c < n; ++c ) {
				memset( neuz, 0, sizeof( neuz ) );
				//printf( "(%lf %lf)\n", X, Y );
				printf( "(%d %d %d %lf), %d\n", a, b, c, R, pokriva( a, b, c, R ) );
				//printf( "(%lf %lf)\n", X, Y );
				if( !pokriva( a, b, c, R ) ) continue;
				if( pronadji( R ) ) return( 1 );
			}
	
	return( 0 );
}

double rac( int xx ) {
	int yy = ( xx + 1 ) % 3, zz = ( xx + 2 ) % 3;
	double rx = x[ yy ] - x[ zz ];
	double ry = y[ yy ] - y[ zz ];
	double L = sqrt( rx * rx + ry * ry ) + r[ yy ] + r[ zz ];
	return max( r[ xx ], L * 0.5 );
}

int main( void ) {
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i ) {
		scanf( "%d", &n );
		for( int j = 0; j < n; ++j )
			scanf( "%lf %lf %lf", &x[ j ], &y[ j ], &r[ j ] );
		
		/*double a = 0, b = 1000;
		while( b - a > 1e-7 ) {
			double mid = ( a + b ) * 0.5;
			//printf( "%lf: %d\n", mid, solve( mid ) );
			if( solve( mid ) ) b = mid; else a = mid;
		}*/
		
		//printf( "Case #%d: %lf\n", i + 1, ( a + b ) * 0.5 );
		if( n == 1 ) printf( "Case #%d: %lf\n", i + 1, r[ 0 ] );
		else if( n == 2 ) {
			printf( "Case #%d: %lf\n", i + 1, max( r[ 0 ], r[ 1 ] ) );
		} else {
		printf( "Case #%d: %lf\n", i + 1, min( min( rac( 0 ), rac( 1 ) ), rac( 2 ) ) );
		}
	}
	
	return( 0 );
}
