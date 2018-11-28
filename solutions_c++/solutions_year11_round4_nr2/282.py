
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

int R, C, D;
int grid[500][500];

int solve() {
    scanf("%d%d%d", &R, &C, &D);
    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
            char c = 0;
            while(c < '0' || c > '9')
                scanf("%c", &c);
            grid[i][j] = c - '0';
            //printf("%d", grid[i][j]);
        }
        //printf("\n");
    }

    int best = -1;
    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
            for(int k = 3;; k += 2) {
                int shift = k / 2;
                if(i + shift >= R || j + shift >= C)
                    break;
                if(i - shift < 0 || j - shift < 0)
                    break;
                int isum = 0, jsum = 0;
                for(int di = -shift; di <= shift; di++) {
                    for(int dj = -shift; dj <= shift; dj++) {
                        if((di == -shift || di == shift)
                                && (dj == -shift || dj == shift))
                            continue;
                        isum += di * grid[i+di][j+dj];
                        jsum += dj * grid[i+di][j+dj];
                    }
                }

                if(isum == 0 && jsum == 0) {
                    //printf("%d %d\n", isum, jsum);
                    best = max(k, best);
                }
            }
        }
    }
    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++) {
            for(int k = 4;; k += 2) {
                int shift = k / 2;
                if(i + shift >= R || j + shift >= C)
                    break;
                if(i - shift + 1 < 0 || j - shift + 1 < 0)
                    break;
                double isum = 0, jsum = 0;
                for(int di = -shift + 1; di <= shift; di++) {
                    for(int dj = -shift + 1; dj <= shift; dj++) {
                        if((di == -shift+1 || di == shift)
                                && (dj == -shift+1 || dj == shift))
                            continue;
                        isum += 1.0 * (di - 0.5) * grid[i+di][j+dj];
                        jsum += 1.0 * (dj - 0.5) * grid[i+di][j+dj];
                    }
                }

                if(fabs(isum) < 1e-5 && fabs(jsum) < 1e-5) {
                    //printf("%.10lf %.10lf\n", isum, jsum);
                    best = max(k, best);
                }
            }
        }
    }

    return best;
}

int main() {
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);

        int ans = solve();
        if(ans == -1)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }
}
