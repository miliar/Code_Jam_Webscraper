#include <cstdio>
#include <set>
using namespace std;

int a , b;
int pow10[9];

void read()
{
    scanf ( "%d%d" , &a , &b );
}

int num_digs ( int x )
{
    int digs = 0;
    while ( x )
    {
        x /= 10;
        ++digs;
    }
    return digs;
}

int go ( int x )
{
    set < int > db;
    int d = num_digs ( x );
    int tmp = x;
    int res = 0;

    for (int i = 0; i < d - 1; ++i)
    {
        int mod = tmp % 10;
        tmp /= 10;
        tmp = mod * pow10[d - 1] + tmp;

        if ( tmp > x && tmp >= ::a && tmp <= ::b && num_digs ( tmp ) == d )
        {
            if ( !db.count ( tmp ) )
            {
                db.insert ( tmp );
                ++res;
            }
        }

        //printf ( "%d --> %d\n" , x , tmp );
    }
    return res;
}

void solve ( int test )
{
    int res = 0;
    for (int i = a; i <= b; ++i)
    {
        res += go ( i );
    }

    printf ( "Case #%d: %d\n" , test , res );
}

int main()
{
    pow10[0] = 1;
    for (int i = 1; i <= 8; ++i)
        pow10[i] = pow10[i - 1] * 10;


    int t;
    scanf ( "%d" , &t );

    for (int i = 1; i <= t; ++i)
    {
        read();
        solve ( i );
    }
}
