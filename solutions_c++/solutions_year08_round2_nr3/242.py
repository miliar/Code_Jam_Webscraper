#include <cstdio>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main( void )
{
    int N;
    scanf( "%d", &N );

    for (int tc = 0; tc < N; tc++)
    {
        int K, n;
        scanf( "%d%d", &K, &n );
        vector<int> d( n );
        for (int i = 0; i < n; i++)
        {
            scanf( "%d", &d[i] );
        }

        int res[5010];
        int tmp[5010];
        int tmp2[5010];
        for (int i = 0; i < K; i++) tmp[i] = i;

        int S = K;
        for (int k = 0; k < K; k++)
        {
            int p = k % S;
            res[tmp[p]] = k+1;
            int c = 0;
            for (int i = p+1; i < S; i++) tmp2[c++] = tmp[i];
            for (int i = 0; i < p; i++) tmp2[c++] = tmp[i];
            S--;
            memcpy( tmp, tmp2, sizeof( tmp ) );
        }

        printf( "Case #%d:", tc+1 );
        for (int i = 0; i < n; i++)
        {
            printf( " %d", res[d[i]-1] );
        }
        printf( "\n" );
    }
}
