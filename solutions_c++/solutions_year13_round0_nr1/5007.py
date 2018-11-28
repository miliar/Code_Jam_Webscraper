#include <cstdio>
#include <cstdlib>

#define E(a, b) (a == b || a == 'T')

int main(void) {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n, i, j, k, T;
    bool full;
    unsigned int xrow, xcol, orow, ocol, xdiag, xrdiag, odiag, ordiag;
    char board[4][4];
    
    scanf("%d\n", &T);

    for (i=1; i<=T; ++i) {
        full = true;
        printf("Case #%d: ", i);

        xrow = xcol = orow = ocol = (1<<4)-1;
        xdiag = xrdiag = odiag = ordiag = 1;
        for (j=0; j<4; ++j) {
            for (k=0; k<4; ++k) {
                scanf("%c", &board[j][k]);
                full &= board[j][k] != '.';

                xrow &= ~((!E(board[j][k], 'X'))<<j);
                xcol &= ~((!E(board[j][k], 'X'))<<k);
                orow &= ~((!E(board[j][k], 'O'))<<j);
                ocol &= ~((!E(board[j][k], 'O'))<<k);
                if ( j == k ) {
                    xdiag &= E(board[j][k], 'X');
                    odiag &= E(board[j][k], 'O');
                }
                else if ( j+k == 3 ) {
                    xrdiag &= E(board[j][k], 'X');
                    ordiag &= E(board[j][k], 'O');
                }
            }
            scanf("\n");
        }
        scanf("\n");

        if ( xrow || xcol || xdiag || xrdiag ) printf("X won\n");
        else if ( orow || ocol || odiag || ordiag ) printf("O won\n");
        else if ( full ) printf("Draw\n");
        else printf("Game has not completed\n");
    }

    return 0;
}
