#include <iostream>
#include <cassert>

using namespace std;

int be[32][2];
int A[128];
int dp[128][128];

int main() {
    memset(be,0,sizeof(be));
    for(int i = 0; i <= 10; i++) for(int j = i; j <= 10 && j-i <= 2; j++) for(int k = j; k <= 10 && k-i <= 2; k++) {
        int r = i+j+k;
        int s = (k-i == 2);
        be[r][s] = max(be[r][s], k);
    }
    int T;
    cin >> T;
    for(int te = 1; te <= T; te++) {
        int N, S, p;
        cin >> N >> S >> p;
        for(int i = 1; i <= N; i++) cin >> A[i];
        memset(dp,-1,sizeof(dp));
        dp[0][0] = 0;
        for(int i = 1; i <= N; i++) {
            for(int j = 0; j <= S; j++) if(dp[i-1][j] != -1) {
                int nu = (be[A[i]][0] >= p);
                dp[i][j] = max(dp[i][j], dp[i-1][j] + nu);
            }
            for(int j = 1; j <= S; j++) if(dp[i-1][j-1] != -1) {
                int nu = (be[A[i]][1] >= p);
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + nu);
            }
        }
        assert(dp[N][S] != -1);
        cout << "Case #" << te << ": " << dp[N][S] << endl;
    }
    return 0;
}
