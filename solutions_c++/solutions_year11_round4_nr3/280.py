#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int p[1000005];

int main() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int tests;
    scanf("%d", &tests);
    for (int testId = 1; testId <= tests; ++testId) {
        long long x;
        cin >> x;
        if (x == 1) {
            printf("Case #%d: 0\n", testId);
            continue;
        }
        memset(p, -1, sizeof(p));
        long long r1 = 0;
        for (long long i = 2; i * i <= x; ++i) {
            if (p[i] == -1) {
                long long tmp = i * i;
                while (tmp <= x) {
                    ++r1;
                    tmp *= i;
                }
                for (long long j = i + i; j * j <= x; j += i)
                    p[j] = 0;
            }
        }
        printf("Case #%d: %lld\n", testId, r1 + 1LL);
    }
    return 0;
}
