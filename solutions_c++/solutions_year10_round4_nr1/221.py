#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

#define MAX_N 256

int K, N;
int mat[MAX_N][MAX_N];
int goodX[MAX_N];
int goodY[MAX_N];

void read() {
    memset(mat, -1, sizeof(mat));
    scanf("%d", &K);
    for (int i = 1; i <= 2 * K - 1; ++i) {
        int pos  = (i <= K ? (K - i) : (i - K)) + 1;
        int nr  = (i <= K ? i : 2 * K - i);
        for (int j = 0; j < nr; ++j) {
            scanf("%d", &mat[i][pos + j * 2]);
        }
    }
}

int inside(int i, int j) {
    return (1 <= i && i <= 2 * K - 1 &&
            1 <= j && j <= 2 * K - 1);
}

void solve() {
/*
   printf("\n");
    for (int i = 1; i <= 10; ++i) {
        for (int j = 1; j <= 10; ++j)
            printf("%d ", mat[i][j]);
        printf("\n");
    }
*/
    memset(goodX, 0, sizeof(goodX));
    for (int x = 1; x <= 2 * K - 1; ++x) {
        goodX[x] = 1;
        for (int d = 1; d <= 2 * K - 1; ++d)
            for (int j = 1; j <= 2 * K - 1; ++j) {
                int i1 = x - d;
                int i2 = x + d;
                if (!(inside(i1, j) && inside(i2, j)))
                    continue;
                if (mat[i1][j] == -1 || mat[i2][j] == -1)
                    continue;
                if (mat[i1][j] != mat[i2][j])
                    goodX[x] = 0;
            }
    }
/*
   for (int i = 1; i <= 10; ++i)
        printf("%d ", goodX[i]);
    printf("\n");
*/
    memset(goodY, 0, sizeof(goodY));
    for (int y = 1; y <= 2 * K - 1; ++y) {
        goodY[y] = 1;
        for (int i = 1; i <= 2 * K - 1; ++i)
            for (int d = 1; d <= 2 * K - 1; ++d) {
                int j1 = y - d;
                int j2 = y + d;
                if (!(inside(i, j1) && inside(i, j2)))
                    continue;
                if (mat[i][j1] == -1 || mat[i][j2] == -1)
                    continue;
                if (mat[i][j1] != mat[i][j2])
                    goodY[y] = 0;
            }
    }
/*
   for (int i = 1; i <= 10; ++i)
        printf("%d ", goodY[i]);
    printf("\n");
*/
    int sol = 0x3f3f3f3f;
    for (int i = 1; i <= 2 * K - 1; ++i)
        for (int j = 1; j <= 2 * K - 1; ++j) {
            //printf("%d %d\n", i, j);
            if (goodX[i] && goodY[j]) {
                //printf("%d %d\n", abs(K - i), abs(K - j));
                sol = min(sol, abs(K - i) + abs(K - j));
            }
        }
    printf("%d\n", (K + sol) * (K + sol) - K * K);
}

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        read();
        printf("Case #%d: ", i);
        solve();
    }

    return 0;
}
