#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;
typedef long long LL;

LL solve() {
    int r, k, n;
    scanf("%d %d %d", &r, &k, &n);
    vector<int> t(n);
    for (int i = 0; i < n; i++)
        scanf("%d", &t[i]);
    vector<int> p(n, -1);
    vector<LL> q(n, -1);
    p[0] = r;
    q[0] = 0;
    int start = 0;
    LL ret = 0;
    while (r--) {
        int kk = k;
        int j = start;
        while (kk >= t[j]) {
            kk -= t[j];
            ret += t[j];
            j = (j + 1) % n;
            if (j == start) break;
        }
        start = j;
        if (p[start] > -1) {
            int ile = p[start] - r;
            LL delta = ret - q[start];
            ret += delta * (r / ile);
            r %= ile;
        }
        else {
            p[start] = r;
            q[start] = ret;
        }
    }
    return ret;
}


int main() {
    int te;
    scanf("%d", &te);
    for (int l = 1; l <= te; l++) {
        LL ret = solve();
        printf("Case #%d: %lld\n", l, ret);
    }
}

