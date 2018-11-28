#define _CRT_SECURE_NO_WARNINGS
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <string>
#include <cstdlib>
#include <queue>
#include <stack>
using namespace std;

static const int MAXN = 44;
//static const double GOLD = 0.38196601125010515179541316563436;

inline double Sqr( double x )
{
	return x * x;
}

struct Point
{
	double X, Y;
	Point()
	{
	}
	Point( double x, double y )
		: X( x )
		, Y( y )
	{
	}
};

struct Vector
{
	double X, Y;
	Vector()
	{
	}
	Vector( double x, double y )
		: X( x )
		, Y( y )
	{
	}
};

inline Vector operator -( const Point &p1, const Point &p2 )
{
	return Vector( p1.X - p2.X, p1.Y - p2.Y );
}

inline double Abs( const Vector &v )
{
	return sqrt( Sqr( v.X ) + Sqr( v.Y ) );
}

Vector operator +( const Vector &v1, const Vector &v2 )
{
	return Vector( v1.X + v2.X, v1.Y + v2.Y );
}

Vector operator *( double x, const Vector &v )
{
	return Vector( x * v.X, x * v.Y );
}

struct sPlant : public Point
{
	double R;
	sPlant()
		
	{
	}
	sPlant( double x, double y, double r )
		: Point( x, y )
		, R( r )
	{
	}
};

int N;
sPlant Plant[ MAXN ];

void Read()
{
	int i;
	memset( Plant, 0, sizeof( Plant ) );
	scanf( "%d", &N );
	for( i = 0; i < N; ++i )
	{
		int x, y, r;
		scanf( "%d%d%d", &x, &y, &r );
		Plant[ i ].X = x;
		Plant[ i ].Y = y;
		Plant[ i ].R = r;
	}
}

double Result;

void Work()
{
	int i, j, k, m, n;

	//for( i = 0; i < N; ++i )
	//{
	//	for( j = 0; j < N; ++j )
	//	{
	//		for( k = 0; k < N; ++k )
	//		{
	//			double r;
	//			Point o( ( Plant[ i ].X + Plant[ j ].X + Plant[ k ].X ) / 3, ( Plant[ i ].Y + Plant[ j ].Y + Plant[ k ].Y ) / 3 );
	//			r = Abs( o - Plant[ i ] );
	//			o = Point( ( ( r + Plant[ i ].R ) * Plant[ i ].X + ( r + Plant[ j ].R ) * Plant[ j ].X + ( r + Plant[ k ].R ) * Plant[ k ].X ) / ( 3 * r + Plant[ i ].R + Plant[ j ].R + Plant[ k ].R ),
	//				        ( ( r + Plant[ i ].R ) * Plant[ i ].Y + ( r + Plant[ j ].R ) * Plant[ j ].Y + ( r + Plant[ k ].R ) * Plant[ k ].Y ) / ( 3 * r + Plant[ i ].R + Plant[ j ].R + Plant[ k ].R ) );
	//			Vector a, b, c;
	//			while( true )
	//			{
	//				if( Max( Abs( Plant[ i ] - o ), Abs( Plant[ j ] - o ), Abs( Plant[ k ] - o ) ) - Min( Abs( Plant[ i ] - o ), Abs( Plant[ j ] - o ), Abs( Plant[ k ] - o ) <= EPS
	//			}
	//		}
	//	}
	//}

	if( N == 1 )
	{
		Result = Plant[ 0 ].R;
	}
	else if( N == 2 )
	{
		Result = max( Plant[ 0 ].R, Plant[ 1 ].R );
	}
	else // N == 3
	{
		Result = min( min( max( Plant[ 1 ].R, ( Plant[ 2 ].R + Plant[ 0 ].R + Abs( Plant[ 2 ] - Plant[ 0 ] ) ) / 2 ),
		                   max( Plant[ 2 ].R, ( Plant[ 0 ].R + Plant[ 1 ].R + Abs( Plant[ 0 ] - Plant[ 1 ] ) ) / 2 ) ),
			   				 max( Plant[ 0 ].R, ( Plant[ 1 ].R + Plant[ 2 ].R + Abs( Plant[ 1 ] - Plant[ 2 ] ) ) / 2 ) );
	}
}

void Write( int t )
{
	printf( "Case #%d: %.9lf\n", t, Result );
}

int T;

int main()
{
	int t;
	scanf( "%d", &T );
	for( t = 0; t < T; ++t )
	{
		Read();
		Work();
		Write( t + 1 );
	}
	return 0;
}
