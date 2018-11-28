#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int m[ 128 ], x[ 128 ];
char s[ 128 ];

int solve( int __r )
{
    scanf( "%s", s );
    int n = strlen( s );
    memset( m, -1, sizeof m );
    int cnt = 0;
    for( int i = 0; i < n; ++i )
    {
	if( m[s[i]] == -1 )
	{
	    if( cnt == 0 )
	    {
		m[s[i]] = 1;
		++cnt;
	    }
	    else if( cnt == 1 )
	    {
		m[s[i]] = 0;
		++cnt;
	    }
	    else
	    {
		m[s[i]] = cnt++;
	    }
	}
	x[i] = m[s[i]];
    }
    if( cnt == 1 ) cnt = 2;
    long long ret = 0, mul = 1;
    for( int i = n-1; i >= 0; --i, mul *= cnt )
	ret += x[i] * mul;
    cout << "Case #" << __r << ": " << ret << endl;
}

int main( void )
{
    freopen( "A-large.in", "r", stdin );
    int __t; cin >> __t;
    for( int i = 1; i <= __t; ++i )
	solve( i );
    return 0;
}
