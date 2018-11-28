#include <cstdio>
#include <cstring>

using namespace std;

char M[150][150];
int alt[150][150];
int T;
int lins, cols;
char letra;

char colore(int i, int j) {
    if (M[i][j] != 0)
        return M[i][j];
    int opc1, opc2, opc3, opc4;
    opc1 = i > 0 ? alt[i-1][j] : 0x7fffffff;
    opc2 = j > 0 ? alt[i][j-1] : 0x7fffffff;
    opc3 = i < lins-1 ? alt[i+1][j] : 0x7fffffff;
    opc4 = j < cols-1 ? alt[i][j+1] : 0x7fffffff;
    int best = 0x7fffffff;
    if (opc1 < best) best = opc1;
    if (opc2 < best) best = opc2;
    if (opc4 < best) best = opc4;
    if (opc3 < best) best = opc3;
    if (best >= alt[i][j]) {
        char x = letra;
        letra++;
        return x;
    }

    if (best == opc1) return M[i-1][j] = colore(i-1,j);
    if (best == opc2) return M[i][j-1] = colore(i,j-1);
    if (best == opc4) return M[i][j+1] = colore(i,j+1);
    if (best == opc3) return M[i+1][j] = colore(i+1,j);
}

int main() {

    int C = 1;

    scanf("%d",&T);
    while (T--) {
        printf("Case #%d:\n",C++);
        scanf("%d %d",&lins,&cols);
        for (int i=0;i<lins+3;i++)
            memset(M[i],0,(cols+3)*sizeof(char));
        letra='a';
        for (int i=0;i<lins;i++)
            for (int j=0;j<cols;j++)
                scanf("%d",&alt[i][j]);
        for (int i=0;i<lins;i++)
            for (int j=0;j<cols;j++)
                if (M[i][j] == 0)
                    M[i][j] = colore(i,j);
        for (int i=0;i<lins;i++) {
            for (int j=0;j<cols;j++)
                printf("%c ",M[i][j]);
            printf("\n");
            }
    }

    return 0;
}
