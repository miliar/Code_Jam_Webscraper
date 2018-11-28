#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

vector <int> room[10];
int clr[10], n, m, nc, nr, u[10], v[10], ans, rec[10];
bool used[10], g[10][10];

void go(int i, int j, int beg)
{
    g[i][j] = 0;
    while (1) {
        int nk = -1;
        for (int k = (j+1)%n; k != i; k = (k+1) % n) {
            if (g[j][k]) nk = k;
        }
        g[j][nk] = 0;
        if (nk == beg) break;
        room[nr].push_back(nk);
        i = j, j = nk;
    }
}

void dfs(int dep)
{
    if (dep == n) {
        for (int i = 0; i < nr; ++i) {
            memset(used, 0, sizeof(used));
            for (int j = 0; j < (int)room[i].size(); ++j) {
                used[clr[room[i][j]]] = 1;
            }
            bool fail = 0;
            for (int j = 0; !fail && j < nc; ++j) if (!used[j]) fail = 1;
            if (fail) return;
        }
//        for (int i = 0; i < n; ++i) printf("%d ", clr[i]); puts("");
        if (nc > ans) {
            ans = nc;
            for (int i = 0; i < n; ++i) rec[i] = clr[i] + 1;
        }
        return;
    }
    for (int i = 0; i < nc; ++i) {
        clr[dep] = i;
        dfs(dep+1);
    }
    clr[dep] = nc++;
    dfs(dep+1);
    --nc;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < m; ++i) scanf("%d", &u[i]);
        for (int i = 0; i < m; ++i) scanf("%d", &v[i]);
        memset(g, 0, sizeof(g));
        for (int i = 0; i < m; ++i) {
            --u[i], --v[i];
            g[u[i]][v[i]] = g[v[i]][u[i]] = 1;
        }
        for (int i = 0; i < n; ++i) g[i][(i+1)%n] = 1;
        int lim = 8;
        nr = 0;
        for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) if (g[i][j]) {
//            printf("%d %d\n", i, j);
            room[nr].clear();
            room[nr].push_back(i), room[nr].push_back(j);
            go(i, j, i);
            if ((int)room[nr].size() < lim) lim = (int)room[nr].size();
//            for (int j = 0; j < (int)room[nr].size(); ++j) printf("%d ", room[nr][j]); puts("");
            nr++;
        }
//        puts("OK");
//        for (int i = 0; i < n; ++i) lt[i].clear();
//        for (int i = 0; i < nr; ++i) {
//            for (int j = 0; j < (int)room[i].size(); ++j) {
//                lt[room[i][j]].push_back(i);
//            }
//        }
        nc = 0;
        ans = 0;
        dfs(0);
        printf("Case #%d: %d\n", cas, ans);
        for (int i = 0; i < n; ++i)
            printf("%d%c", rec[i], i == n-1 ? '\n' : ' ');
    }
    return 0;
}
