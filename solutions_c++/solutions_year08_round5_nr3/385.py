#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <deque>
#include <cmath>
#include <iomanip>
#include <cstdio>
#include <algorithm>
using namespace std;

#define SZ(X) (int)X.size()
#define pb(X,Y) X.push_back(Y)
#define EPS 1e-6

/*class  {
public:

};*/

int dp[10][2100];
char b[10][11];

int main() {
    int C;
    cin >> C;
    int num;
    for( num = 0; num < C; num++ ) {
        int M,N;
        cin >> M >> N;
        int i,j,k,l;
        for( i = 0; i < M; i++ ) cin >> b[i];
        memset(dp,0,sizeof(dp));
        int bound = (1 << N);
        for( i = 0; i < bound; i++ ) {
            int cnt = 0;
            bool v = true;
            bool pre = false;
            for( j = 0; j < N; j++ ) {
                if( b[M-1][j] == 'x' && (i&(1<<j)) > 0 
                ||  pre && (i & (1<<j)) > 0 ) {
                    v = false;
                    break;
                }
                else {
                    if( (i&(1<<j)) > 0 ) {
                        pre = true;
                        cnt ++;
                    }
                    else pre = false;
                }
            }
            if(v) dp[M-1][i] = cnt;
        }
        for( k = M-1; k > 0; k-- ) {
            for( i = 0; i < bound; i++ ) {
                 char tmp[11];
                 memcpy(tmp,b[k-1],sizeof(b[k-1]));
                 bool pre = false;
                 bool v = true;
                 for( l = 0; l < N; l++ ) {
                     if( b[k][l] == 'x' && (i & (1<<l) ) > 0 
                     ||  pre && (i & (1<<l)) > 0 ) {
                         v = false;
                         break;
                     }
                     else {
                         if( (i & (1<<l)) > 0 ) pre = true;
                         else pre = false;
                     }
                 } 
                 if( !v ) continue;
                 for( l = 0; l < N; l++ ) {
                     if( (i & (1<<l)) > 0 ) {
                         if( l-1 > -1 ) tmp[l-1] = 'x';
                         if( l+1 < N ) tmp[l+1] = 'x';
                     }
                 }
                 for( j = 0; j < bound; j++ ) {
                     int cnt = 0;
                     pre = false;
                     v = true;
                     for( l = 0; l < N; l++ ) {
                         if( tmp[l] == 'x' && (j & (1<<l) ) > 0 
                         ||  pre && (j & (1<<l)) > 0 ) {
                             v = false;
                             break;
                         }
                         else {
                             if( (j & (1<<l)) > 0 ) {
                                 pre = true;
                                 cnt++;
                             }
                             else pre = false;
                         }
                     }
                     if( v && dp[k][i]+cnt > dp[k-1][j] ) dp[k-1][j] = dp[k][i]+cnt;
                 }
            }
        }
        int res = 0;
        for( i = 0; i < bound; i++ ) {
            if( dp[0][i] > res ) res = dp[0][i];
        }
        printf("Case #%d: %d\n",num+1,res);
    }
    system("pause");
    return 0;
}
