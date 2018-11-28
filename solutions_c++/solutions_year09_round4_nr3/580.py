#include <cmath>
#include <cctype>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <utility>

#define forn(a,b,c) for (int a=b; a < c; ++a)
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define set(a,b) memset ((a) , b , sizeof(a) )
#define MAXN ( 1 << 7 )
#define MAXM ( 1 << 5 )

using namespace std;

typedef pair <int , int> pii;
typedef long long ll;
typedef vector <int> vi;

int brt, sol, a[MAXN][MAXN], t, n, m, price[MAXN][MAXM];
int dp [ 1 << 16 ];

int main ()
{
    scanf ("%d" , &t );

    while ( t -- )
    {
        scanf ( "%d%d" , &n , &m );

        set ( price , 0 );
        set ( a , 0 );
        set ( dp , 0x7f );

        sol = 0;

        forn ( i , 0 , n )
            forn ( j , 0 , m )
            {
                scanf ( "%d" , &price[i][j] );
            }

        forn ( i , 0 , n )
            forn ( j , i+1 , n )
            {
                int pomal = 1, pogol = 1;
                for (int k=0; k < m; ++k)
                {
                    if ( !pomal && !pogol ) break;
                    if ( price[i][k] > price[j][k] )
                        { pomal = 0; continue; }
                    if ( price[i][k] < price[j][k] )
                        { pogol = 0; continue; }

                    if ( price[i][k] == price[j][k] )
                        { pomal = pogol = 0; break; }
                }

                if ( pomal )
                    a[j][i] = a[i][j] = 1; //a[j].pb ( i );

                if ( pogol )
                    a[i][j] = a[j][i] = 1;//a[i].pb ( j );
            }

        dp[ 0 ] = 1;
        for (int i=0; i < (1 << n); ++i)
        {
            for (int j=0; j < n; ++j)
                if ( !( i & ( 1 << j ) ) )
                {
                    int fl = 1;
                    forn (k , 0 , n)
                        if ( i & ( 1 << k ) )
                            if ( !a[j][k] )
                                { fl = 0; break; }

                    if ( fl )
                        { dp[ i + ( 1 << j ) ] = min ( dp[ i + ( 1 << j ) ], dp[ i ] ); continue; }

                    for (int mask = i; mask; mask = (mask - 1) & i )
                    {
                        int opmask = (i - mask) + ( 1 << j );

                        dp[ i + ( 1 << j )] = min ( dp[ i + ( 1 << j) ] , dp[ mask ] + dp[ opmask ] );
                    }
                    //else
                    //    dp[ i + ( 1 << j ) ] = min ( dp[ i + ( 1 << j ) ] , dp[i] + 1 );
                }
        }

        printf ("Case #%d: %d\n" ,  ++brt, dp [(1 << n) - 1] );
    }

    return 0;
}
