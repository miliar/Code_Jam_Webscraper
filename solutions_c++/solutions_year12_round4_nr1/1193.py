#include <cstdio>
#include <vector>
#include <algorithm>

#define N 20000

using namespace std;

int d[N], l[N], dp[N];
bool reach[N];

bool prob(){
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n; ++i){
        scanf("%d %d", &d[i], &l[i]);
        reach[i] = false;
        dp[i] = 0;
    }
    int s;
    scanf("%d", &s);
    d[++n] = s;
    dp[n] = 0;
    reach[n] = false;
    // dp[i] = ระยะห่างมากสุดจากความสูง 0
    dp[1] = d[1];
    for(int i = 1; i < n; ++i){
        //printf("i = %d\n", i);
        for(int j = i + 1; d[i] + dp[i] >= d[j] && j <= n; ++j){
            dp[j] = max(dp[j], min(d[j] - d[i], l[j]));
            //printf("dp[%d] = %d\n", j, dp[j]);
            reach[j] = true;
        }
    }
    //printf("reach[%d] = %d\n", n, reach[n]);
    return reach[n];
}

int main(){
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i)
        printf("Case #%d: %s\n", i, prob() ? "YES" : "NO");
    return 0;
}
