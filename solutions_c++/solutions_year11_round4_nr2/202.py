#include <algorithm>
#include <cstdio>
#include <cassert>
#include <iostream>

using namespace std;

long long x[501][501], y[501][501], w[501][501];
long long partial_x[501][501], partial_y[501][501], partial_w[501][501];

int main() {
    int t;
    scanf("%d", &t);

    for(int z = 1; z <= t; z++) {
        int R, C, D;
        scanf("%d %d %d", &R, &C, &D);

        for(int i = 1; i <= R; i++) {
            char c[1000];
            scanf("%s", c);

            for(int j = 1; j <= C; j++) {
                w[i][j] = D + c[j-1] - '0';
                x[i][j] = w[i][j] * i;
                y[i][j] = w[i][j] * j;
            }
        }

        for(int i = 0; i <= R; i++)
            for(int j = 0; j <= C; j++) {
                partial_x[i][j] = (!i || !j) ? 0 : partial_x[i-1][j] + partial_x[i][j-1]
                    - partial_x[i-1][j-1] + x[i][j];

                partial_y[i][j] = (!i || !j) ? 0 : partial_y[i-1][j] + partial_y[i][j-1]
                    - partial_y[i-1][j-1] + y[i][j];

                partial_w[i][j] = (!i || !j) ? 0 : partial_w[i-1][j] + partial_w[i][j-1]
                    - partial_w[i-1][j-1] + w[i][j];
            }

        int ans = 0;
        for(int i = 1; i <= R; i++)
            for(int j = 1; j <= C; j++)
                for(int k = 2; k+i <= R && k+j <= C; k++) {
                    long long sum_x = partial_x[i+k][j+k] - partial_x[i-1][j+k]
                        - partial_x[i+k][j-1] + partial_x[i-1][j-1];
                    sum_x -= x[i][j] + x[i+k][j] + x[i][j+k] + x[i+k][j+k];
                    assert(sum_x >= 0);

                    long long sum_y = partial_y[i+k][j+k] - partial_y[i-1][j+k]
                        - partial_y[i+k][j-1] + partial_y[i-1][j-1];
                    sum_y -= y[i][j] + y[i+k][j] + y[i][j+k] + y[i+k][j+k];
                    assert(sum_y >= 0);

                    long long sum_w = partial_w[i+k][j+k] - partial_w[i-1][j+k]
                        - partial_w[i+k][j-1] + partial_w[i-1][j-1];
                    sum_w -= w[i][j] + w[i+k][j] + w[i][j+k] + w[i+k][j+k];
                    assert(sum_w > 0);

                    sum_x *= 2;
                    sum_y *= 2;
                    if(sum_x % sum_w || sum_y % sum_w) continue;
                    if(sum_x/sum_w != 2*i + k || sum_y/sum_w != 2*j + k) continue;

                    ans = max(ans, k+1);
                }

        if(ans == 0)
            printf("Case #%d: IMPOSSIBLE\n", z);
        else
            printf("Case #%d: %d\n", z, ans);
    }
}
