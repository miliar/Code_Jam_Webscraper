#include <stdio.h>

void dotest(int numtest) {
    int N;
    scanf("%d", &N);
    int dd[60000];
    int ll[60000];
    int bb[60000];
    for(int i = 0; i<N; i++) {
        scanf("%d %d", &(dd[i]), &(ll[i]));
        bb[i] = 0;
    }
    int D;
    scanf("%d", &D);
    bb[N] = 0;
    dd[N] = D;
    ll[N] = 1;
    bb[0] = dd[0];
    for(int i = 0; i<N; i++) {
        int b = bb[i];
        if (b>ll[i]) b = ll[i];
        for(int j = i+1; j<=N; j++) {
            if(dd[j]>dd[i]+b) break;
            int d = dd[j]-dd[i];
            if(bb[j]<d) bb[j] = d;
        }
    }
    if (bb[N]==0) {
        printf("Case #%d: NO\n", numtest);
    } else {
        printf("Case #%d: YES\n", numtest);
    }
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

