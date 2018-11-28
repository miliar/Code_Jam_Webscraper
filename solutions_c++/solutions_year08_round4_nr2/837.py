#include <iostream>

using namespace std;

int main() {
    unsigned long long numTestCases;
    unsigned long long n, m, a;

    bool flag;
    cin >> numTestCases;
    for (unsigned long long i = 0; i < numTestCases; ++i) {
        cin >> n >> m >> a;
        flag = false;
        for (unsigned long long y = 1; y <= m; ++y) {
            for (unsigned long long x = 1; x <= n; ++x) {
                for (unsigned long long z = 0; z <= m; ++z) {
                    for (unsigned long long w = 0; w <= n; ++w) {
                        if ((x*z - y*w) == a) {
                            cout << "Case #" << i + 1 << ": 0 0 " << x << " " << y << " " << w << " " << z << endl;
                            flag = true;
                            break;
                        }
                    }
                    if (flag) break;
                }
                if (flag) break;
            }
            if (flag) break;
        }

        if (!flag) cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
    }

    return 0;
}
