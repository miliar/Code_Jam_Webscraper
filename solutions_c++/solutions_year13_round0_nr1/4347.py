#include <cstdio>
#include <cstring>

#define FILEIN "input.txt"
#define FILEOUT "output.txt"

char G[6][6];
int k,i,j;

void solve() {
    int xwon = 0;
    int owon = 0;
    int ocount, xcount;
    int dotcount = 0;
    for ( i = 1; i <= 4; i++) {
        for ( j = 1; j <= 4; ++j) {
            if(G[i][j] == '.')
                dotcount++;
        }
    }
    for ( i = 1; i <= 4; i++) { // check lines
        ocount = xcount = 0;
        for ( j = 1; j <= 4; ++j) {
            if(G[i][j] == 'O')
                ocount++;
            if(G[i][j] == 'T')
                ocount++, xcount++;
            if(G[i][j] == 'X')
                xcount++;
        }
        if(ocount == 4)
            owon = 1;
        if(xcount == 4)
            xwon = 1;
    }
    for ( i = 1; i <= 4; i++) { // check columns
        ocount = xcount = 0;
        for ( j = 1; j <= 4; ++j) {
            if(G[j][i] == 'O')
                ocount++;
            if(G[j][i] == 'T')
                ocount++, xcount++;
            if(G[j][i] == 'X')
                xcount++;
        }
        if(ocount == 4)
            owon = 1;
        if(xcount == 4)
            xwon = 1;
    }
    ocount = xcount = 0;
    for ( i = 1; i <= 4; i++) { // check diagonals
        if(G[i][i] == 'O')
            ocount++;
        if(G[i][i] == 'T')
            ocount++, xcount++;
        if(G[i][i] == 'X')
            xcount++;
    }
    if(ocount == 4)
        owon = 1;
    if(xcount == 4)
        xwon = 1;
    ocount = xcount = 0;
    for ( i = 1; i <= 4; i++) { // check diagonals
        if(G[i][5-i] == 'O')
            ocount++;
        if(G[i][5-i] == 'T')
            ocount++, xcount++;
        if(G[i][5-i] == 'X')
            xcount++;
    }
    if(ocount == 4)
        owon = 1;
    if(xcount == 4)
        xwon = 1;
    if(owon == 1 && xwon == 1)
        printf("Case #%d: Draw\n", k);
    else
    if(owon == 1)
        printf("Case #%d: O won\n", k);
    else
    if(xwon == 1)
        printf("Case #%d: X won\n", k);
    else
    {
        if(dotcount == 0)
            printf("Case #%d: Draw\n", k);
        else
            printf("Case #%d: Game has not completed\n", k);
    }

}

int main() {
    freopen(FILEIN,"r",stdin);
    freopen(FILEOUT, "w", stdout);
    int T;
    scanf("%d", &T);
    for( k = 1; k <= T; ++k) {
        scanf("%s\n", &G[1][0]+1);
        scanf("%s\n", &G[2][0]+1);
        scanf("%s\n", &G[3][0]+1);
        scanf("%s\n", &G[4][0]+1);
        scanf("\n");
        solve();
    }
    return 0;
}
