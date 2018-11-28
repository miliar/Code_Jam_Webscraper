#include <iostream>
using namespace std;

int g[206], p[20006], next[20006];
int m[206], b[106][26], n, k, ans, task, tt, tot;
bool v[206];

inline bool check(int i, int j)
{
       int t;
       if (b[i][0] == b[j][0]) return 0;
       for (t = 1; t < k; ++t) {
           if (b[i][t] == b[j][t]) return 0;
           if ((b[i][t] < b[j][t]) != (b[i][0] < b[j][0]))
              return 0;
       }
       return 1;
}

inline void add(int s, int t)
{
       p[++tot] = t; next[tot] = g[s]; g[s] = tot;
}

bool dfs(int x)
{
    int i = g[x]; v[x] = 1;
    while (i) {
          if (!m[p[i]] || !v[m[p[i]]] && dfs(m[p[i]])) {
             m[x] = p[i]; m[p[i]] = x; return 1;
          }
          i = next[i];
    }
    return 0;
}

int main()
{
    freopen("c2.in", "r", stdin);
    freopen("c2.out", "w", stdout);
    scanf("%d", &task); int i, j;
    for (tt = 1; tt <= task; ++tt) {
        scanf("%d%d", &n, &k); tot = 0; ans = 0;
        memset(g, 0, sizeof(g));
        for (i = 1; i <= n; ++i)
            for (j = 0; j < k; ++j)
                scanf("%d", &b[i][j]);
        for (i = 1; i <= n; ++i)
            for (j = i + 1; j <= n; ++j)
                if (check(i, j))
                   if (b[i][0] < b[j][0]) add(i, j + n);
                   else add(j, i + n);
        memset(m, 0, sizeof(m));
        for (i = 1; i <= n; ++i) {
            memset(v, 0, sizeof(v));
            if (dfs(i)) ++ans;
        }
        printf("Case #%d: %d\n", tt, n - ans);
    }
    return 0;
}
