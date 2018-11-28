
#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

typedef enum { X_WON, O_WON, DRAW, NOT_COMPLETED } GameStatus;

GameStatus solve(char tab[4][5]) {
    bool o_used;
    bool x_used;
    bool empty = false;
    int i, j;
    
    for (i = 0; i < 4; i++) {
        o_used = false;
        x_used = false;
        
        for (j = 0; j < 4; j++) {
            if (tab[i][j] == '.') {
                empty = true;
                break;
            } else if (tab[i][j] == 'X') {
                x_used = true;
            } else if (tab[i][j] == 'O') {
                o_used = true;   
            }
        }
        
        if (tab[i][j] != '.') {
            if (x_used && !o_used) { return X_WON; }
            else if (o_used && !x_used) { return O_WON; }
        }
    }
    
    for (i = 0; i < 4; i++) {
        o_used = false;
        x_used = false;
        
        for (j = 0; j < 4; j++) {
            if (tab[j][i] == '.') {
                empty = true;
                break;
            } else if (tab[j][i] == 'X') {
                x_used = true;
            } else if (tab[j][i] == 'O') {
                o_used = true;   
            }
        }
        
        if (tab[j][i] != '.') {
            if (x_used && !o_used) { return X_WON; }
            else if (o_used && !x_used) { return O_WON; }
        }
    }
    
    o_used = false;
    x_used = false;
    
    for (i = 0; i < 4; i++) {
        if (tab[i][i] == 'X') x_used = true;
        if (tab[i][i] == 'O') o_used = true;
        if (tab[i][i] == '.') {
            break;
        }
    }
    
    if (tab[i][i] != '.') {
        if (x_used && !o_used) { return X_WON; }
        else if (o_used && !x_used) { return O_WON; }
    }
    
    o_used = false;
    x_used = false;
    
    for (i = 0; i < 4; i++) {
        if (tab[i][3 - i] == 'X') x_used = true;
        if (tab[i][3 - i] == 'O') o_used = true;
        if (tab[i][3 - i] == '.') {
            break;
        }
    }
    
    if (tab[i][3 - i] != '.') {
        if (x_used && !o_used) { return X_WON; }
        else if (o_used && !x_used) { return O_WON; }
    }
    
    if (empty) {
        return NOT_COMPLETED;
    } else {
        return DRAW;
    }
}

int main (void) {
    int t;
    char tab[4][5];
    GameStatus gameStatus;
    
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    scanf("%d", &t);
    
    for (int z = 1; z <= t; z++) {
        for (int i = 0; i < 4; i++) {
            scanf("%s", tab[i]);
        }
        
        printf("Case #%d: ", z);
        gameStatus = solve(tab);
        
        if (gameStatus == X_WON) {
            printf("X won\n");
        } else if (gameStatus == O_WON) {
            printf("O won\n");
        } else if (gameStatus == DRAW) {
            printf("Draw\n");
        } else if (gameStatus == NOT_COMPLETED) {
            printf("Game has not completed\n");
        }
    }
    
    return 0;
}
