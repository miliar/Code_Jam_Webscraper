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
int n, K;

void solve()
{
	cin >> T;
	fk( T )
	{
		cout << "Case #" << k + 1 << ": ";
		cin >> n >> K;
		int mask = ( 1LL << n ) - 1;
		if ( ( K & mask ) == mask )
			cout << "ON\n";
		else
			cout << "OFF\n";
	}
}

int main()
{
	initf();
	solve();
	return ( 0 );
}
