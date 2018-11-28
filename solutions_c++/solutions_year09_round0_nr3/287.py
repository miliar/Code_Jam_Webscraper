#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

const int maxn = 512;
const int modu = 10000;
string p( "_welcome to code jam" );
int f[ 64 ];

void solve( int __r )
{
    string s;
    getline( cin, s );
    int n = s.size( );
    memset( f, 0, sizeof f );
    f[0] = 1;
    for( int i = 1; i < n+1; ++i )
    {
	for( int j = 1; j < p.size( ); ++j )
	{
	    if( s[i-1] == p[j] )
		f[j] = ( f[j] + f[j-1] ) % modu;
	}
    }
    printf( "Case #%d: %04d\n", __r, f[p.size()-1] );
}


int main( void )
{
    //freopen( "C-large.in", "r", stdin );
    int __t;
    cin >> __t;
    while( getchar( ) != '\n' );
    for( int i = 1; i <= __t; ++i )
	solve( i );
    return 0;
}
