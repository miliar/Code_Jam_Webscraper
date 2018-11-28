#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <functional>
#include <sstream>
#include <cassert>
using namespace std;

#pragma comment(linker, "/STACK:56777216")

typedef long long LL;

#define rep(i, n) for (int i = 0; i < n; i++)
#define sz(v) (int) ((v).size())

bool dfs(int u, vector<int>* gr, int* color, int c) {
    color[u] = c;

    rep(i, sz(gr[u])) {
        int v = gr[u][i];

        if (color[v] != 0) {
            if (color[v] != c) {
                continue;
            } else {
                return false;
            }
        }

        if (!dfs(v, gr, color, c)) {
            return false;
        }
    }

    return true;
}

int main() {
#ifndef ONLINE_JUDGE
//    freopen("../DefaultProject/1.txt", "rb", stdin);
    freopen("../DefaultProject/A-large.in", "rb", stdin);
    freopen("../DefaultProject/A-large.out", "wb", stdout);
#endif

    int T;
    scanf("%d", &T);
    rep(tc, T) {
        printf("Case #%d: ", tc + 1);

        vector<int> gr[1000];
        static bool up[1000];
        int N;

        scanf("%d", &N);

        rep(i, N) {
            up[i] = true;
        }

        rep(i, N) {
            int M;
            scanf("%d", &M);
            rep(j, M) {
                int k;
                scanf("%d", &k);
                gr[i].push_back(k - 1);
                up[k - 1] = false;
            }
        }

        static int color[1000];
        memset(color, 0, sizeof(color));

        bool ok = true;
        int c = 1;
        rep(i, N) {
            if (!up[i]) continue;
            memset(color, 0, sizeof(color));

            if (dfs(i, gr, color, c)) {
                c++;
            } else {
                ok = false;
                break;
            }
        }

        puts(!ok ? "Yes" : "No");
    }

    return 0;
}
