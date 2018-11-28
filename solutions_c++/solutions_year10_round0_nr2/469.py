// AlexFetisov
// Accepted

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/STACK:32000000")

#include <iostream>
#include <stdio.h>
#include <cstring>

void initf() 
{ 
	freopen( "in.txt", "r", stdin); 
	freopen( "out.txt", "w", stdout); 
}

#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>

using namespace std;

#define fr(i,a,b) for ( int i = ( a ); i <= ( b ); ++i )
#define fi( a ) for ( int i = 0; i < ( a ); ++i )
#define fj( a ) for ( int j = 0; j < ( a ); ++j )
#define fk( a ) for ( int k = 0; k < ( a ); ++k )
#define CLR( a, b ) memset( ( a ), ( b ), sizeof ( a ) )
#define clr( a ) CLR( ( a ), 0 )
#define pb push_back
#define mp make_pair
#define all( v ) ( v ).begin(), ( v ).end()

typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long ll;
typedef vector < int > vi;
typedef pair < int, int > pii;

const int inf = ( 1 << 30 );

int T;
int n;
ll t[1001];
vector < ll > v;

ll gcd( ll x, ll y )
{
	return ( y == 0 ? x : gcd( y, x % y ) );
}

void solve()
{
	cin >> T;
	fr(tst,1,T)
	{
		cout << "Case #" << tst << ": ";
		cin >> n;
		fi( n )
			cin >> t[i];
		sort( t, t + n );
		v.clear();
		fi( n ) if ( i )
			v.pb( t[i] - t[0] );
		ll gg = v[0];
		fi( v.size() ) if ( i )
			gg = gcd( gg, v[i] );
		if ( gg == 1 )
			cout << "0\n";
		else
		{
			ll ost = t[0] % gg;
			cout << ( gg - ost ) % gg << endl;
		}
	}
}

int main()
{
	initf();
	solve();
	return ( 0 );
}
