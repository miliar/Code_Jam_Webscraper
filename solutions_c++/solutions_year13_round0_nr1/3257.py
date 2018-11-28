#include<cstdlib>
#include<cstdio>
#include<iostream>
using namespace std;
#define REP(i,n) for ( int i = 0; i < (n); i++ )
char winner;
char plan[4][4];
char checkLine(int a) {
    int x, o;
    x = o = 0;
    REP(b,4) {
        if (plan[a][b] == '.') return 'D';
        if (plan[a][b] == 'X') x++;
        if (plan[a][b] == 'O') o++;
    }
    if (!x) return 'O';
    if (!o) return 'X';
    return 'D';
}

char checkColum(int b) {
    int x, o;
    x = o = 0;
    REP(a,4) {
        if (plan[a][b] == '.') return 'D';
        if (plan[a][b] == 'X') x++;
        if (plan[a][b] == 'O') o++;
    }
    if (!x) return 'O';
    if (!o) return 'X';
    return 'D';
}

char checkDiagonals() {
    int x, o;
    x = o = 0;
    REP(i,4) {
        if (plan[i][i] == '.')  { x = o = 1; break; }
        if (plan[i][i] == 'X') x++;
        if (plan[i][i] == 'O') o++;
    }
    if (!x) return 'O';
    if (!o) return 'X';
    x = o = 0;
    REP(i,4) {
        if (plan[i][3-i] == '.') return 'D';
        if (plan[i][3-i] == 'X') x++;
        if (plan[i][3-i] == 'O') o++;
    }
    if (!x) return 'O';
    if (!o) return 'X';
    return 'D';
}

int main() {
    int n;
    bool drawpossible;

    scanf("%d",&n);
    REP(testNr,n) {
        drawpossible = true;
        REP(i,4) REP(j,4) {
            scanf(" %c",&plan[i][j]);
            if (plan[i][j] == '.') drawpossible = false;
        }
        winner = 'D';
        REP(i,4) if ( winner == 'D' ) winner = checkLine(i);
        REP(j,4) if ( winner == 'D' ) winner = checkColum(j);
        if (winner == 'D') winner = checkDiagonals();
        if (winner == 'D')
            if (drawpossible) printf("Case #%d: Draw\n",testNr+1);
            else printf("Case #%d: Game has not completed\n",testNr+1);
        else printf("Case #%d: %c won\n",testNr+1,winner);
    }
    return 0;
}

