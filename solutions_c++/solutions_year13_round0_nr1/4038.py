#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <string>
#include <cstring>
#define TASK "A"
using namespace std;

char winningLine(char grid[4][4], int x, int y, int dx, int dy) {
    for (char r = 'O'; r <= 'X'; r += 'X' - 'O') {
        bool winning = true;
        for (int i = 0; i < 4; i++) {
            char c = grid[y + i * dy][x + i * dx];
            if (c == '.') {
                return -1;
            } else if (c != 'T' && c != r) {
                winning = false;
                break;
            }
        }
        if (winning) {
            return r;
        }
    }
    return -1;
}

int main() {
    freopen(TASK ".in", "r", stdin);
    freopen(TASK ".out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for (int test = 1; test <= T; test++) {
        char g[4][4];
        int empty = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf(" %c", &g[i][j]);
                empty += g[i][j] == '.';
            }
        }
        
        char winner = -1;
        
        winner = winningLine(g, 0, 0, +1, +1);
        if (winner == -1) {
            winner = winningLine(g, 0, 3, +1, -1);
        }
        
        for (int i = 0; i < 4 && winner == -1; i++) {
            //printf("Considering i = %d\n", i);
            if ((winner = winningLine(g, 0, i, +1, 0)) != -1) {
                break;
            } else if ((winner = winningLine(g, i, 0, 0, +1)) != -1) {
                break;
            }
        }
        
        printf("Case #%d: ", test);
        if (winner != -1) {
            printf("%c won", winner);
        } else if (empty > 0) {
            printf("Game has not completed");
        } else {
            printf("Draw");
        }
        printf("\n");
    }
    
    return 0;
}
