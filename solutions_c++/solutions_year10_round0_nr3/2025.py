// autor: Andrzej Pezarski
// GCJ2010
// Theme Park

#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;


int main() {
    int T, R, K, N;
    int G[1100];
    int next[1100];
    long long val[1100];
    int tnext[1100];
    long long tval[1100];
    int wnext[1100];
    long long wval[1100];
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        scanf("%d%d%d", &R, &K, &N);
        for (int n=0; n<N; n++) scanf("%d", G+n);

        for (int n=0, m=0, s=0; n<N; n++) {
            while (m<N && s+G[(n+m)%N]<=K) {
                s+=G[(n+m)%N];
                m++;
            }
            next[n]=(n+m)%N;
            val[n]=s;
            m=max(0, m-1);
            s=max(0, s-G[n]);
        }

        for (int n=0; n<N; n++) {
            wnext[n]=n;
            wval[n]=0;
        }
        for (int i=(1<<30); i; i>>=1) {
            for (int n=0; n<N; n++) {
                tnext[n]=wnext[wnext[n]];
                tval[n]=wval[n]+wval[wnext[n]];
            }
            for (int n=0; n<N; n++) {
                wnext[n]=tnext[n];
                wval[n]=tval[n];
            }

            if (R&i) {
                for (int n=0; n<N; n++) {
                    tnext[n]=next[wnext[n]];
                    tval[n]=wval[n]+val[wnext[n]];
                }
                for (int n=0; n<N; n++) {
                    wnext[n]=tnext[n];
                    wval[n]=tval[n];
                }
            }
        }

        printf("Case #%d: %lld\n", t, wval[0]);
    }
    return 0;
}
