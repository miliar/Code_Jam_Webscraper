#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

#define INF 2000000000

using namespace std;

int P,N,m[2048],p[1024];

void Calc(int n, long long dp[]) {
    int i,j;
    long long dp1[12],dp2[12];

    for(i=0; i<12; i++)
        dp[i] = INF; 
    if(n >= N-1) {
        dp[m[n]] = 0;
        return;
    }
    Calc(n*2+1, dp1);
    Calc(n*2+2, dp2);
    for(i=0; i<12; i++)
        for(j=0; j<12; j++) {
            int k = min(i,j);
            if(k > 0)
                dp[k-1] = min(dp[k-1], dp1[i]+dp2[j]);
            dp[k] = min(dp[k], dp1[i]+dp2[j]+p[n]);
        }
}
        
int main() {
    int T,i,j,cas=1;
    long long dp[12];

    scanf("%d", &T);
    while(T--) {
        scanf("%d", &P);
        N = 1 << P;
        for(i=0; i<N; i++)
            scanf("%d", &m[i+N-1]);
        for(i=P-1; i>=0; i--)
            for(j=0; j<(1<<i); j++)
                scanf("%d", &p[j+(1<<i)-1]);
        Calc(0, dp);
        long long ans=INF;
        for(i=0; i<12; i++)
            ans = min(ans, dp[i]);
        printf("Case #%d: %lld\n", cas++, ans);
    }
    return 0;
}

