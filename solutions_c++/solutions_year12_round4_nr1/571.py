#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cstdio>

using namespace std;
const int MaxN = 10005;

int dp[MaxN];
int L[MaxN], D[MaxN];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A.txt", "w", stdout);
    int T;scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas){
        int N;scanf("%d", &N);
        for(int i = 0; i < N; ++i){
            scanf("%d%d", D + i, L + i);
        }
        int Len;scanf("%d", &Len);
        memset(dp, -1, sizeof(dp));
        dp[0] = D[0];
        for(int i = 0; i < N; ++i){
            if(dp[i] == -1) continue;
            for(int j = i + 1; j < N; ++j){
                if(dp[i] + D[i] >= D[j]){
                    dp[j] = max(dp[j], min(D[j] - D[i], L[j]));
                }
            }
        }
        int F = 0;
        for(int i = 0; i < N; ++i){
           // printf("%d %d %d\n", i, D[i], dp[i]);
            if(dp[i] != -1 && D[i] + dp[i] >= Len) {
                //printf("%d %d %d\n", i, D[i], dp[i]);
                F = 1;
            }
        }
        printf("Case #%d: ", cas);
        if(F) puts("YES");
        else puts("NO");
    }
}
