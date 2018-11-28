#include <stdio.h>
#include <algorithm>
using namespace std;
long long mod = 100003;

long long dp[555][555];
long long c[555][555];

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    c[0][0] = c[1][0] = c[1][1] = 1;
    for(int i=2; i<=500; i++) {
        c[i][0] = 1;
        for(int j=1; j<=i; j++) {
            c[i][j] = (c[i-1][j]+c[i-1][j-1])%mod;
        }
    }

    dp[2][1] = 1;
    for(int i=3; i<=500; i++) {
        dp[i][1] = 1;
        for(int j=2; j<=i-1; j++) {
            int low = max(0,2*j-i);
            int high = j-1;
            for(int k=low; k<=high; k++) {
                dp[i][j] = (dp[i][j]+dp[j][k]*c[i-j-1][j-1-k])%mod;
            }
            //printf("%d %d %d\n", i, j, dp[i][j]);
        }
    }
    int ca;
    scanf("%d\n", &ca);
    for(int v=1; v<=ca; v++) {
        int n;
        scanf("%d", &n);
        int ret = 0;
        for(int i=1; i<n; i++) ret += dp[n][i];
        printf("Case #%d: %d\n", v, ret%mod);
    }
    return 0;
}
