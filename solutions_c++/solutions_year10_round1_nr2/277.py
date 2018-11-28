#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int ur(int a, int b)
{
    return a / b + (a % b ? 1 : 0);
}

int main()
{
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        int D, I, M, n;
        cin >> D >> I >> M >> n;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) cin >> a[i];
        vector<int> dp(256);
        for (int i = 0; i < n; ++i) {
            //cout << i << "/" << n << endl;
            vector<int> ndp(256, numeric_limits<int>::max());
            for (int j = 0; j <= 255; ++j) {
                if (i == 0 || abs(a[i] - j) <= M) {
                    // Don't change
                    ndp[a[i]] = min(ndp[a[i]], dp[j]);
                }// else if (M != 0) {
                //    int d = abs(a[i] - j);
                //    int ins = d / M + (d % M ? 1 : 0) - 1;
                    // Insert
                //    ndp[a[i]] = min(ndp[a[i]], dp[j] + ins * I);
                //}
                // Delete
                ndp[j] = min(ndp[j], dp[j] + D);
                // Modify
                if (M) {
                    for (int k = 0; k <= 255; ++k) {
                        int d = abs(j - k);
                        int ins = ur(d, M); if (ins) --ins;
                        ndp[k] = min(ndp[k], dp[j] + abs(a[i] - k) + ins * I);
                    }
                } else {
                    ndp[j] = min(ndp[j], dp[j] + abs(a[i] - j));
                }
            }
            //copy(ndp.begin(), ndp.end(), ostream_iterator<int>(cout, " ")); cout << endl;
            dp.swap(ndp);
        }
        int minval = numeric_limits<int>::max();
        for (int i = 0; i <= 255; ++i) {
            if (dp[i] < minval) {
                minval = dp[i];
            }
        }
        cout << "Case #" << (test + 1) << ": ";
        cout << minval << endl;
    }
}
