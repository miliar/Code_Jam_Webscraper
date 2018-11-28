#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<double> s(n);
    double M = 0;
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
        M += s[i];
    }
    vector<double> res(n);
    for (int i = 0; i < n; i++) {
        double l = 0;
        double r = 1;

        for (int it = 0; it < 40; ++it) {
            double d = (l + r) / 2;

            double sd = d;
            for (int j = 0; j < n; j++) if (j != i) {
                double dj = (s[i] - s[j]) / M + d;
                sd += max(0.0, dj);
            }

            if (sd > 1) r = d; else l = d;
        }

        res[i] = (l + r) / 2;
    }
    static int test = 0;
    cout << "Case #" << ++test << ":";
    for (int i = 0; i < n; i++)
        printf(" %.10lf", res[i] * 100);
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--)
        solve();

    return 0;
}
