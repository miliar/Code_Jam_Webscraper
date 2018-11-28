#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <iostream>
#include <cassert>
#include <vector>
#include <set>

using namespace std;

const int nmax = 3001;

int n, m;
set < int > d[nmax];
int e[nmax];
int ans[nmax];
bool imp;

void init() {
    memset(e, -1, sizeof(e));
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; ++i) {
        d[i].clear();
        int amount;
        scanf("%d", &amount);
        for (int j = 0; j < amount; ++j) {
            int x, y;
            scanf("%d%d", &x, &y);
            if (y == 0) d[i].insert(x - 1); else e[i] = x - 1;
        }
    }
    memset(ans, 0, sizeof(ans));
}

void solve() {
    imp = false;
    while (true) {
        int bad = -2;
        for (int i = 0; i < m; ++i) {
            if (e[i] >= 0 && ans[e[i]] == 1) continue;
            if ((int)d[i].size() == 0) {
                bad = e[i];
                break;
            }
        }
        if (bad == -1) { imp = true; return; }
        if (bad == -2) break;
        ans[bad] = 1;
        for (int i = 0; i < m; ++i) {
            if (d[i].count(bad) > 0) d[i].erase(bad);
        }
    }
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testcnt;
    scanf("%d", &testcnt);
    for (int testid = 0; testid < testcnt; ++testid) {
        init();
        solve();
        printf("Case #%d:", testid + 1);
        if (imp) printf(" IMPOSSIBLE"); else {
            for (int i = 0; i < n; ++i) {
                printf(" %d", ans[i]);
            }
        }
        printf("\n");
    }

    return 0;
}
