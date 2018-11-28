#include <iostream>
#include <cstdio>
#include <cstring>

#define MAXV 1010
#define MAXE 1000100

using namespace std;

struct Edge {
    int ed, next;
} edge[MAXE];

int head[MAXV], nEdge, deg[MAXV];
bool vis[MAXV];

void init() {
    memset(head, -1, sizeof(head));
    nEdge = 0;
}

void addEdge(int a, int b) {
    edge[nEdge].ed = b;
    edge[nEdge].next = head[a];
    head[a] = nEdge++;
}

bool dfs(int x) {
    int i;

    if (vis[x]) return true;
    vis[x] = true;
    for (i = head[x]; ~i; i = edge[i].next) {
        if (dfs(edge[i].ed)) return true;
    }

    return false;
}

int main() {
    int t, ct = 0, n, m, i, j, a;
    bool tag;


    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        init();
        memset(deg, 0, sizeof(deg));

        scanf("%d", &n);
        for (i = 0; i < n; ++i) {
            scanf("%d", &m);
            while (m--) {
                scanf("%d", &a);
                addEdge(i, a - 1);
                ++deg[a - 1];
            }
        }
        tag = false;
        for (i = 0; i < n; ++i) {
            if (!deg[i]) {
                memset(vis, 0, sizeof(vis));
                if (dfs(i)) {
                    tag = true;
                    break;
                }
            }
        }

        printf("Case #%d: %s\n", ++ct, tag ? "Yes" : "No");
    }

    return 0;
}
