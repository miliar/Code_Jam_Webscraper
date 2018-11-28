#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
using namespace std;

int g[40][40], dist[40], n, m;
int bit_cnt[1 << 16], max_adj;
long long adj[40];

int count_bit(long long a) {
    return bit_cnt[a & 65535] + bit_cnt[a >> 16 & 65535] + bit_cnt[a >> 32 & 65535];
}

void dfs(int dep, int v, long long path, long long mask) {
    if (dist[v] == 1) {
        max_adj = max(max_adj, count_bit(mask & ~path));
        return;
    }
    for (int i = 0; i < n; ++i) {
        if (g[v][i] && dist[v] == dist[i] + 1) {
            dfs(dep + 1, i, path | 1LL << i, mask | adj[i]);
        }
    }
}

int main() {
    bit_cnt[0] = 0;
    for (int i = 1; i < 1 << 16; ++i) {
        bit_cnt[i] = bit_cnt[i & (i - 1)] + 1;
    }

    int tot_t;
    scanf("%d", &tot_t);
    for (int cur_t = 0; cur_t < tot_t; ++cur_t) {
        scanf("%d%d", &n, &m);
        memset(g, 0, sizeof g);
        memset(adj, 0, sizeof adj);
        for (int i = 0; i < m; ++i) {
            int a, b;
            scanf("%d,%d", &a, &b);
            g[a][b] = g[b][a] = 1;
            adj[a] |= 1LL << b;
            adj[b] |= 1LL << a;
        }
        memset(dist, 0xff, sizeof dist);
        dist[1] = 0;
        queue<int> q;
        for (q.push(1); !q.empty(); q.pop()) {
            int v = q.front();
            for (int i = 0; i < n; ++i) {
                if (g[v][i] && dist[i] == -1) {
                    dist[i] = dist[v] + 1;
                    q.push(i);
                }
            }
        }
        max_adj = 0;
        dfs(0, 0, 1 << 0, adj[0]);
        printf("Case #%d: %d %d\n", cur_t + 1, dist[0] - 1, max_adj);
    }
    return 0;
}

