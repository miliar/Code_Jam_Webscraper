#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define rep(i,n) for( int i = 0, _n = (n); i < _n; i++ )
#define forn(i,a,b) for( int i = (a), _n = (b); i <= _n; i++ )
#define ford(i,a,b) for( int i = (a), _n = (b); i >= _n; i-- )
#define foreach(it,c) for( typeof((c).begin()) it = (c).begin(); it != (c).end(); it++ )

#define debug(x) cout << ">>" << #x << " = " << x << endl; 

#define two(x) (1<<(x))
#define contain(S,x) (((S)&two(x)) > 0)
#define twoll(x) (1LL<<(x))
#define containll(S,x) (((S)&twoll(x))>0)

int n,k;

int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );

	int ntc;
	scanf( "%d", &ntc );
	rep( T, ntc )
	{
		scanf( "%d%d", &n, &k );
		int x = two(n);
		k = k % x;
		printf( "Case #%d: ", T+1 );
		if( k == two(n)-1 ) printf( "ON\n" );
		else printf( "OFF\n" );
	}	
	return 0;
}
