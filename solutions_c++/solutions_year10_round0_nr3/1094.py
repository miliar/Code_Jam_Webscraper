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

int ne[1001];
int R, K, n, a[1001];
int mark[1001];
ll am[1001];
int tst;

void solve()
{
	scanf("%d%d%d", &R, &K, &n );
	fi( n )
		scanf("%d", a + i );
	fi( n )
	{
		ll cur = a[i];
		int id = i+1;
		id %= n;
		while ( id != i )
		{
			if ( cur + a[id] > K ) break;
			cur += a[id];
			++id;
			if ( id == n ) id = 0;
		}          
		ne[i] = id;
		am[i] = cur;
	}
	int cyc = 0;
	int cur = 0;
	CLR( mark, -1 );	
	ll tot = 0;

	if ( R <= 10000 )
	{
		ll ret = 0;
	 	cur = 0;
		fi( R )
		{
			ret += am[cur];
			cur = ne[cur];
		}
		cout << "Case #" << tst << ": " << ret << endl;
		return;
	}

	while ( 1 )
	{
		if ( mark[cur] > -1 ) 
		{
			cout << mark[cur] << ' ' << cyc << endl;
			cyc = cyc - mark[cur];
			break;
		}
		mark[cur] = cyc;
		++cyc;
		tot += am[cur];
		cur = ne[cur];				
	}

	R -= mark[cur];
	int z = R / cyc;
	ll ret = tot * (ll)z;
	R %= cyc;            
	//ll ret = 0;
	 cur = 0;
	fi( R )
	{
		ret += am[cur];
		cur = ne[cur];
	}
	cout << "Case #" << tst << ": " << ret << endl;
}

int main()
{
	initf();
	int T;
	cin >> T;
	for ( tst = 1; tst <= T; ++tst )
		solve();
	return ( 0 );
}
