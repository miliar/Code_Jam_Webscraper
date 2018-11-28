#include <cstdio>

const int MAX_N = 1024;

int n;
int a[MAX_N], b[MAX_N];

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    int t; scanf("%d", &t);
    for (int test = 1; test <= t; ++test) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
            scanf("%d %d", &a[i], &b[i]);

        int ans = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (a[i] > a[j] && b[i] < b[j])
                    ++ans;
        printf("Case #%d: %d\n", test, ans);
    }
}
