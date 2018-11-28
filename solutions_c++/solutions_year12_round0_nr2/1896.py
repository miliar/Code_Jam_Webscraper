#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

vector < int > t;

int n , s , p;

void read()
{
    scanf ( "%d%d%d" , &n , &s , &p );

    t.resize ( n );
    for (int i = 0; i < n; ++i)
    {
        scanf ( "%d" , &t[i] );
    }
}

int go ( int x )
{
    if ( x < 3 )
    {
        if ( x == 2 )
        {
            if ( 1 >= p )
                return 1;

            if ( s > 0 && 2 >= p )
            {
                --s;
                return 1;
            }
        }
        else
        {
            if ( x >= p )
                return 1;
        }
        return 0;
    }

    int mod = x % 3;
    x /= 3;

    if ( mod == 0 )
    {
        if ( x >= p )
            return 1;

        if ( s > 0 && (x + 1) >= p )
        {
            --s;
            return 1;
        }
    }
    if ( mod == 1 )
    {
        if ( x + 1 >= p )
            return 1;
    }
    if ( mod == 2 )
    {
        if ( x + 1 >= p )
            return 1;

        if ( s > 0 && (x + 2) >= p )
        {
            --s;
            return 1;
        }
    }
    return 0;
}

void solve ( int test )
{
    int i , res = 0;
    for (i = 0; i < n; ++i)
    {
        res += go ( t[i] );
    }

    printf ( "Case #%d: %d\n" , test , res );
}

int main()
{
    int t;
    scanf ( "%d" , &t );

    for (int i = 1; i <= t; ++i)
    {
        read();
        solve ( i );
    }
    return 0;
}
