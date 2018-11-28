#include <stdio.h>

#define REP(i, n) for(int i=0; i<(n); i++)
#define REPD(i, n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i, a, b) for( int i = a; i <= (b); i++)
#define FORD(i, a, b) for(int i=(a); i >= (b); i--)
#define VAR(a, b) __typeof(b) a=(b)
#define FORCOL(i, col) for(VAR(i, (col).begin()); i!=(col).end(); i++)
#define ZERO(x) memset(x, 0, sizeof x);
#define ALL(x) (x).begin(), (x).end()

#define PB push_back
#define ST first
#define ND second

typedef long long int LL;
typedef long double LD;

char ** STATE;

bool checkRow(char sign, int row) {
    REP(i, 4) {
        if (STATE[row][i] == sign || STATE[row][i] == 'T') {
        } else {
            return false;
        }
    }
    return true;
}

bool checkColumn(char sign, int col) {
    REP(i, 4) {
        if (STATE[i][col] == sign || STATE[i][col] == 'T') {
        } else {
            return false;
        }
    }
    return true;
}

bool checkDiagonalOne(char sign) {
    REP(i, 4) {
        if (STATE[i][i] == sign || STATE[i][i] == 'T') {
        } else {
            return false;
        }
    }
    return true;
}

bool checkDiagonalTwo(char sign) {
    REP(i, 4) {
        if (STATE[i][3-i] == sign || STATE[i][3-i] == 'T') {
        } else {
            return false;
        }
    }
    return true;
}

bool checkEnd() {
    REP(i, 4) {
        REP(j, 4) {
            if (STATE[i][j] == '.') {
                return false;
            }
        }
    }
    return true;
}

bool checkWin(char sign) {
    REP(i, 4) {
        if (checkRow(sign, i)) return true;
        if (checkColumn(sign, i)) return true;
    }
    if (checkDiagonalOne(sign)) return true;
    if (checkDiagonalTwo(sign)) return true;
    return false;
}

int main() {
    STATE = new char*[4];
    REP(i, 4) {
        STATE[i] = new char[4];
    }
    
    int t;
    scanf("%d\n", &t);
    REP(tt, t) {
        REP(i, 4) {
            scanf("%s\n", STATE[i]);
        }
        scanf("\n");
        if (checkWin('X')) {
            printf("Case #%d: X won\n", tt+1);
        } else if (checkWin('O')) {
            printf("Case #%d: O won\n", tt+1);
        } else if(checkEnd()) {
            printf("Case #%d: Draw\n", tt+1);
        } else {
            printf("Case #%d: Game has not completed\n", tt+1);
        }
        
    }
    return 0;
}
