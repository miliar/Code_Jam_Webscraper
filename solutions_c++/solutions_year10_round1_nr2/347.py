#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int D, I, M, N;

int array[300];

int table[300][300];

const int inf = 100000000;

inline int ABS(int v) { return v<0?-v:v; }

inline int cost(int from, int to) {
    if(M > 0) {
        return max(0, I * ((ABS(from - to) - 1) / M));
    } else {
        return from != to? inf: 0;
    }
}

int min_cost(int atual, int pos) {
    if(table[atual][pos] != -1) return table[atual][pos];
    if(pos == N-1) return 0;
    int resp = (N - pos - 1) * D;
    for(int j = pos + 1; j < N; ++j) {
        for(int i = 0; i < 256; ++i) {
            resp = min(resp, min_cost(i, j) + cost(atual, i) + ABS(i - array[j]) + (j - pos - 1) * D);
        }
    }
    return table[atual][pos] = resp;
}

int main(void) {
    int T;
    scanf("%d", &T);
    for(int t = 0; t < T; ++t) {
        printf("Case #%d: ", t+1);
        scanf("%d%d%d%d", &D, &I, &M, &N);
        for(int i = 0; i < N; ++i) scanf("%d", array+i);
        memset(table, -1, sizeof(table));

        int resp = D*N;
        for(int i = 0; i < N; ++i) for(int j = 0; j < 256; ++j) {
            resp = min(resp, min_cost(j, i) + D*i + ABS(j - array[i]));
        }

        printf("%d\n", resp);
    }
    return 0;
}
