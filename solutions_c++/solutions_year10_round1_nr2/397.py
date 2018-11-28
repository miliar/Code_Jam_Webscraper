#include <iostream>
#include <climits>
#include <cmath>
#include <algorithm>
using namespace std;

int T, D, I, M, N;
int num[105], ans = INT_MAX;
int dp[105][256];

int best(int x, int val){
    //printf("dp(%d,%d)\n", x, val);
    if(x == -1) return 0;
    if(dp[x][val]!=-1) return dp[x][val];
    dp[x][val] = best(x-1, val) + D;
    if(abs(num[x]-val)<=M){
     //   printf("dp(%d,%d) yay\n", x, val);
        dp[x][val] = min(dp[x][val], best(x-1, num[x]));
    }
    for(int i=max(0, val-M);i<=min(255,val+M);++i) dp[x][val] = min(dp[x][val],best(x, i) + I);
    for(int i=max(0, val-M);i<=min(255,val+M);++i) dp[x][val] = min(dp[x][val],best(x-1,i) + abs(num[x]-i));
   // printf("dp(%d,%d) is %d\n", x, val, dp[x][val]);
    return dp[x][val];
}   

int main(){
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B-small.out", "w", stdout);
    scanf("%d", &T);
    for(int a=1;a<=T;++a){
        ans = INT_MAX;
        scanf("%d%d%d%d", &D, &I, &M, &N);
        for(int i=0;i<N;++i) for(int j=0;j<=255;++j) dp[i][j] = -1;
        for(int i=0;i<N;++i) scanf("%d", &num[i]);
        for(int i=0;i<=255;++i) ans = min(ans, best(N-2,i) + abs(i - num[N-1]));
        printf("Case #%d: %d\n", a, ans);
    }
  //  system("pause");
}
