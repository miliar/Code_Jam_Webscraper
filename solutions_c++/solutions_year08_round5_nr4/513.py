#include <map>
#include <set>
#include <list>
#include <stack>
#include <queue>
#include <cmath>
#include <cstdio>
#include <vector>
#include <cctype>
#include <cstdlib>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef pair<int,int> pii;

const double eps = 1e-9;
const int INF = 0x3F3F3F3F, NIL = -1;

const int MOD = 10007, MAX = 200;

int h,w,r, dp[ MAX ][ MAX ], done[ MAX ][ MAX ];
int rm[ ] = {1,2};
int cm[ ] = {2,1};

int rec( int row, int col )
{
    if(done[row][col])return dp[row][col];
    int ret = 0;
    done[row][col]=1;

    for(int i=0;i<2;i++)
    {
     int nr,nc;
     nr = row + rm[i];
     nc = col + cm[i];
     if(nr>h || nc>w)continue;
     ret += rec(nr,nc);
     ret %= MOD;
    }

    return dp[row][col] = ret;
}

int main()
{
    int cases;
    freopen( "data.txt", "r", stdin);
    freopen( "D.txt", "w", stdout );


    scanf( "%d", &cases );

    for( int cas = 1; cas <= cases ; cas ++ )
    {
        scanf( "%d %d %d", &h,&w, &r );

        memset(dp,0, sizeof (dp) );
        memset(done,0,sizeof done );

        for(int i=0;i<r;i++)
        {
            int a,b;
            scanf( "%d %d", &a, &b );
            dp[ a ][ b ] = 0;
            done[a][b] = 1;
        }

        dp[ h ][ w ] = 1;
        done[h][w]=1;

        rec( 1,1 );

        printf( "Case #%d: ", cas );

        printf( "%d\n", dp[1][1] );
    }

    return 0;
}
