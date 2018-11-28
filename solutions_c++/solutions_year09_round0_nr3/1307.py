#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define rep(i,n) for (int i = 0; i < n; i++)

const char *target = "welcome to code jam";

int main()
{
    int n;
    scanf("%d\n", &n);
    rep(I,n) {
        int dp[19][1000];
        memset(dp, 0, sizeof(dp));
        char in[1024];
        fgets(in, sizeof(in), stdin);
        int len = strlen(in);
        rep(i,len){
            dp[0][i+1] = dp[0][i] + (in[i] == target[0] ? 1 : 0);
            for (int j = 1; j < min(i+1,19); j++) {
                dp[j][i+1] = (dp[j][i] + (in[i] == target[j] ? dp[j-1][i] : 0)) % 10000;
            }
        }
        //rep(i, len) { rep(j,18) printf("%03d ", dp[j][i+1]); puts(""); }
        printf("Case #%d: %04d\n", I+1, dp[18][len]);
    }
    return 0;
}
