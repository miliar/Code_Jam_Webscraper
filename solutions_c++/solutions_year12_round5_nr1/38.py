#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
using namespace std;

const int MAXN = 1010;
int tot, n;
int a[MAXN], t[MAXN], ans[MAXN];

int cmp(int x, int y) {
    return (t[x] > t[y]) || (t[x] == t[y] && t[x] != 0 && a[x] < a[y]) ||
      (t[x] == t[y] && a[x] == a[y] && x < y) || 
      (t[x] == 0 && t[y] == 0 && x < y);
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &tot);
    int now = 0;
    while (now < tot) {
        ++now;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
            scanf("%d", &a[i]);
        for (int i = 0; i < n; ++i)
            scanf("%d", &t[i]);
        for (int i = 0; i < n; ++i)
            ans[i] = i;
        sort(ans, ans+n, cmp);
        printf("Case #%d:", now);
        for (int i = 0; i < n; ++i)
            printf(" %d", ans[i]);
        printf("\n");
    }
}
