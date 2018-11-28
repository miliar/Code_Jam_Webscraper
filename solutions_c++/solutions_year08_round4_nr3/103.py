#include <stdio.h>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <set>
#include <map>

using namespace std;

#define fo(a,b,c) for( ( a ) = ( b ); ( a ) < ( c ); ++ ( a ) )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )

const int maxn = 1005;

int n, m;
int x[maxn], y[maxn], z[maxn], p[maxn];

double moo3( double xx, double yy, double zz )
{
	int i;
	double ret = 0;
	
	fi( n ) ret = max( ret, ( fabs( xx - x[i] ) + fabs( yy - y[i] ) + fabs( zz - z[i] ) ) / p[i] );
	
	return ret;
}

double moo2( double x, double y )
{
	int i;
	double ll = -1000001, rr = 1000001;
	fi( 100 )
	{
		double ee1 = ( ll + ll + rr ) / 3;
		double ee2 = ( ll + rr + rr ) / 3;
		double vv1 = moo3( x, y, ee1 );
		double vv2 = moo3( x, y, ee2 );
		if( vv1 >= vv2 ) ll = ee1;
		else rr = ee2;
	}
	
	return moo3( x, y, ll );
}

double moo1( double x )
{
	int i;
	double ll = -1000001, rr = 1000001;
	fi( 100 )
	{
		double ee1 = ( ll + ll + rr ) / 3;
		double ee2 = ( ll + rr + rr ) / 3;
		double vv1 = moo2( x, ee1 );
		double vv2 = moo2( x, ee2 );
		if( vv1 >= vv2 ) ll = ee1;
		else rr = ee2;
	}
	
	return moo2( x, ll );
}

int main( )
{
	int i, j, k, t, tt;
	
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	scanf( "%d", &t );
	for( tt = 1; tt <= t; ++ tt )
	{
		scanf( "%d", &n );
		fi( n ) scanf( "%d %d %d %d", &x[i], &y[i], &z[i], &p[i] );
		
		double ll = -1000001, rr = 1000001;
		fi( 100 )
		{
			double ee1 = ( ll + ll + rr ) / 3;
			double ee2 = ( ll + rr + rr ) / 3;
			double vv1 = moo1( ee1 );
			double vv2 = moo1( ee2 );
			if( vv1 >= vv2 ) ll = ee1;
			else rr = ee2;
		}
		fprintf( stderr, "%d\n", tt );
		printf( "Case #%d: %.12lf\n", tt, moo1( ll ) );
	}
	
	return 0;
}
