#include <iostream>
#include <cstdio>
#include <cstring>

#define MAXN 110

using namespace std;

int a[MAXN], n, l, h;

bool check(const int k) {
    int i;

    for (i = 0; i < n; i++) {
        if (k % a[i] && a[i] % k) return false;
    }

    return true;
}

int solve() {
    int i;

    for (i = l; i <= h; i++) {
        if (check(i)) return i;
    }

    return -1;
}

int main() {
    int t, cnt = 1, i, ans;

    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("C-small-attempt0.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d %d %d", &n, &l, &h);
        for (i = 0; i < n; i++) scanf("%d", &a[i]);
        ans = solve();
        printf("Case #%d: ", cnt++);
        if (~ans) printf("%d\n", ans);
        else printf("NO\n");
    }

    return 0;
}
