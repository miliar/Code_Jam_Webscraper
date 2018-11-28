#include <iostream>
using namespace std;

int p;
int m[1024], c[2048], f[2049][11], level[11];

inline int max(int x, int y)
{
       return x > y ?x :y;
}

inline int min(int x, int y)
{
       return x < y ?x :y;
}

int main()
{
    freopen("b2.in", "r", stdin);
    freopen("b.out", "w", stdout);
    
    int task; scanf("%d", &task);
    for (int tt = 1; tt <= task; ++tt) {
    
    scanf("%d", &p);
    for (int i = 0; i < (1 << p); ++i) {
        scanf("%d", &m[i]); m[i] = p - m[i];
    }
    for (int i = p; i; --i) {
        level[i] = 1 << (i - 1);
        for (int j = 0; j < (1 << (i - 1)); ++j)
            scanf("%d", &c[level[i] + j]);
    }
    memset(f, 127, sizeof(f));
    for (int i = 0; i < (1 << p); i += 2) {
        int k = max(m[i], m[i + 1]);
        f[level[p] + (i >> 1)][max(k - 1, 0)] = c[level[p] + (i >> 1)];
        f[level[p] + (i >> 1)][k] = 0;
    }
    for (int i = p; i; --i)
        for (int j = 0; j < (1 << (i - 1)); j += 2) {
            int p1 = level[i] + j, p2 = level[i] + j + 1;
            for (int k = 0; k <= p; ++k)
                if (f[p1][k] <= 1000000000)
                   for (int t = 0; t <= p; ++t)
                       if (f[p2][t] <= 1000000000) {
                          int w = max(k, t);
                          f[p1 >> 1][w] = min(f[p1 >> 1][w], f[p1][k] + f[p2][t]);
                          f[p1 >> 1][max(w - 1, 0)] = min(f[p1 >> 1][max(w - 1, 0)], f[p1][k] + f[p2][t] + c[p1 >> 1]);
                       }
    }
    printf("Case #%d: %d\n", tt, f[1][0]);
    }
    return 0;
}
