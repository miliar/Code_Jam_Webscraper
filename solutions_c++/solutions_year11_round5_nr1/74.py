#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

const double eps = 1e-12;

double area, W;
int L, U, Lx[110], Ly[110], Ux[110], Uy[110];

double calc2( int* x, int *y, int i, double line ){
	return y[i-1] + ( line - x[ i - 1 ] ) * ( y[i] - y[ i - 1 ] ) / (double)( x[i] - x[ i - 1 ] );
}

double calc( int l, int u, double x ){
	return calc2( Ux, Uy, u, x ) - calc2( Lx, Ly, l, x );
}

double solve( double now, double tar ){
	double add, beg, end, mid;
	double minimum;
	area = 0;
	int i, j;
	while( true ){
		for ( i = 0; i < L; i ++ )
			if ( Lx[i] > now + eps )
				break;
		for ( j = 0; j < U; j ++ )
			if ( Ux[j] > now + eps )
				break;
		if ( i == L && j == U )
			break;
		minimum = min( Lx[i], Ux[j] );
		add = ( calc( i, j, now ) + calc( i, j, minimum ) ) * ( minimum - now );
		if ( area + add > tar ){
			beg = now;
			end = minimum;
			while( end - beg > eps ){
				mid = ( beg + end ) / 2;
				add = ( calc( i, j, now ) + calc( i, j, mid ) ) * ( mid - now );
				if ( area + add > tar )
					end = mid;
				else
					beg = mid;
			}
			return mid;
		}
		else{
			area += add;
			now = minimum;
		}
	}
	
	return now;
}

main(){
	freopen( "AL.in", "r", stdin );
	freopen( "AL.out", "w", stdout );
	
	double avg, line;
	int t, tt = 0;
	int G, i;
	
	scanf ( "%d", &t );
	while( t -- ){
		scanf ( "%lf %d %d %d", &W, &L, &U, &G );
		for ( i = 0; i < L; i ++ )
			scanf ( "%d %d", Lx + i, Ly + i );
		for ( i = 0; i < U; i ++ )
			scanf ( "%d %d", Ux + i, Uy + i );
		solve( 0, 20000000 );
		line = 0;
		avg = area / G;
		printf( "Case #%d:\n", ++ tt );
		for ( i = 1; i < G; i ++ ){
			line = solve( line, avg );
			printf( "%.10lf\n", line );
		}
		
	}
	
	return 0;
}
