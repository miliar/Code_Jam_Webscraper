#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <utility>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <map>

const int maxn = 1010000;

bool b[maxn];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    long long t, n;
    std::memset(b, true, sizeof(b));
    std::cin >> t;
    for (int i = 4; i < maxn; ++i) {
        for (int j = 2; j*j <= i; ++j) {
            if (i%j == 0) {
                b[i] = false;
                break;
            }
        }
    }
    for (int ti = 1; ti <= t; ++ti) {
        std::cin >> n;
        int ans = 0;
        for (long long i = 2; i*i <= n; ++i) {
            if (b[i]) {
                long long k = i*i;
                while (k <= n) {
                    ++ans;
                    k *= i;
                }
            }
        }
        ans += 1;
        if (n <= 2) {
            ans = 0;
        }
        std::printf("Case #%d: %d\n", ti, ans);
    }


    return 0;
}