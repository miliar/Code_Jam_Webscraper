/*
TASK: Theme Park
AUTHOR: Yordan Chaparov
*/

#include <iostream>
#include <cstring>
using namespace std;

int T;
int r, K, n;
int g[2048];
int ne[1024];
int s[1024];
long long sol = 0;

int main()
{
    int i, j, k;

    scanf( "%d", &T );
    for ( int ii = 1; ii <= T; ii++ )
    {
        scanf( "%d %d %d", &r, &K, &n );
        for ( i = 1; i <= n; i++ )
        {
            scanf( "%d", &g[i] );
            g[i+n] = g[i];
        }

        for ( i = 1; i <= n; i++ )
        {
            j = i;
            s[i] = 0;
            k = 0;
            while ( ( k + g[j] <= K ) && ( j < i+n ) )
            {
                k = k + g[j];
                j++;
            }
            ne[i] = j;
            if ( ne[i] > n )
                ne[i] = ne[i]-n;
            s[i] = k;
//            cout << i << " " << ne[i] << " " << s[i] << endl;
        }

        j = 1;
        sol = 0;
        for ( i = 1; i <= r; i++ )
        {
            sol = sol + s[j];
            j = ne[j];
        }
        printf( "Case #%d: ", ii );
        cout << sol << endl;
    }
    return 0;
}
