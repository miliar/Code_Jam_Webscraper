#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

#define MAX 10010

int T;
int N;
int D;
int d[MAX], l[MAX];
int dp[MAX];

int main(){
    scanf("%d",&T);
    for (int tt = 1; tt <= T; tt++){
        scanf("%d",&N);
        for (int i = 0; i < N; i++) scanf("%d%d",&d[i],&l[i]);
        scanf("%d",&D);
        dp[0] = min(l[0],d[0]);
        int runner = 0;
        for (int i = 1; i < N; i++){
            //furthest vine to the left that can reach
            while (runner < i && dp[runner] + d[runner] < d[i]) runner++;
            if (runner >= i) dp[i] = -1;
            else{
                dp[i] = min(l[i],d[i]- d[runner]);
            } 
        }
        bool can = false;
        for (int i = 0; i < N; i++){
            //printf("dp[%d]=%d d=%d D=%d\n",i,dp[i],d[i],D);
            if (dp[i] != -1 && dp[i] + d[i] >= D) can = true;
        }
        printf("Case #%d: ",tt); if (can) printf("YES\n"); else printf("NO\n");
    }
    return 0;
}