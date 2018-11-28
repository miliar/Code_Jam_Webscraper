#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long i64;

int main() {
    int C, N, K, B, T;
    cin >> C;
    for(int t = 0; t < C; ++t) {
        cin >> N >> K >> B >> T;
        vector<i64> X(N), V(N);
        bool A[50] = {};
        for(int i = 0; i < N; ++i) {
            cin >> X[i];
        }
        for(int i = 0; i < N; ++i) {
            cin >> V[i];
        }
        for(int i = 0; i < N; ++i) {
            if(B - X[i] > V[i] * T) A[i] = true;
        }
        int cnt = 0;
        for(int i = 0; i < N; ++i) {
            if(!A[i]) ++cnt;
        }
        if(cnt < K) {
            printf("Case #%d: IMPOSSIBLE\n", t + 1);
            continue;
        }
        int ans = 0, tot = 0;
        for(int i = N-1; i >= 0 && K; --i) {
            if(A[i]) ++tot;
            else {
                ans += tot;
                --K;
            }
        }
        printf("Case #%d: %d\n", t + 1, ans);
    }
}
