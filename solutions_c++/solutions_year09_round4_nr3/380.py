//AlexFetisov
//Accepted
//I'm Feeling Lucky!

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:128000000")

#include <iostream>

void initf()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
}

#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <string>
#include <cmath>

using namespace std;

#define fr(i,a,b) for ( int i = ( a ); i <= ( b ); ++i)
#define fi(a) for ( int i = 0; i < ( a ); ++i)
#define fj(a) for ( int j = 0; j < ( a ); ++j)
#define fk(a) for ( int k = 0; k < ( a ); ++k)
#define CLR(a, b) memset( ( a ), ( b ), sizeof( ( a ) ) )
#define clr(a) CLR( ( a ), 0 )
#define pb push_back
#define mp make_pair
#define all( v ) ( v ).begin(),( v ).end()

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef vector < int > vi;
typedef pair < int, int > pii;

const int inf = 1 << 30;
const double eps = 1e-8;

struct tpnt
{
	double x, y;
	tpnt ( double X = 0., double Y = 0. )
	{
		x = X;
		y = Y;	
	}
};

double dst( tpnt p1, tpnt p2 )
{
	return ( hypot( p1.x - p2.x, p1.y - p2.y ) );
}


struct line
{
	double a, b, c;
	line( tpnt p1, tpnt p2 )
	{
		a = p2.y - p1.y;
		b = p1.x - p2.x;
		double d = sqrt(a * a + b * b);
		a /= d;
		b /= d;
		c = -( p1.x * a + p1.y * b );
	}
};

int lcross( line l1, line l2, tpnt & p )
{
	double d = l1.a * l2.b - l1.b * l2.a;
	double dx = l1.b * l2.c - l1.c * l2.b;
	double dy = l1.c * l2.a - l1.a * l2.c;
	if ( fabs( d ) <= eps )
	{
		if ( fabs( dx ) <= eps && fabs( dy ) <= eps ) return ( 0 );
		return ( 2 );	
	}
	p.x = dx / d;
	p.y = dy / d;
	return ( 1 );
}

bool onseg( tpnt p1, tpnt p2, tpnt p )
{
	return ( fabs( dst( p1, p2 ) - dst( p1, p ) - dst( p2, p ) ) <= eps );
}

bool eq( tpnt p1, tpnt p2 )
{
	return ( fabs( p1.x - p2.x ) <= eps && fabs( p1.y - p2.y ) <= eps );
}

bool cross( tpnt p1, tpnt p2, tpnt p3, tpnt p4 )
{
	tpnt p;
	int q = lcross(  line(p1, p2 ), line (p3, p4 ), p );
	if ( q == 2 ) return ( false );
	if ( q == 1 ) 	
	{
		//if ( ( eq( p, p1 ) || eq( p, p2 ) ) && ( eq( p, p3 ) || eq( p, p4 ) ) ) return ( false );	
		return ( onseg( p1, p2, p ) && onseg( p3, p4, p ) );
	}
	bool ok = false;
	if ( onseg( p1, p2, p3 ) || onseg( p1, p2, p4 ) ) ok = true;
	if ( onseg( p3, p4, p1 ) || onseg( p3, p4, p1 ) ) ok = true;
	return ( ok );
}

bool g[20][20];



bool good( vector < tpnt > v1, vector < tpnt > v2 )
{
	bool ok = true;
	//fi( v1.size() )
	//	if ( eq( v1[i], v2[i] ) )
	//	{
	//		ok = true;
	//		break;
	//	}	

	//if ( !ok ) return ( false );
	
		
	fi( v1.size() ) if ( i )
		fj( v2.size() ) if ( j )
			if ( cross( v1[i-1], v1[i], v2[j-1], v2[j] ) )
			{
				ok = false;
				break;
		   	}
	return ( ok );
}

bool can[1<<20];

int dp[1<<20];

int rec( int mask )
{
	if ( can[mask] ) return ( 1 );
	if ( dp[mask] != -1 ) return ( dp[mask] );
	dp[mask] = inf;
	for ( int s = mask; s > 0; s = ( mask & ( s-1 ) ) )
	{
		if ( s == mask ) continue;
		dp[mask] = min( dp[mask], rec( s ) + rec( mask - s ) ); 
  	}
  	return ( dp[mask] );
}

int n, k;

void solve()
{
	int test;
	scanf("%d", &test);
	fr(tst,1,test)
	{
		printf("Case #%d: ", tst );
		/////////////////////////////////////
		vector < tpnt > v[20];
		clr( g );
		clr( can );
		CLR( dp, -1 );
		cin >> n >> k;
		fi( n )
			fj( k )
			{
				int x;
				cin >> x;
				tpnt P = tpnt( double( j ), double( x ) );
				v[i].pb( P );
			}
		fi( n ) fj( n ) if ( i != j ) if ( good( v[i], v[j] ) ) g[i][j] = true;

		fi( 1 << n ) if ( i )
		{
			vi vec;
			fj( n ) 
			{
            	if ( ( ( 1 << j ) & i ) ) vec.pb( j );
            }
            if ( vec.size() == 1 )
            {
            	can[i] = true;
            	continue;
            }
            bool ok = true;
            fr(i1,0,vec.size()-1) fr(j1,i1+1,vec.size()-1 )
            {
            	if ( !g[vec[i1]][vec[j1]] ) 
            	{
            		ok = false;
            		break;
            	}
            }
            if ( ok )
            	can[i] = true;
		}

		printf("%d\n", rec( ( 1 << n ) - 1 ) );
	}
}

int main()
{
	initf();
	solve();
	return (0);
}