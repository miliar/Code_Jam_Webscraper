#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int K = 1; K <= T; ++K) {
        int n;
        cin >> n;
        vector<int> d(n + 2);
        vector<int> l(n + 2);
        for (int i = 1; i <= n; ++i) {
            cin >> d[i] >> l[i];
        }
        d[0] = 0;
        l[0] = 0;

        int D;
        cin >> D;
        d[n + 1] = D;
        l[n + 1] = 0;

        vector<int> min_win(n + 2, D);
        min_win[n + 1] = D;

        // printf("Case #%d:\n", K);
        for (int i = n + 1; i >= 0; --i) {
            // printf("i = %d, min_win = %d\n", i, min_win[i]);

            for (int j = i - 1; j >= 0; --j) {

                int length = min(d[i] - d[j], l[i]);
                int good_dist = d[i] + length;
                // printf("j = %d, length = %d, good_dist = %d\n", j, length, good_dist);

                if (min_win[i] <= good_dist) {
                    min_win[j] = d[i];
                }
            }
            
        }

        bool res = min_win[0] <= d[1];
        printf("Case #%d: %s\n", K, res ? "YES" : "NO");
    }
}
