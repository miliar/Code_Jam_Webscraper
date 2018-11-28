#include <cstdio>
#include <cassert>
#include <algorithm>
using namespace std;

long long DD[501][501];
long long M[501][501];
long long Micm[501][501]; // M * (c.o.m. in x dir)
long long Mjcm[501][501];

int docase() {
    int R, C, D;
    scanf("%d %d %d\n", &R, &C, &D);
    char buf[C+1];
    for (int i = 1; i <= R; ++i) {
        scanf("%s\n", buf);
        DD[i][0] = 0;
        for (int j = 0; j < C; ++j) {
            DD[i][j+1] = buf[j] - '0' + D;
        }
    }

    for (int i = 1; i <= R; ++i) {
        for (int j = 1; j <= C; ++j) {
            long long up = M[i-1][j];
            long long upleft = M[i-1][j-1];
            long long left = M[i][j-1];

            M[i][j] = DD[i][j] + up + left - upleft;
            Micm[i][j] = i*(DD[i][j]) + Micm[i-1][j] + Micm[i][j-1] - Micm[i-1][j-1];
            Mjcm[i][j] = j*(DD[i][j]) + Mjcm[i-1][j] + Mjcm[i][j-1] - Mjcm[i-1][j-1];
        }
    }

    for (int K = min(R, C); K >= 3; --K) {
        for (int i = K; i <= R; ++i) {
            for (int j = K; j <= C; ++j) { // coords of bottom right
                long long mass = M[i][j] - M[i-K][j] - M[i][j-K] + M[i-K][j-K];
                long long micm = Micm[i][j] - Micm[i-K][j] - Micm[i][j-K] + Micm[i-K][j-K];
                long long mjcm = Mjcm[i][j] - Mjcm[i-K][j] - Mjcm[i][j-K] + Mjcm[i-K][j-K];
                mass -= DD[i][j] + DD[i-K+1][j] + DD[i][j-K+1] + DD[i-K+1][j-K+1];
                micm -= i*(DD[i][j] + DD[i][j-K+1]) + (i-K+1)*(DD[i-K+1][j] + DD[i-K+1][j-K+1]);
                mjcm -= j*(DD[i][j] + DD[i-K+1][j]) + (j-K+1)*(DD[i][j-K+1] + DD[i-K+1][j-K+1]);
//                fprintf(stderr, "%d: (%d, %d) -- (%f, %f)\n", K, j, i, (double)mjcm/mass, (double)micm/mass);
                if (micm*2 == (i+i-K+1)*mass && mjcm*2 == (j+j-K+1)*mass)
                    return K;
            }
        }
    }
    return -1;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        int ans = docase();
        if (ans == -1)
            printf("Case #%d: IMPOSSIBLE\n", i);
        else
            printf("Case #%d: %d\n", i, ans);
    }
}
