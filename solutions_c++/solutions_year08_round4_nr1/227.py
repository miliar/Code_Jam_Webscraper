#include <cstdio>

const int maxn = 100000;
const int inf = 0x7fffffff;

int kind[maxn], change[maxn];
int value[maxn];
int opt[maxn][2];
int n, V;

void Init() {
    int i;
    scanf("%d %d", &n, &V);
    for (i = 0; i * 2 + 1 < n; i++)
        scanf("%d %d", &kind[i], &change[i]);
    for (; i < n; i++)
        scanf("%d", &value[i]);
}

void Calc(int v) {
    if (v * 2 + 1 >= n) {
        opt[v][value[v]] = 0;
        opt[v][1 - value[v]] = inf;
        return;
    }
    Calc(v * 2 + 1);
    Calc(v * 2 + 2);
    int curr = kind[v], i, a, b, oo, now;
    opt[v][0] = opt[v][1] = inf;
    for (i = 0; i <= change[v]; i++, curr = 1 - curr)
        for (a = 0; a < 2; a++)
            if (opt[v * 2 + 1][a] < inf)
                for (b = 0; b < 2; b++)
                    if (opt[v * 2 + 2][b] < inf) {
                        now = i + opt[v * 2 + 1][a] + opt[v * 2 + 2][b];
                        oo = curr ? (a & b) : (a | b);
                        if (now < opt[v][oo]) opt[v][oo] = now;
                    }
}

void Work() {
    Calc(0);
    int ans = opt[0][V];
    if (ans < inf) printf("%d\n", ans);
    else printf("IMPOSSIBLE\n");
}

int main() {
    int t, i;
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        Init();
        Work();
    }
    return 0;
}
