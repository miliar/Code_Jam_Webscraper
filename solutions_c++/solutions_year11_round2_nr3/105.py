#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int room[1000][10];
int size[1000];
int g[8][8], s[10], vis[10];
int n, m, totr;

void find_room(int dep) {
    for (int i = s[dep - 1] + 1; i < n; ++i) {
        if (!vis[i] && g[i][s[dep - 1]]) {
            bool ok = true;
            for (int j = 1; j < dep - 1; ++j) {
                if (g[s[j]][i]) {
                    ok = false;
                    break;
                }
            }
            if (!ok) {
                continue;
            }
 
            vis[i] = 1;
            s[dep] = i;
            if (dep >= 2 && g[s[0]][i]) {
                for (int i = 0; i <= dep; ++i) {
                    room[totr][i] = s[i];
                }
                size[totr] = dep + 1;
                ++totr;
            } else {
                find_room(dep + 1);
            }
            vis[i] = 0;
        }
    }
}

int color[10], max_color;

bool fill_color(int dep) {
    if (dep == n) {
        for (int j = 0; j < totr; ++j) { 
            int has[10] = {0}, sum = 0;
            for (int k = 0; k < size[j]; ++k) {
                if (has[color[room[j][k]]] == 0) {
                    has[color[room[j][k]]] = 1;
                    ++sum;
                }
            }
            if (sum < max_color) {
                return false;
            }
        }
        return true;
    } else {
        for (int i = 1; i <= max_color; ++i) {
            color[dep] = i;
            if (fill_color(dep + 1)) {
                return true;
            }
        }
        return false;
    }
}

int u[100], v[100];

int main() {
    int tot_t;
    scanf("%d", &tot_t);
    for (int cur_t = 0; cur_t < tot_t; ++cur_t) {
        scanf("%d%d", &n, &m);
        memset(g, 0, sizeof g);
        for (int i = 0; i < n; ++i) {
            int j = (i + 1) % n;
            g[i][j] = g[j][i] = 1;
        }
        for (int i = 0; i < m; ++i) {
            scanf("%d", &u[i]);
            --u[i];
        }
        for (int i = 0; i < m; ++i) {
            scanf("%d", &v[i]);
            --v[i];
            g[u[i]][v[i]] = g[v[i]][u[i]] = 1;
        }
        totr = 0;

        memset(room, 0, sizeof room);
        memset(size, 0, sizeof size);
        for (int i = 0; i < n; ++i) {
            memset(vis, 0, sizeof vis);
            s[0] = i;
            vis[i] = 1;
            find_room(1);
        }
        
        max_color = *max_element(size, size + totr);
        while (!fill_color(0)) {
            --max_color;
        }
        printf("Case #%d: %d\n", cur_t + 1, max_color);
        for (int i = 0; i < n; ++i) {
            printf("%d%s", color[i], i + 1 < n ? " " : "");
        }
        putchar('\n');
    }
    return 0;
}

