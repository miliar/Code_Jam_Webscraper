#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
#define N 500
#define Mod 100003

long long dp[510][510], ans[510], w[510][510];
int n;
void init(){
     memset(w, 0, sizeof(w));
    w[0][0] = 1;
    for (int i = 1; i <= N; ++i){
        w[i][0] = w[i][i] = 1; 
        for (int j = 1; j < i; ++j){
            w[i][j] = w[i-1][j-1] + w[i-1][j];
            w[i][j] %= Mod;
        }
    }
    memset(dp, 0, sizeof(dp));
    memset(ans, 0, sizeof(ans));
    dp[1][0] = 1;
    dp[2][1] = 1;
    ans[1] = 1; 
    ans[2] = 1;
}

void solve() {
   for (int i = 3; i <= N; ++i){
        dp[i][1] = 1;
        for (int j = 1; j < i; ++j)  {
            
            for (int k = 1; k < j; ++k){
                dp[i][j] += (dp[j][k] * w[(i-1)-(j+1)+1][(j-1)-(k+1)+1]) % Mod;
            }
            
            ans[i] += dp[i][j];
            ans[i] %= Mod;
        }
    }
}
int main(){
//    freopen("test.txt", "r", stdin);
//    freopen("c.out", "w", stdout);
    int T;
    init();
    solve();
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d", &n);
        printf("Case #%d: %I64d\n", t, ans[n]);
    }
    return 0;
}


