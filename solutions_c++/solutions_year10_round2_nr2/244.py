#include <cmath>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

#define MAXN 100

int test, tests;
int n, k, b, t;
int x[MAXN];
int v[MAXN];

void solve() {
    scanf("%d%d%d%d", &n, &k, &b, &t);
    for (int i = 0; i < n; i++)
        scanf("%d", &x[i]);
    for (int i = 0; i < n; i++)
        scanf("%d", &v[i]);

    int tmp;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (x[j] > x[i]) {
                tmp = x[i]; x[i] = x[j]; x[j] = tmp;
                tmp = v[i]; v[i] = v[j]; v[j] = tmp;
            }

    int res = 0;
    int cnt = 0;
    for (int i = 0; cnt < k && i < n; i++) {
        if (v[i] * t >= b - x[i])
            cnt++;
        else
            res += (k - cnt);
    }

    printf("Case #%d: ", test);
    if (cnt < k)
        printf("IMPOSSIBLE\n");
    else
        printf("%d\n", res);
}

int main() {
    freopen("B-large.in", "rt", stdin);
    freopen("data.out", "wt", stdout);

    scanf("%d", &tests);
    for (test = 1; test <= tests; test++)
        solve();

    return 0;
}
