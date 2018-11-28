#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int dist[40][40], adj[40][40], p, ans;
long long n[40];

void backtrack(int v, long long path, long long neighbors) {
    for(int i = 0; i < p; i++)
        if(adj[v][i] && (path & (1LL<<i)) == 0 && dist[i][1] + 1 == dist[v][1]) {
            if(i == 1) ans = max(__builtin_popcountll(neighbors | 2), ans);
            else backtrack(i, path | (1LL<<i), (neighbors | n[i]) & ~(path | (1LL<<i)));
        }
}

int main() {
    int t;
    scanf("%d", &t);

    for(int z = 1; z <= t; z++) {
        int w;
        scanf("%d %d", &p, &w);

        memset(dist, 0x3f, sizeof dist);
        memset(adj, 0, sizeof adj);
        memset(n, 0, sizeof n);
        for(int i = 0; i < p; i++)
            dist[i][i] = 0;

        for(int i = 0; i < w; i++) {
            int a, b;
            scanf("%d,%d", &a, &b);
            n[a] |= 1LL<<b;
            n[b] |= 1LL<<a;

            dist[a][b] = dist[b][a] = 1;
            adj[a][b] = adj[b][a] = 1;
        }

        for(int k = 0; k < p; k++)
            for(int i = 0; i < p; i++)
                for(int j = 0; j < p; j++)
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);

        ans = 0;
        backtrack(0, 1, n[0]);

        printf("Case #%d: %d %d\n", z, dist[0][1] - 1, ans);
        fflush(stdout);
    }
}
