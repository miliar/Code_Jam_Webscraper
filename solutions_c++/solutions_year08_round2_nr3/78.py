#include <cstdio>
#include <cstring>

#define MAXN 1048576

using namespace std;

int t[2 * MAXN], ans[MAXN];

void add(int i, int c) {
    for (i += MAXN; i >= 1; i >>= 1) {
        t[i] += c;
    }
}

int calc(int i) {
    int res = 0;
    for (i += MAXN; i >= 1; i >>= 1) {
        if (i % 2 == 1) {
            res += t[i - 1];
        }
    }
    return res;
}

int pos(int c) {
    int i = 1;
    while (i < MAXN) {
        if (c >= t[2 * i]) {
            c -= t[2 * i];
            i = 2 * i + 1;
        }
        else i = 2 * i;
    }
    return i - MAXN;
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ti = 0; ti < T; ti++) {
        int n;
        memset(t, 0, sizeof(t));
        memset(ans, 0, sizeof(ans));
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            add(i, 1);
        }

        int ind = 0;
        for (int i = 0; i < n; i++) {
            ind = pos((calc(ind) + i) % (n - i));
            ans[ind] = i + 1;
            add(ind, -1);
        }
        printf("Case #%d:", ti + 1);
        int k;
        scanf("%d", &k);
        for (int i = 0; i < k; i++) {
            int d;
            scanf("%d", &d);
            printf(" %d", ans[d - 1]);
        }
        printf("\n");
    }
    return 0;
}
