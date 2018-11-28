// autor: Andrzej Pezarski
// GCJ2010
// World Cup 2010

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;

int tab[3000][16];


int main() {
    int T, P, D;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        scanf("%d", &P);
        D=(1<<P);
        for (int i=2*D-1; i>=D; i--) {
            int M;
            scanf("%d", &M);
            for (int j=0; j<P-M; j++) tab[i][j]=300000000;
            for (int j=P-M; j<=P+1; j++) tab[i][j]=0;
        }
        for (int i=D-1; i>0; i--) {
            int cena;
            scanf("%d", &cena);
            for (int j=0; j<=P; j++) tab[i][j]= min (tab[2*i][j] + tab[2*i+1][j], 300000000);
            for (int j=0; j<P; j++) tab[i][j] = min (tab[i][j], tab[i][j+1] + cena);
        }
        printf("Case #%d: %d\n", t, tab[1][0]);
    }
    return 0;
}
