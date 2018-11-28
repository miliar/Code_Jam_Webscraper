#include <iostream>
#include <cstdio>
#include <cstring>

#define MAX 110

typedef long long i64;

using namespace std;

i64 a[MAX], b[MAX];
int A[MAX], B[MAX], n, m;

i64 cnt;

i64 dfs(int x, int y, i64 pre) {
    i64 ret = 0, sum = 0, cur = 0;
    int i;

    if (x == n || y == m) return pre;
    for (i = y; i < m; ++i) {
        if (A[x] == B[i]) {
            cur = min(a[x] - sum, b[i]);
            b[i] -= cur;
            ret = max(ret, dfs(x + 1, i + (b[i] == 0), pre + cur + sum));
            b[i] += cur;
            if ((sum += b[i]) >= a[x]) break;
        }
    }
    ret = max(ret, dfs(x + 1, y, pre));

    return ret;
}

int main() {
    int t, ct = 0, i;

    //freopen("C-small-attempt1.in", "r", stdin);
    //freopen("C-small-attempt1.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d %d", &n, &m);
        for (i = 0; i < n; ++i) scanf("%lld %d", &a[i], &A[i]);
        for (i = 0; i < m; ++i) scanf("%lld %d", &b[i], &B[i]);
        cnt = 0;
        printf("Case #%d: %lld\n", ++ct, dfs(0, 0, 0));
    }

    return 0;
}
