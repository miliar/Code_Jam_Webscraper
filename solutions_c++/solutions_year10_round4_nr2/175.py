/**********************************************************************
Author: hanshuai
Created Time:  2010/6/5 23:17:41
File Name: b.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;
const int INF = 1000000000;
int l2[15], a[15][1005], dp[15][1005][15], p;
void update(int t1, int t2, int t3, int v){
    if(t3 < 0 || t3 > p) return;
    dp[t1][t2][t3] = min(dp[t1][t2][t3], v);
}
int main() {
    freopen("b.out", "w", stdout);
    l2[0] = 1;
    for(int i = 1; i <= 13; i ++) l2[i] = l2[i-1]*2;
    int test, cas = 0;
    scanf("%d", &test);
    while(test --){
        scanf("%d", &p);
        for(int i = p; i >= 0; i --){
            for(int j = 0; j < l2[i]; j ++){
                scanf("%d", &a[i][j]);
                for(int l = 0; l <= p; l ++) dp[i][j][l] = INF;
            }
        }
        for(int i = 0; i < l2[p]; i ++){
            dp[p][i][a[p][i]] = 0;
            for(int l = p-1; l >= 0; l --) dp[p][i][l] = min(dp[p][i][l], dp[p][i][l+1]);
        }
        for(int i = p - 1; i >= 0; i --){
            for(int j = 0; j < l2[i]; j ++){
                int t1 = j*2, t2 = t1 + 1;
                for(int l1 = 0; l1 <= p; l1 ++){
                    for(int l2 = 0; l2 <= p; l2++){
                        update(i, j, min(l1,l2)-1, dp[i+1][t1][l1]+dp[i+1][t2][l2]);
                        update(i, j, min(l1,l2), dp[i+1][t1][l1]+dp[i+1][t2][l2]+a[i][j]);
                    }
                }
                for(int l = p-1; l >= 0; l --) dp[i][j][l] = min(dp[i][j][l], dp[i][j][l+1]);
            }
        }
        int ans = INF;
        for(int i = 0; i <= p; i ++){
            ans = min(ans, dp[0][0][i]);
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}

