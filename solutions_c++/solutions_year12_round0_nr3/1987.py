#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;

int solve(int a, int b) {
    int sol = 0;
    for (int i = a; i <= b; ++i) {
        int found[10];
        memset(found, -1, sizeof found);
        int val = i;
        int cifara = int(log10(double(val)));
        int mod = int(pow(10., cifara));
        for (int j = 0; j < cifara; ++j) {
            val = (val % mod) * 10 + val / mod;
            if (val > i && val <= b) {
                bool fail = false;
                for (int k = 0; k < j - 1; ++k) {
                    if (val == found[k]) {
                        fail = true;
                    }
                }
                if (!fail) {
                    ++sol;
                    found[j] = val;
                }
            }
        }
    }
    return sol;
}

int main() {
    int tests = 0;
    scanf("%d", &tests);
    for (int t = 0; t < tests; ++t) {
        int a, b;
        scanf("%d %d", &a, &b);
        printf("Case #%d: %d\n", t + 1, solve(a, b));
    }
    return 0;
}

