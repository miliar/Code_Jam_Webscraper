// autor: Andrzej Pezarski
// GCJ2010
// Rotate

#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;


char tab[100][100];


int main() {
    int T, N, K;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        scanf("%d%d", &N, &K);
        for (int n=0; n<N; n++) {
            scanf("%s", tab[n]);
            int m=N;
            for (int i=N-1; i>=0; i--) if (tab[n][i]!='.') tab[n][--m]=tab[n][i];
            for (int i=0; i<m; i++) tab[n][i]='.';
        }
        bool R=false, B=false;
        for (int i=0; i<N; i++) for (int j=0; j<N; j++) if (tab[i][j]!='.') {
            bool ti=true;
            bool tj=true;
            bool tij=true;
            bool tk=true;
            for (int k=1; k<K; k++) {
                ti = ti && i+k<N && tab[i][j]==tab[i+k][j];
                tj = tj && j+k<N && tab[i][j]==tab[i][j+k];
                tij = tij && i+k<N && j+k<N && tab[i][j]==tab[i+k][j+k];
                tk = tk && i-k>=0 && j+k<N && tab[i][j]==tab[i-k][j+k];
            }
            if (tab[i][j]=='R') R = R || ti || tj || tij || tk;
            else B = B || ti || tj || tij || tk;
        }
        printf("Case #%d: ", t);
        if (R && B) printf("Both\n");
        else if (R) printf("Red\n");
        else if (B) printf("Blue\n");
        else printf("Neither\n");
    }
    return 0;
}
