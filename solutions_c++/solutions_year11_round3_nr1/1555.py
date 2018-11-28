
#include <cstdlib>
#include <cstdio>
#include <cstring>

#include <cmath>

#define rep(I,N) for (int I=0; I<(N); I++)
#define rep2(I,B,E) for (int I=(B); I<=(E); I++)
#define repb(I,B,E) for (int I=(E); I>=(B); I--)

#define EPSILON 1E-6
#define eqr(A,B) (fabs( (A)-(B) ) < EPSILON)
#define ler(A,B) ( eqr(A,B) || (A)<(B) )
#define ger(A,B) ( eqr(A,B) || (A)>(B) )
#define MAXS 7

using namespace std;

int r,c;
char board[MAXS][MAXS];
char redtile[2][4] = {"/\\","\\/"};

bool replace(int i, int j) {
    rep(di,2) {
        rep(dj,2) {
            if (board[i+di][j+dj] == '#')
                board[i+di][j+dj]=redtile[di][dj];
            else
                return false;
        }
    }
    return true;
}

bool solve() {
    rep(i,r) {
        rep(j,c) {
            if (board[i][j]=='#') {
                if (!replace(i,j)) return false;
            }
        }
    }
    return true;
}

void printMat() {
    rep(i,r) {
        rep(j,c) {
            printf("%c", board[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int T;
    scanf("%i",&T);
    rep2(tc,1,T) {
        scanf("%i %i",&r,&c);
        rep(i,r) {
            scanf("%s",board[i]);
        }
        printf("Case #%i:\n", tc);
        if (solve())
            printMat();
        else
            printf("Impossible\n");
    }
}
