#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int main () {
    int t;
    long R, k, N, h0, h, sum, res;
    long g[1000];

    scanf("%d", &t);
    memset(g, 0, sizeof(g));

    for (int i = 0; i < t; i++) {
        scanf("%ld %ld %ld", &R, &k, &N);
        for (int j = 0; j < N; j++){
            scanf("%ld", &g[j]);
        }
        h = 0;
        res = 0;
        for (int r = 0; r < R; r++) {
            sum = 0;
            h0 = 0;
            while (sum + g[h] <= k) {
                if (h0 == N) {
                    break;
                }
                sum += g[h];
                h++;
                if (h == N) {
                    h = 0;
                }
                h0++;
            }
            res += sum;
        }
        printf("Case #%d: %ld\n", i+1, res);
    }
    
}
