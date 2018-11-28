#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <iomanip>
#include <math.h>
#include <string>
#include <string.h>
using namespace std;

#define pii pair<int,int>
#define mk make_pair

typedef long long ll;

const int maxn = 505;

int h,w,d;
ll mat[maxn][maxn];

char buff[maxn];

ll dpr[maxn][maxn];
ll dpc[maxn][maxn];
ll dp[maxn][maxn];

ll ss( ll dp[maxn][maxn], int r1, int r2, int c1, int c2 ){
    ll ret = dp[r2][c2];
    if( c1 && r1 ) ret += dp[r1-1][c1-1];
    if( c1 ) ret -= dp[r2][c1-1];
    if( r1 ) ret -= dp[r1-1][c2];
    return ret;
}

const double eps = 1e-9;

int main(){
    freopen("Ulaz.txt","r",stdin);
    freopen("Izlaz.txt","w",stdout);

    int tests; scanf("%d",&tests);

    for( int t = 1; t <= tests; ++ t){
        scanf("%d%d%d",&h,&w,&d);


        for( int i = 0; i < h; ++i ){
            scanf("%s",buff);
            for( int j = 0; j < w; ++j ){
                mat[i][j] = buff[j] - '0';
                mat[i][j] += d;
            }
        }

        for( int c = 0; c < w; ++c ){
            for( int r = 0; r < h; ++r ){
                dp[r][c] = mat[r][c];
                dpr[r][c] = r*mat[r][c];
                dpc[r][c] = c*mat[r][c];
                if( r ){
                    dp[r][c] += dp[r-1][c];
                    dpr[r][c] += dpr[r-1][c];
                    dpc[r][c] += dpc[r-1][c];
                }
            }
        }

        for( int r = 0; r < h; ++r )
            for( int c = 1; c < w; ++c )
                dp[r][c] += dp[r][c-1], dpr[r][c] += dpr[r][c-1], dpc[r][c] += dpc[r][c-1];


        int sol = 0;
        int T =min(h,w);
        for( int k = 3; k <= T; ++k ){
            for( int r = 0; r+k <= h; ++r ){
                for( int c = 0; c+k <= w; ++c ){
                    int r1 = r + k - 1;
                    int c1 = c + k - 1;

                    ll corner = mat[r][c] + mat[r1][c1] + mat[r1][c] + mat[r][c1];
                    ll RSUM = ss( dpr , r , r1, c , c1 );
                    ll CSUM = ss( dpc , r , r1, c , c1 );
                    ll SUM  = ss( dp , r , r1 , c , c1 );
                    RSUM -= mat[r][c]*r + mat[r1][c1]*r1 + mat[r1][c]*r1 + r*mat[r][c1];
                    CSUM -= mat[r][c]*c + mat[r1][c1]*c1 + mat[r1][c]*c + c1*mat[r][c1];
                    SUM -= corner;


                    double rc = (r+r1)/2.0, cc = (c+c1) /2.0;

                    double R = RSUM - rc * SUM;
                    double C = CSUM - cc * SUM;

                    if( fabs(R-C) < eps && fabs(R-0) < eps ) sol = max( sol , k );
                }
            }
        }


        if( sol ) printf("Case #%d: %d\n",t,sol);
        else printf("Case #%d: IMPOSSIBLE\n",t);
    }


    return 0;
}
