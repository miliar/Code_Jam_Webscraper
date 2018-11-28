/**********************************************************************
Author: hanshuai
Created Time:  2010/5/22 9:23:01
File Name: b.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;
const int maxn = 105;
const int INF = 1000000000;
int a[maxn];
int dp[maxn][300], cur[300];
int main() {
    freopen("b.out", "w", stdout);
    int test, D, I, M, n, cas = 0;
    scanf("%d", &test);
    while(test --){
        scanf("%d%d%d%d", &D, &I, &M, &n);
        for(int i = 0; i < n; i ++) scanf("%d", &a[i]);
        for(int i = 0; i <= 255; i++){
            dp[0][i] = abs(a[0]-i);
            cur[i] = min(D, dp[0][i]);
        }
        int ans = INF;
        for(int i = 1; i < n; i ++){
            for(int j = 0; j <= 255; j ++){
                dp[i][j] = INF;
                for(int k = 0; k <= 255; k ++){
                    int v = abs(j-k);
                    if(M == 0 && v != 0) continue;
                    if(v != 0) v = (v/M+(v%M?1:0) - 1)*I;
                    dp[i][j] = min(cur[k]+v+abs(j-a[i]), dp[i][j]);
                } 
            }
            for(int j = 0; j <= 255; j ++){
                cur[j] = min(cur[j]+D, dp[i][j]);
            }
        }
        for(int j = 0; j <= 255; j ++) ans = min(ans, cur[j]);
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}

