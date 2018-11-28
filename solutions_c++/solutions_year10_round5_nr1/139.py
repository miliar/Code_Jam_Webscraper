#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <utility>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
#include <memory.h>
#include <algorithm>
using namespace std;

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )
#define pb push_back
typedef long long ll;
typedef pair<int,int> pii;

const int maxn = 1000000;
vector<int> pp;

bool u[maxn+10];
int n, k, a[17];

void primes()
{
	for ( int i=2; i<=maxn; i++ ) if ( !u[i] )
	{
		for ( ll j=(ll)i*i; j<=maxn; j+=i )
			u[j] = 1;
		pp.push_back( i );
	}
}

ll powmod( ll x, ll k, ll md )
{
	ll res = 1;
	for ( ; k>0; k>>=1 )
	{
		if ( k&1 ) res = ( res*x ) % md;
		x = ( x*x ) % md;
	}
	return res % md;
}

int solve()
{
	if ( k < 3 )
	{
		forn( i,k ) fprintf( stderr, "%d ", a[i] ); fprintf( stderr, "\n" );
		if ( k == 2 && a[0] == a[1] ) return a[0];
		return -1;
	}
	
	int mm = a[0];
	forn( i, k ) mm = max( mm, a[i] );
	
	int res = -1;
	
	ll P;
	//printf( "pp.size() = %d\n", pp.size() );
	forn( i, pp.size() )
	{
		if ( pp[i] < mm+1 ) continue;
		if ( pp[i] >= n ) break;
		P = pp[i];
		
			ll y = ( a[2] - a[1] + P ) % P;
			ll x = ( a[1] - a[0] + P ) % P;
			ll A = ( y * powmod( x, P-2, P ) ) % P;
			ll B = ( a[1] - ( A*a[0] % P ) + P ) % P;
			
			//printf( "P=%d, A=%d, B=%d\n", (int)P, (int)A, (int)B );
			
		bool ok = true;
		forn( j, k-1 )
			if ( ( A*a[j] + B ) % P != a[j+1] ) ok = false;
		
		if ( ok )
		{
			if ( res == -1 ) res = ( A*a[k-1] + B ) % P;
			else if ( res != ( A*a[k-1] + B ) % P ) return -1;				
		}
	}
	
	return res;
}

int main()
{
	primes();
	int tc;
	scanf( "%d", &tc );
	for ( int qt=1; qt<=tc; qt++ )
	{
		int D;
		scanf( "%d %d", &D, &k );
		n = 1;
		forn( q,D ) n *= 10;
		forn( i,k ) scanf( "%d", &a[i] );

		int z = solve();
		printf( "Case #%d: ", qt );
		if ( z > -1 ) printf( "%d\n", z );
		else printf( "I don't know.\n" );
	}
}
