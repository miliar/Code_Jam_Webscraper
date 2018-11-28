#include <iostream>

#include "BigIntegerLibrary.hh"

using namespace std;

#define MAXN 1200

BigUnsigned t[ MAXN ];

int main()
{
   // freopen( "in2.txt", "rt", stdin );

    int tests;
    cin >> tests;
    for( int test = 1; test <= tests; ++ test )
    {
        int n;
        cin >> n;
        for( int i = 0; i != n; ++ i )
        {
            char buf[ 128 ];
            cin >>  buf;
            t[i] = stringToBigUnsigned( buf );
        }

        for( int i = 1; i < n; ++ i )
        {
            if( t[0] > t[i] )
            {
                BigUnsigned z = t[0];
                t[0] = t[i];
                t[i] = z;
            }
        }

        for( int i = 1; i < n; ++ i )
            t[i] -= t[0];

        BigUnsigned d = t[1];
        for( int i = 2; i < n; ++ i )
            d = gcd( d, t[i] );

        BigUnsigned ans = t[0]%d;
        if( ans > 0 )
            ans = d - ans;
        cout << "Case #" << test <<": "<< ans << std::endl;
    }

    return 0;
}