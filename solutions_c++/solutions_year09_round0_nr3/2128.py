#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#define MAXN (1 << 9)
#define MAXS (1 << 5)
#define mod 10000
using namespace std;

int t , sol, brt;
int dp[MAXN][MAXS];
//    pos , matched
string s , tar = "welcome to code jam";
vector <int> a[MAXS];
// positions

void clear ()
{
    sol = 0;
    memset (dp , 0 , sizeof(dp));
    s.clear ();
}

int main ()
{
    for (int i=0; i < tar.size(); ++i)
    {
        if ( tar[i] == ' ' ) a[27].push_back ( i+1 );
        else a[ tar[i] - 'a' ].push_back ( i+1 );
    }

    scanf ( "%d\n" , &t );
    while ( t -- )
    {
        clear ();
        // read
        getline ( cin , s );
        // solve
        for (int i=0; i < s.size(); ++i)
        {
            if ( s[i] == 'w' ) { dp[i][1] = 1; continue; } // the start
            int ind = 0;

            if ( s[i] == ' ' ) ind = 27;
            else ind = s[i] - 'a';

            for (int j=0; j < i; ++j)
            {

                for (int p=0; p < a[ind].size(); ++p)
                {
                   dp[i][ a[ind][p] ] += dp[j][ a[ind][p] -1 ];
                   dp[i][ a[ind][p] ] %= mod;
                }
            }
            /*
            for (int p=0; p < a[ind].size(); ++p)
                printf ( "dp[ %d ][ %d ] is %d\n", i , a[ind][p], dp[i][ a[ind][p] ] );

            printf ( "\n" );
            */
            sol = (sol + dp[i][19]) % mod ;
        }

        // write
        printf ( "Case #%d: ", ++brt );
        if ( sol < 1000 ) printf ( "0" );
        if ( sol < 100 ) printf ( "0" );
        if ( sol < 10 ) printf ( "0" );

        printf ( "%d\n" , sol );
    }

    return 0;
}
