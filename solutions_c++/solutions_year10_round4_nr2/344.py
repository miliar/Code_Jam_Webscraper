
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
#define MAXM 2000
#define INF 1e9
typedef long long int Lint;

Lint dp[MAXM][2][20];
bool isfind[MAXM][2][20];
int p[MAXM], m[MAXM];
int num, P;

Lint DP( int n, int buy, int cnt )
{

	//basic
    if( n >= num ){
        if (buy == 1)
            --cnt;

        // impossible
        if ( cnt < P - m[n-num] )
            return INF;

        //ok
        else
            return 0;
    }

    //isfind
    if ( isfind[n][buy][cnt] )
        return dp[n][buy][cnt];

    //DP
    dp[n][buy][cnt] = INF;
    for (int i = 0; i < 2; i++)		//左邊選不選
        for (int j = 0; j < 2; j++)	//右邊選不選
        	dp[n][buy][cnt] = min( dp[n][buy][cnt], DP( 2*n, i, cnt + i) + DP( 2*n+1, j, cnt + j) );

    //如果選了這個node就加上cost
    if(buy == 1)
    	dp[n][buy][cnt] += p[n];

    isfind[n][buy][cnt] = true;
    return dp[n][buy][cnt];
}

int main()
{


    freopen( "test", "r", stdin );
    freopen( "out", "w", stdout );

    int c = 1, cases;

    scanf( "%d", &cases );
    while ( cases-- ){
        scanf( "%d", &P );
        num = (1 << P);

        for (int i = 0; i < num; ++i )
            scanf( "%d", &m[i] );

        for (int i = P - 1; i >= 0; i-- ){
            int subnum = (1 << i);
            for (int j = 0; j < subnum; j++ ){
                scanf( "%d", &p[subnum+j] );
            }
        }

        memset( isfind, false, sizeof( isfind ) );
        Lint ans = min( DP(1,0,0), DP(1,1,1) );
        printf( "Case #%d: %lld\n", c++,  ans);
    }
    return 0;
}



