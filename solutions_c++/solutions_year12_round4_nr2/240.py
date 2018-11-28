#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct IntInd{
    int r;
    int ind;
};

int mycomp(const void* a, const void* b) {
    return ((IntInd*)b)->r - ((IntInd*)a)->r;
}

void dotest(int numtest) {
    int N, W, L;
    scanf("%d %d %d", &N, &W, &L);
    IntInd rr[10000];
    for(int i = 0; i<N; i++) {
        scanf("%d", &(rr[i].r));
        rr[i].ind = i;
    }
    qsort(rr, N, sizeof(IntInd), mycomp);
    double xx[10000];
    double yy[10000];
    for(int i = 0; i<N; i++) {
        double x = 0;
        double y = 0;
        while(true) {
            x = rand()*1.l*W/RAND_MAX;
            y = rand()*1.l*L/RAND_MAX;
            bool ok = true;
            for(int j = 0; j<i; j++) {
                double dx = xx[j] - x;
                double dy = yy[j] - y;
                double len = sqrt(dx*dx+dy*dy);
                if (len<(rr[i].r+rr[j].r)*1.001) {
                    ok = false;
                    break;
                }
            }
            if(ok) break;
        }
        xx[i] = x;
        yy[i] = y;
    }
    double xx2[10000];
    double yy2[10000];
    for(int i = 0; i<N; i++) {
        xx2[rr[i].ind] = xx[i];
        yy2[rr[i].ind] = yy[i];
    }
    printf("Case #%d:", numtest);
    for(int i = 0; i<N; i++) {
        printf(" %.8lf %.8lf", xx2[i], yy2[i]);
    }
    printf("\n");
}

int main() {
    int T;
    scanf("%d", &T);
    for(int i = 0; i<T; i++) {
        dotest(i+1);
        fflush(stdout);
    }
    return 0;
}

