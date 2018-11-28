#include <cstdio>
#include <iostream>
using namespace std;
#define N 500
#define M 100003
typedef long long llt;
llt dp[510][510], ans[510], c[510][510];
void solve() {
    memset(c, 0, sizeof(c));
    c[0][0] = 1;
    for (int i = 1; i <= N; ++i){
        c[i][0] = c[i][i] = 1; 
        for (int j = 1; j < i; ++j){
            c[i][j] = c[i-1][j-1] + c[i-1][j];
            c[i][j] %= M;
        }
    }
    memset(dp, 0, sizeof(dp));
    memset(ans, 0, sizeof(ans));
    
    dp[1][0] = 1;
    dp[2][1] = 1;
    ans[1] = 1; 
    ans[2] = 1;
    for (int i = 3; i <= N; ++i){
        dp[i][1] = 1;
        for (int j = 1; j < i; ++j)  {
            
            for (int k = 1; k < j; ++k){
                dp[i][j] += dp[j][k] * c[(i-1)-(j+1)+1][(j-1)-(k+1)+1];
                dp[i][j] %= M;
            }
            
            ans[i] += dp[i][j];
            ans[i] %= M;
        }
    }
}
int main(){
    freopen("cl.in", "r", stdin);
    freopen("cl.out", "w", stdout);
    int n, T;
    solve();
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d", &n);
        printf("Case #%d: %I64d\n", t, ans[n]);
    }
    return 0;
}
