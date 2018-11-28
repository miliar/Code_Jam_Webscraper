#pragma comment( linker, "/stack:128000000" )
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>

void prepare( )
{
	freopen( "input.txt", "r", stdin );
#ifndef _DEBUG
	freopen( "output.txt", "w", stdout );
#endif
}

#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <sstream>
#include <iostream>
#include <deque>

using namespace std;

#define fo(a,b,c) for(a =(b);a<(c);++a)
#define fr(a,b) fo(a,0,(b))
#define fi(a) fr(i,(a))
#define fj(a) fr(j,(a))
#define fk(a) fr(k,(a))
#define all(a) (a).begin(),(a).end()
#define mp make_pair
#define pb push_back
#define sz(a) (int)(a).size()
#define _(a,b) memset((a),(b),sizeof(a))
#define __(a) _((a),0)

typedef long long lint;

const int MAXN = 5005;
const double eps = 1e-9;
const double ADDY = 10005;

struct C
{
	double x, y;
	double sqrDist( ) { return x * x + y * y; }
	double dist( ) { return sqrt( sqrDist( ) ); }
	C( ) { x = y = 0; }
	C( double _x, double _y ): x( _x ), y( _y ) { }
};

bool eq( const double &a, const double &b ) { return a - b < eps && b - a < eps; }
C operator-( const C &a, const C &b ) {	return C( a.x - b.x, a.y - b.y ); }
C operator+( const C &a, const C &b ) {	return C( a.x + b.x, a.y + b.y ); }
C operator*( const C &a, const double &b ) { return C( a.x * b, a.y * b ); }
C operator/( const C &a, const double &b ) { return C( a.x / b, a.y / b ); }

struct Circ
{
	C c;
	double r;
};

Circ c[MAXN];
vector <double> xs;
vector <C> ms;
vector <pair< double, int> > s;
int n, m;
double ans[2];

double sqr( const double &a )
{
	return a * a;
}

vector<C> intersect( const Circ &a, const Circ &b )
{
	vector<C> res;
	C v = b.c - a.c;
	double d = v.dist( );
	if ( a.r > b.r + d - eps || b.r > a.r + d - eps || d > a.r + b.r - eps )
		return res;
	double anga = acos( ( sqr( a.r ) + sqr( d ) - sqr( b.r ) ) / ( 2 * a.r * d ) );
	double angb = atan2( v.y, v.x );
	C c1( cos( angb + anga ), sin( angb + anga ) );
	res.push_back( a.c + c1 * a.r );
	C c2( cos( angb - anga ), sin( angb - anga ) );
	res.push_back( a.c + c2 * a.r );
	return res;
}

double getInteg( const Circ &c, const double &x )
{
	double h = ( x - c.c.x ) / c.r;
	if ( h > 1 )
		h = 1;
	if ( h < -1 )
		h = -1;
	double t = asin( h );
	double res = sqr( c.r ) * ( sin( 2 * t ) + 2 * t ) / 4;
	return res;
}

bool getSquare( const Circ &c, const double &a, const double &b, double &up, double &down )
{
	double y = getInteg( c, b ) - getInteg( c, a );
	vector<double> res;
	double ts = ( c.c.y + ADDY ) * ( b - a );
	up = ts + y;
	down = ts - y;
	return true;
}

int main( )
{
	prepare( );
	int i, j, k;
	int t, tn;
	cin >> tn;
	fr( t, tn )
	{
		printf( "Case #%d:", t + 1 );
		scanf( "%d %d", &n, &m );
		for( i = 0; i < n; ++ i )
		{
			int x, y;
			scanf( "%d %d", &x, &y );
			c[i].c.x = x;
			c[i].c.y = y;
 		}

		int tttn;
		C mid;
		fr( tttn, m )
		{
			int x, y;
			scanf( "%d %d", &x, &y );
			mid.x = x;
			mid.y = y;
			double aminx = -1e+10, amaxx = +1e+10;
			fi( n )
			{
				c[i].r = ( c[i].c - mid ).dist( );
				aminx = max( aminx, c[i].c.x - c[i].r );
				amaxx = min( amaxx, c[i].c.x + c[i].r );
			}
			xs.clear( );

			for( i = 0; i < n; ++ i )
			{
				for ( j = i + 1; j < n; ++ j )
				{
					vector<C> a = intersect( c[i], c[j] );
					for ( k = 0; k < a.size( ); ++ k )
					{
						if ( a[k].x > aminx - eps && a[k].x < amaxx + eps )
							xs.push_back( a[k].x );
					}
				}
			}
			xs.pb( aminx );
			xs.pb( amaxx );
			sort( xs.begin( ), xs.end( ) );
			xs.resize( unique( xs.begin( ), xs.end( ), eq ) - xs.begin( ) );
			double ans = 0;
			for ( i = 1; i < xs.size( ); ++ i )
			{
				double xl = xs[i - 1];
				double xr = xs[i];
				double xm = ( xl + xr ) * 0.5;
				s.clear( );
				for ( j = 0; j < n; ++ j )
				{
					if ( c[j].c.x - c[j].r < xm - eps && c[j].c.x + c[j].r > xm + eps )
					{
						double up, down;
						if ( getSquare( c[j], xl, xr, up, down ) )
						{
							s.push_back( make_pair( down, 1 ) );
							s.push_back( make_pair( up, -1 ) );
						}
					}
				}
				sort( s.begin( ), s.end( ) );
				int count = 1;
				for ( j = 1; j < s.size( ); ++ j )
				{
					if ( count == n )
					{
						ans += s[j].first - s[j - 1].first;
					}
					count += s[j].second;
				}
			}
			printf( " %.9lf", ans );
		}
		printf( "\n" );
	}
	return 0;
}