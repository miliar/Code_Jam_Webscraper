#include <stdio.h>
#include <algorithm>

using namespace std;

int C, c;
int sol;
int N, K;
int B, T;
int X[100], V[100], pos[100];
int sw[100], ptr;
int i, j;

int main() {

    scanf("%d", &C);
    for (c = 1; c <= C; c++) {
        scanf("%d %d %d %d", &N, &K, &B, &T);

        for (i = 0; i < N; i++)
            scanf("%d", &X[i]);

        for (i = 0; i < N; i++)
            scanf("%d", &V[i]);
        
        for (i = 0; i < N; i++)
            pos[i] = X[i] + V[i] * T;
        
        ptr = 0;
        for (i = 0; i < N; i++) {
            if (pos[i] < B) continue;           
            sw[ptr] = 0;
            for (j = i + 1; j < N; j++) {
                if (V[j] >= V[i]) continue;
                if (V[i] * X[j] - X[i] * V[j] < B * (V[i] - V[j]) && pos[j] < B) sw[ptr]++;
            }
            ptr++;
        }
        
        if (ptr == 0 && K > 0) {
            printf("Case #%d: IMPOSSIBLE\n", c);
            continue;
        }
        if (K == 0) {
            printf("Case #%d: 0\n", c);
            continue;
        }

        if (ptr < K) {
            printf("Case #%d: IMPOSSIBLE\n", c);
        } else {
            sort(sw, sw+ptr);
            sol = 0;
            for (i = 0; i < K; i++) sol += sw[i];
            printf("Case #%d: %d\n", c, sol);
        }
    }

    return 0;
}