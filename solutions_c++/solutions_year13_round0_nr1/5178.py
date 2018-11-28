#include <stdio.h>
#define FOR(i,n) for(int i = 0; i < (n); i++)

#define Check(b) grid[r][c] == b || grid[r][c] == 'T'

char grid[6][6];
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int numT; scanf("%d", &numT);
    for(int cno = 1; cno <= numT; cno++)
    {
        FOR(r, 4) scanf("%s", grid[r]);
        bool isXWin = false, isOWin = false;
        bool isBoardFill = true;
        FOR(r, 4) {
            int ccx, cco;
            ccx = cco = 0; FOR(c, 4) {
                if(Check('X')) ccx++;
                if(Check('O')) cco++;
            }
            if(ccx == 4) { isXWin = true; goto done; }
            if(cco == 4) { isOWin = true; goto done; }
        }

        FOR(c, 4) {
            int ccx, cco;
            ccx = cco = 0; FOR(r, 4) {
                if(Check('X')) ccx++;
                if(Check('O')) cco++;
            }
            if(ccx == 4) { isXWin = true; goto done; }
            if(cco == 4) { isOWin = true; goto done; }
        }

        {
            int ccx, cco;
            ccx = cco = 0; FOR(r, 4) {
                int c = r;
                if(Check('X')) ccx++;
                if(Check('O')) cco++;
            }
            if(ccx == 4) { isXWin = true; goto done; }
            if(cco == 4) { isOWin = true; goto done; }
        }

        {
            int ccx, cco;
            ccx = cco = 0; FOR(r, 4) {
                int c = 3 - r;
                if(Check('X')) ccx++;
                if(Check('O')) cco++;
            }
            if(ccx == 4) { isXWin = true; goto done; }
            if(cco == 4) { isOWin = true; goto done; }
        }

        FOR(r, 4) {
            FOR(c, 4) {
                if(grid[r][c] == '.') { isBoardFill = false; goto done; }
            }
        }

        done:
        printf("Case #%d: ", cno);
        if(isXWin) printf("X won\n");
        else if(isOWin) printf("O won\n");
        else if(isBoardFill) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
