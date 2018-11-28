#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

#define FI first
#define SE second
#define PB push_back
#define INF 1000000000

using namespace std;
typedef long long LL;
typedef pair<int, int> PI;

LL solve() {
    int n, k;
    LL b, t;
    scanf("%d %d %lld %lld", &n, &k, &b, &t);
    vector<LL> x(n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &x[i]);
    }
    vector<LL> v(n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &v[i]);
    }
    int ret = 0;
    int count = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (x[i] + v[i] * t < b) {
            count++;
        }
        else if (k > 0) {
            ret += count;
            k--;
        }
    }
    if (k > 0) ret = INF;
    return ret;
}

int main() {
    int te;
    scanf("%d", &te);
    for (int l = 1; l <= te; l++) {
        LL ret = solve();
        if (ret < INF)
            printf("Case #%d: %lld\n", l, ret);
        else
            printf("Case #%d: IMPOSSIBLE\n", l);
    }
}

