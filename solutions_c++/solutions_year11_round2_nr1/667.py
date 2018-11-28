/*
    2011 Round 1B -
    RPI
    by Dave Chang
*/
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;

    int T, N;
    int tab[100][100];
    int W[100], A[100];
    double WP[100], OWP[100], OOWP[100];

int main() {
    scanf("%d", &T);
    for(int z=1; z<=T; ++z) {
        scanf("%d", &N);
        memset(A, 0, sizeof(A));
        memset(W, 0, sizeof(W));
        char line[101];
        for(int i=0; i<N; ++i) {
            scanf("%s", line);
            for(int j=0; j<N; ++j)
                switch(line[j]) {
                    case '0':
                        tab[i][j] = -1;
                        break;
                    case '1':
                        tab[i][j] = 1;
                        break;
                    case '.':
                        tab[i][j] = 0;
                }
        }
        for(int i=0; i<N; ++i) {
            WP[i] = 0.0;
            for(int j=0; j<N; ++j) {
                if(tab[i][j]!=0) ++A[i];
                if(tab[i][j]==1) ++W[i];
            }
            WP[i] = (double)W[i] / A[i];
        }
        for(int i=0; i<N; ++i) {
            OWP[i] = 0.0;
            for(int j=0; j<N; ++j) {
                if(j!=i && tab[j][i]!=0) {
                    double t = W[j];
                    if(tab[j][i]==1) --t;
                    OWP[i] += t / (A[j]-1);
                    //printf("%d %d  %lf\n", i, j, t/(A[j]-1));
                }
            }
            OWP[i] /= A[i];
        }
        for(int i=0; i<N; ++i) {
            OOWP[i] = 0.0;
            for(int j=0; j<N; ++j) {
                if(j!=i && tab[j][i]!=0) {
                    OOWP[i] += OWP[j];
                }
            }
            OOWP[i] /= A[i];
        }
        printf("Case #%d:\n", z);
        for(int i=0; i<N; ++i) {
            printf("%.10lf\n", 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]);
        }
    }
    return 0;
}
