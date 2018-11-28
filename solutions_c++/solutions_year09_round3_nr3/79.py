#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int rel[1000];
int memo[200][200];
int p, q;

int best(int q0, int q1) {
    if (q1-q0 == 1) {
        return 0;
    }
    if (memo[q0][q1]) {
        //printf ("best(%d,%d): %d\n", q0, q1, memo[q0][q1]);
        return memo[q0][q1];
    }


    
    int ret=(rel[q1]-rel[q0]-2);
    if (q1-q0 == 2) {
    } else {
        int min = 999999999;
        for (int i=q0+1; i<=q1-1; i++) {
            int v = best(q0, i) + best(i, q1);
            if (v < min) {
                min = v;
            }
        }
        ret += min;
    }



    memo[q0][q1] = ret;
    //printf ("best(%d,%d): %d\n", q0, q1, memo[q0][q1]);
    return ret;
}

int main() {
    int t;
    scanf("%d\n", &t);
    for (int tt=1; tt<=t; tt++) {
        scanf("%d%d", &p, &q);
        rel[0] = 0;
        for (int i=0; i<q; i++) {
            scanf("%d", &rel[i+1]);
        }
        rel[q+1] = p+1;
        memset(memo, 0, sizeof(memo));
        printf("Case #%d: %d\n", tt, best(0, q+1));
    }
}
