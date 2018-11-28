#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;

const int N = 20;
int a[N];
int max;
int tot;

void dfs(int k, int x, int y, int sum)
{
    if (k < 0) {
        if (x == y && sum > max && sum != tot)
            max = sum;
        return;
    }
    dfs(k - 1, x ^ a[k], y, sum + a[k]);
    dfs(k - 1, x, y ^ a[k], sum);
}

int main()
{
    freopen("s.in", "r", stdin);
    freopen("s.out", "w", stdout);
    int i, n, t;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas++) {
        scanf("%d", &n);
        tot = 0;
        for (i = 0; i < n; i++) {
            scanf("%d", &a[i]);
            tot += a[i];
        }
        max = 0;
        dfs(n - 1, 0, 0, 0);
        printf("Case #%d: ", cas);
        if (max) printf("%d\n", max);
        else printf("NO\n");
    }
    return 0;
}
