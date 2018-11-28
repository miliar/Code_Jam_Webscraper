#include <stdio.h>

#define STEP 510
int mass[STEP][STEP];
int sum[STEP][STEP];
int mom1[STEP][STEP];
int mom2[STEP][STEP];

void dotest(int numtest) {
    int R, C, D;
    scanf("%d %d %d", &R, &C, &D);
    char buf[1000];
    for(int i = 0; i<R; i++) {
        scanf("%s", buf);
        for(int j = 0; j<C; j++) {
            mass[i][j] = (int)(buf[j] - '0');
        }
    }
    
    for(int j = 0; j<=C; j++) {
        sum[0][j] = 0;
        mom1[0][j] = 0;
        mom2[0][j] = 0;
    }
    for(int i = 0; i<=R; i++) {
        sum[i][0] = 0;
        mom1[i][0] = 0;
        mom2[i][0] = 0;
    }
        
    for(int i = 0; i<R; i++) {
        int s = 0;
        int s1 = 0;
        int s2 = 0;
        for(int j = 0; j<C; j++) {
            s += mass[i][j];
            s1 += mass[i][j]*i;
            s2 += mass[i][j]*j;
            sum[i+1][j+1] = sum[i][j+1] + s;
            mom1[i+1][j+1] = mom1[i][j+1] + s1;
            mom2[i+1][j+1] = mom2[i][j+1] + s2;
        }
    }
    int best = 0;
    for(int i0 = 0; i0<R; i0++) {
        for(int j0 = 0; j0<C; j0++) {
            for(int s = 3; (i0+s<=R) && (j0+s<=C); s++) {
                int ms = sum[i0+s][j0+s] - sum[i0][j0+s]-sum[i0+s][j0]+sum[i0][j0] 
                    - mass[i0][j0] - mass[i0+s-1][j0] - mass[i0][j0+s-1] - mass[i0+s-1][j0+s-1];
                int mm1 = mom1[i0+s][j0+s] - mom1[i0][j0+s]-mom1[i0+s][j0]+mom1[i0][j0] 
                    - mass[i0][j0]*i0 - mass[i0+s-1][j0]*(i0+s-1) - mass[i0][j0+s-1]*i0 - mass[i0+s-1][j0+s-1]*(i0+s-1);
                int mm2 = mom2[i0+s][j0+s] - mom2[i0][j0+s]-mom2[i0+s][j0]+mom2[i0][j0] 
                    - mass[i0][j0]*j0 - mass[i0+s-1][j0]*j0 - mass[i0][j0+s-1]*(j0+s-1) - mass[i0+s-1][j0+s-1]*(j0+s-1);
                int ci2 = i0 + i0 + s-1;
                int cj2 = j0 + j0 + s-1;
                if (ci2*ms == 2*mm1 && cj2*ms == 2*mm2) {
                    if (best<s) best = s;
                }
            }
        }
    }
    
    if(best>=3) {
        printf("Case #%d: %d\n", numtest, best);
    } else {
        printf("Case #%d: IMPOSSIBLE\n", numtest, best);
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for(int i = 0; i<T; i++) {
        dotest(i+1);
    }
    return 0;
}

