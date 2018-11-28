#include<iostream>
#include<algorithm>

using namespace std;

int iabs(int x) {
    return x > 0?x:-x;
}

int iceil(int a, int b) {
    if(b == 0) return 99999;
    if(a % b == 0) return a / b;
    else return a / b + 1;
}

int main() {
    int T, D, I, M, N, A[100];
    int dp[101][256];
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> D >> I >> M >> N;
        for(int i = 0; i < N; i++) cin >> A[i];

        for(int j = 0; j <= 255; j++) {
            dp[0][j] = 0;
        }
        for(int i = 1; i <= N; i++) {
            for(int j = 0; j <= 255; j++) {
                dp[i][j] = dp[i-1][j] + D;

                for(int k = 0; k <= 255; k++) {
                    int d = iabs(j - k);
                    if(d <= M) dp[i][j] = min(dp[i][j], dp[i-1][k] + iabs(A[i-1] - j));

                    d = iabs(A[i-1] - k);
                    if(d <= M and M > 0) dp[i][j] = min(dp[i][j], dp[i-1][k] + I * iceil(iabs(A[i-1] - j), M));
                }
            }
        }

        int M = D * N;
        for(int i = 0; i <= 255; i++) M = min(M, dp[N][i]);

        cout << "Case #" << t << ": " << M << endl;
    }
}

