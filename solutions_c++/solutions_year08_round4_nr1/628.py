#include <algorithm>
#include <cstdio>

using namespace std;

const int inf = 9999;

void eval(int n, int* I, int* G) {
    int left = 2 * n + 1;
    int right = 2 * n + 2;
    if (G[n] == 0) {
        eval(left, I, G);
        eval(right, I, G);
        I[n] = max(I[left], I[right]);
    } else if (G[n] == 1) {
        eval(left, I, G);
        eval(right, I, G);
        I[n] = min(I[left], I[right]);
    }
}

int calc(int n, int v, int* I, int* G, int* C) {
    int left = 2 * n + 1;
    int right = 2 * n + 2;
    if (I[n] == v) {
        return 0;
    } else if (G[n] == -1) {
        return inf;
    } else {
        int l0 = calc(left, 0, I, G, C);
        int l1 = calc(left, 1, I, G, C);
        int r0 = calc(right, 0, I, G, C);
        int r1 = calc(right, 1, I, G, C);
        int res = inf;
        if (v == 0) {
            res <?= l0 + r0;
            if (G[n] == 1) {
                res <?= l0 + r1;
                res <?= l1 + r0;
            }
        } else {
            res <?= l1 + r1;
            if (G[n] == 0) {
                res <?= l0 + r1;
                res <?= l1 + r0;
            }
        }
        if (C[n] == 1) {
            if (v == 0) {
                res <?= l0 + r0 + 1;
                if (G[n] == 0) {
                    res <?= l0 + r1 + 1;
                    res <?= l1 + r0 + 1;
                }
            } else {
                res <?= l1 + r1 + 1;
                if (G[n] == 1) {
                    res <?= l0 + r1 + 1;
                    res <?= l1 + r0 + 1;
                }
            }
        }
        return res;
    }
}

int main() {
    int N;
    scanf("%d", &N);
    for (int c = 1; c <= N; c ++) {
        int M, V;
        scanf("%d %d", &M, &V);
        int I[M], G[M], C[M];
        for (int i = 0; i < (M - 1) / 2; i ++) {
            scanf("%d %d", G + i, C + i);
        }
        for (int i = (M - 1) / 2; i < M; i ++) {
            scanf("%d", I + i);
            G[i] = -1;
        }
        eval(0, I, G);
        int res = calc(0, V, I, G, C);
        if (res < inf) {
            printf("Case #%d: %d\n", c, res);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", c);
        }
    }
    return 0;
}
