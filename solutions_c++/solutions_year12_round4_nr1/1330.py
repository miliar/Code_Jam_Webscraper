#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int d[10010];
int l[10010];

int dp[200][200];

int
main(void)
{
    int T, N, D;
    int i, j, k, a, len;

    cin >> T;

    for(i=1;i<=T;i++) {
        cin >> N;
        d[0] = 0;
        l[0] = 0;
        for(j=1;j<=N;j++) {
            cin >> d[j] >> l[j];
        }
        cin >> D;
        d[N+1] = D;
        l[N+1] = 0;
        N++;
        memset(dp, 0, sizeof(dp));
        dp[0][1] = 1;
        
        for(j=0;j<N;j++) {
            // printf("j=%d\n", j);
            for(k=j+1;k<N;k++) {
                // printf("k=%d\n", k);
                if (dp[j][k] == 0)
                    continue;
                len = min(d[k]-d[j],l[k]);
                // printf("len=%d\n",len);
                for(a=k+1;a<=N;a++) {
                    // printf("a=%d\n", a);
                    // printf("%d,%d\n", d[k]+len,d[a]);
                    if ((d[k]+len) >= d[a]) {
                        dp[k][a] = 1;
                    }
                }
            }
        }
        // printf("here\n");
        // for(j=0;j<N;j++) {
        //     for(k=j+1;k<=N;k++) {
        //         printf("dp[%d][%d]=%d\n", j, k, dp[j][k]);
        //     }
        // }
        bool flg = false;
        for(j=0;j<N;j++) {
            // printf("j=%d\n", j);
            if (dp[j][N]) {
                flg = true;
            }
        }
        printf("Case #%d: %s\n", i, flg ? "YES" : "NO");
    }
    
    return 0;
}
