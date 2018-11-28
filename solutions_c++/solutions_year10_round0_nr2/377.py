#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

long long gcd(long long x, long long y) {
    long long t;
    if(x < y) {
        t = x;
        x = y;
        y = t;
    }
    while(y) {
        t = x;
        x = y;
        y = t % y;
    }
    return x;
}

long long a[1001];

int main() {
    int t, n;
    freopen("/home/isilme/B-small-attempt0.in", "r", stdin);
    freopen("/home/isilme/B.out", "w", stdout);
    while(cin >> t) {
        for(int i = 1; i <= t; i++) {
            cin >> n;
            for(int i = 0; i < n; i++) cin >> a[i];
            sort(a, a + n);
            long long mod;
            mod = a[1] - a[0];
            for(int i = 2; i < n; i++) {
                mod = gcd(mod, a[i] - a[i - 1]);
            }
            int ans = a[0] % mod;
            if(ans != 0) ans = -ans + mod;
            printf("Case #%d: %d\n", i, ans);
        }
    }
}
