#include <stdio.h>

#define MOD 100003

int counts[501][501];
int binoms[501][501];

int main() {
    for(int i = 0; i<501; i++) {
        for(int j = 0; j<501; j++) {
            counts[i][j] = 0;
            if (j==0) {
                binoms[i][j] = 1;
            } else if (i<j) {
                binoms[i][j] = 0;
            } else {
                binoms[i][j] = (binoms[i-1][j] + binoms[i-1][j-1]) % MOD;
            }
        }
    }
    counts[1][0] = 1;
    int res[501];
    for(int i = 2; i<501; i++) {
        int sum2 = 0;
        for(int j = 1; j<i; j++) {
            int sum = 0;
            for(int k = 0; k<j; k++) {
                sum += counts[j][k] * binoms[i-j-1][j-k-1];
                sum = sum%MOD;
            }
            counts[i][j] = sum;
            sum2 += sum;
            sum2 %= MOD;
        }
        //printf("%d %d\n", i, sum2);
        res[i] = sum2;
    }

    int T;
    scanf("%d", &T);
    for(int i = 0; i<T; i++) {
        int ii;
        scanf("%d", &ii);
        printf("Case #%d: %d\n", i+1, res[ii]);
    }
            
    return 0;
}
