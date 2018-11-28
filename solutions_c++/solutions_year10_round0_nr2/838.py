#include <iostream>
#include <string>
#include <cstring>
using namespace std;

const int MAXN = 52;
/*
class bigint
{
    public:
        int len;
        int val[ MAXN ];

        bigint()
        {
            len = 1;
            memset( val, 0, sizeof( val ) );
        }
        bigint( int a )
        {
            len = 1;
            memset( val, 0, sizeof( val ) );
            ( *this ) = a;
        }
        bigint( const string &s )
        {
            len = 1;
            memset( val, 0, sizeof( val ) );
            ( *this ) = s;
        }

        bigint& operator=( int b )
        {
            if( b == 0 )
            { len = 1; val[ 0 ] = 0; return *this; }
            for( len = 0; b > 0; )
            { val[ len++ ] = b % 10; b /= 10; }
            return *this;
        }

        bigint& operator=( const string &str )
        {
            len = str.length();
            for( int k = 0; k < len; k++ )
            {
                val[ k ] = str[ len - k - 1 ] - '0';
            }
            return *this;
        }

        bigint& operator=( const bigint &b )
        {
            if( this != &b )
            {
                len = b.len;
                memcpy( val, b.val, sizeof( b.val ) );
            }
            return *this;
        }

        int comp( const bigint &b )
        {
            if( len > b.len )return 1;
            if( len < b.len )return -1;
            int k = len;
            while( k > 0 && val[ k ] == b.val[ k ] )k--;
            return val[ k ] - b.val[ k ];
        }

        const bigint operator-( const bigint &b )
        {
            int i, j;
            bigint c;

            for( i = 0, j = 0; i < len; i++ )
            {
                c.val[ i ] = val[ i ] - j;
                if( i < b.len )c.val[ i ] -= b.val[ i ];
                if( c.val[ i ] < 0 )
                {
                    j = 1;
                    c.val[ i ] += 10;
                }
                else
                    j = 0;
            }
            c.len = len;
            while( c.len > 1 && !c.val[ c.len - 1 ] )c.len--;
            return c;
        }

        const bigint operator%( const bigint &b )
        {
            int i, j;
            bigint d( 0 );
            for( i = len - 1; i >= 0; i-- )
            {
                if( !( d.len == 1 && d.val[ 0 ] == 0 ) )
                {
                    for( j = d.len - 1; j >= 0; j-- )
                        d.val[ j + 1 ] = d.val[ j ];
                    ++d.len;

                }
                d.val[ 0 ] = val[ i ];
                while( j = d.comp( b ) >= 0 )
                {
                    d = d - b;
                    if( j == 0 )
                        break;
                }
            }
            return d;
        }
};

bigint a[ MAXN ];
bigint b[ MAXN ];

bigint gcd( bigint a, bigint b )
{
    if( !( b.len == 1 && b.val[ 0 ] == 0 ) )
    {
        return gcd( b, a % b );
    }
    return a;
}

void work( int t )
{
    memset( a, 0, sizeof( a ) );
    memset( b, 0, sizeof( b ) );
    int n;
    cin >> n;
    for( int k = 0; k < n; k++ )
    {
        string now;
        cin >> now;
        a[ k ] = now;
    }

    for( int k = 1; k < n; k++ )
        b[ k ] = a[ k ].comp( a[ k - 1 ] ) > 0 ? a[ k ] - a[ k - 1 ] : a[ k - 1 ] - a[ k ];
    b[ 0 ] = a[ 0 ].comp( a[ n - 1 ] ) > 0 ? a[ 0 ] - a[ n - 1 ] : a[ n - 1 ] - a[ 0 ];

    bigint ans;
    ans = b[ 0 ];
    for( int k = 1; k < n; k++ )
        ans = gcd( ans, b[ k ] );

    bigint ans2;
    ans2 = ans - ( a[ 0 ] % ans );
    if( ( ans.len == 1 && ans.val[ 0 ] == 1 ) ) ans2 = 0;
    cout << "Case #" << t << ": ";
    for( int k = ans2.len - 1; k >= 0; k-- )
        cout << ans2.val[ k ];
    cout << endl;
}
*/

int a[ MAXN ];
int b[ MAXN ];

int gcd( int a, int b )
{
    if( b != 0 )
    {
        return gcd( b, a % b );
    }
    return a;
}

void work( int t )
{
    memset( a, 0, sizeof( a ) );
    memset( b, 0, sizeof( b ) );
    int n;
    cin >> n;

    for( int k = 0; k < n; k++ )
        cin >> a[ k ];
    b[ 0 ] = a[ 0 ] < a[ n - 1 ] ? a[ n - 1 ] - a[ 0 ] : a[ 0 ] - a[ n - 1 ];
    for( int k = 1; k < n; k++ )
        b[ k ] = a[ k ] < a[ k - 1 ] ? a[ k - 1 ] - a[ k ] : a[ k ] - a[ k - 1 ];
    int x = b[ 0 ];
    for( int k = 1; k < n; k++ )
        x = gcd( x, b[ k ] );
    int x2 = x - ( a[ 0 ] % x );
    if( x == 1 || x == x2 )x2 = 0;
    cout << "Case #" << t << ": " << x2 << endl;
}


int main()
{
    freopen ( "B-small-attempt5.in", "r" , stdin );
    freopen ( "in2.out", "w", stdout );
    int t;
    cin >> t;
    for( int k = 0; k < t; k++ )
        work( k + 1 );

    return 0;
}
