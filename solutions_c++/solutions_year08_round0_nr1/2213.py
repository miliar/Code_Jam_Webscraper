#include <stdio.h>
#include <algorithm>
#include <set>
#include <string>

#define MAXN 1024
using namespace std;
int T;

string ar[MAXN], br[MAXN];
int dp[MAXN][MAXN];
int N,M;

int solve () {
    scanf("%d\n",&M);
    for (int i=1; i<=M; i++) {
        char temp[MAXN];
        gets(temp);
        br[i] = temp;
    }
    scanf("%d\n",&N);
    for (int i=1; i<=N; i++) {
        char temp[MAXN];
        gets(temp);
        ar[i] = temp;
    }
    if (N == 0) return 0;

    for (int i=1; i<=N; i++) {
        for (int j=1; j<=M; j++) {
            if (ar[i] == br[j]) {
               dp[i][j] = MAXN;
               continue;
            }
            int k = MAXN;
            for (int p=1; p<=M; p++) {
                if (p == j) {
                   if (k > dp[i-1][p]) k = dp[i-1][p];
                } else {
                  if ( k > dp[i-1][p]+1) k = dp[i-1][p]+1;
                }
            }
            dp[i][j] = k;
        }
    }

    int mm = MAXN;
    for (int i=1; i<=M; i++) {
        if (mm > dp[N][i]) mm = dp[N][i];
    }
    return mm;
}
int main () {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    scanf("%d",&T);
    for (int t=1; t<=T; t++) {
        printf("Case #%d: %d\n",t,solve());
    }
    return 0;
}
