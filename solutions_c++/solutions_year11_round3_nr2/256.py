#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

#define MAX 1000100

using namespace std;

typedef long long i64;

struct Pos {
    i64 l, p;
} pp[MAX];

i64 a[MAX], s[MAX];
i64 l, t, n, c;
i64 p[MAX];

bool cmp(const Pos &a, const Pos &b) {
    return a.l > b.l;
}

i64 bsearch() {
    i64 low = 1, high = n, mid, ret = -1;

    while (low <= high) {
        mid = (low + high) >> 1;
        if (s[mid] * 2 > t) {
            ret = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return ret;
}

i64 solve() {
    i64 i, k, sp = 0;
    i64 ll;
    i64 ans = 0;

    k = bsearch();
    if (k == -1) return s[n] * 2;

    for (i = k - 1; i < n; i++) {
        pp[sp].l = s[i + 1] - max(s[i], t / 2);
        pp[sp].p = i;
        sp++;
    }
    sort(pp, pp + sp, cmp);
    ll = l < sp ? l : sp;
    for (i = 0; i < ll; i++) ans += pp[i].l;

    return s[n] * 2 - ans;
}

int main() {
    int T, cnt = 1, i;

    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);

    scanf("%d", &T);
    while (T--) {
        scanf("%lld %lld %lld %lld", &l, &t, &n, &c);
        for (i = 0; i < c; i++) scanf("%lld", &a[i]);
        s[0] = 0;
        for (i = 0; i < n; i++) {
            s[i + 1] = s[i] + a[i % c];
        }
        printf("Case #%d: %lld\n", cnt++, solve());
    }

    return 0;
}
