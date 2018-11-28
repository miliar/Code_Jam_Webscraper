#pragma comment( linker, "/stack:128000000" )
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>

void prepare( )
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
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

const int MAXN = 1000;
const double eps = 1e-6;

int n, m;
int b, tim;
int x[MAXN];
int v[MAXN];

double get_min_time( const vector<pair< double, double> > &x )
{
	double res = 1e+10;
	int i;
	fi( sz( x ) )
	{
		double dt = ( b - x[i].first ) / x[i].second;
		res = min( res, dt );
	}
	fi( sz( x ) - 1 )
	{
		if ( x[i + 1].second + eps < x[i].second )
		{
			double dt = ( x[i + 1].first - x[i].first ) / ( x[i].second - x[i + 1].second );
			if ( dt > eps )
			{
				res = min( res, dt );
			}
		}
	}
	return res;
}

bool eq( const double &a, const double &b )
{
	return a - b < eps && b - a < eps;
}

bool test( int swaps )
{
	double ct = 0;
	int cur = 0;
	int i;
	vector<pair< double, double> > cx;
	fi( n )
	{
		cx.pb( mp( (double)x[i], (double)v[i] ) );
	}
	while ( 1 )
	{
		double t = get_min_time( cx );
		ct += t;
		if ( ct > tim + eps )
			return false;
		for ( i = sz( cx ) - 1; i >= 0; -- i )
		{
			cx[i].first += cx[i].second * t;
			if ( i + 1 < sz( cx ) )
				cx[i].first = min( cx[i].first, cx[i + 1].first );
		}
		for ( i = sz( cx ) - 1; i >= 0; -- i )
		{
			if ( cx[i].first >= b - eps )
			{
				++ cur;
				cx.pop_back( );
			}
			else
				break;
		}
		if ( cur >= m )
			return true;
		while ( 1 )
		{
			if ( swaps == 0 )
				break;
			for ( i = sz( cx ) - 1; i > 0; -- i )
			{
				double nt = ( b - cx[i].first ) / cx[i].second;
				if ( ct + nt > tim + eps )
				{
					if ( eq( cx[i].first, cx[i - 1].first ) &&
						cx[i].second < cx[i - 1].second - eps )
					{
						swap( cx[i], cx[i - 1] );
						-- swaps;
						break;
					}
				}
			}
			if ( i <= 0 )
				break;
		}
	}
}

int main( )
{
	prepare( );
	int i, j, k;
	int t, tn;
	cin >> tn;
	fr( t, tn )
	{
		scanf( "%d %d %d %d", &n, &m, &b, &tim );
		fi( n )
		{
			scanf( "%d", &x[i] );
		}
		fi( n )
		{
			scanf( "%d", &v[i] );										
		}

		int cur = 0;
		int ans = 0;
		for ( i = n - 1; i >= 0; -- i )
		{
			if ( b - x[i] > tim * v[i] )
			{
				++ cur;
			}
			else
			{
				ans += cur;
				-- m;
				if ( m == 0 )
					break;
			}
		}
		if ( m > 0 )
			ans = -1;

		if ( ans >= 0 )
			printf( "Case #%d: %d\n", t + 1, ans );
		else
			printf( "Case #%d: IMPOSSIBLE\n", t + 1 );
	}
	return 0;
}