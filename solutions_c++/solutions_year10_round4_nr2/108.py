#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAX_P = 12;
const int INF = 0x3f3f3f3f;

int p, n;
int m[1 << MAX_P], cost[1 << MAX_P];

int a[1 << MAX_P][MAX_P];
bool vis[1 << MAX_P];

void doit(int node) {
    if (vis[node]) return;
    vis[node] = true;

    // last level
    if (node >= (1 << p)) {
        int team = node - (1 << p);
        for (int j = m[team]; j <= p; ++j)
            a[node][j] = 0;
        return;
    }

    // intermediate level
    int son1 = 2 * node; doit(son1);
    int son2 = 2 * node + 1; doit(son2);

    for (int j = 0; j <= p; ++j) {
        a[node][j] = min(a[node][j], a[son1][j] + a[son2][j]);

        if (j < p && a[son1][j + 1] < INF && a[son2][j + 1] < INF)
            a[node][j] = min(a[node][j], cost[node] + a[son1][j + 1] + a[son2][j + 1]);
    }
    for (int j = 0; j < p; ++j)
        a[node][j + 1] = min(a[node][j], a[node][j + 1]);
}

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    int t; scanf("%d", &t);
    for (int test_no = 1; test_no <= t; ++test_no) {
        scanf("%d", &p);

        for (int i = (1 << p) - 1; i >= 0; --i) {
            scanf("%d", &m[i]);
            m[i] = p - m[i];
        }
        for (int i = (1 << p) - 1; i > 0; --i)
            scanf("%d", &cost[i]);

        memset(vis, 0, sizeof(vis));
        memset(a, INF, sizeof(a));

        doit(1);
        printf("Case #%d: %d\n", test_no, a[1][0]);
    }
}
