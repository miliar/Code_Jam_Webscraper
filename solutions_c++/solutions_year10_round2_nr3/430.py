#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int T, N;
    const int MOD = 100003;
    int C[51][51] = {};
    for(int i = 0; i < 51; ++i) {
        C[i][0] = 1;
        for(int j = 1; j <= i; ++j) {
            C[i][j] = (C[i-1][j-1] + C[i-1][j] ) % MOD;
        }
    }
    int F[51][51] = {};
    for(int i = 2; i < 51; ++i) {
        F[i][1] = 1;
    }
    for(int k = 3; k < 51; ++k) {
        for(int p = 1; p < k; ++p) {
            for(int l = 1; l < p; ++l) {
                F[k][p] += F[p][l] * C[k-p-1][p-l-1];
                F[k][p] %= MOD;
            }
        }
    }
    cin >> T;
    for(int t = 0; t < T; ++t) {
        cin >> N;
        int ans = 0;
        for(int i = 1; i < N; ++i) {
            ans += F[N][i];
            ans %= MOD;
        }
        printf("Case #%d: %d\n", t + 1, ans);
    }
}
