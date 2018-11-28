#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define inf 1000000000
#define MAXN 4

using namespace std;

char board[MAXN][MAXN+1];

char initCurrentSymbol(int i, int j) {
    if (board[i][j] == 'X' || board[i][j] == 'O' || board[i][j] == 'T')
        return board[i][j];
    else return 'Z';
}

int main()
{
    int t;
    scanf("%d\n", &t);
    
    for (int qwertz = 0; qwertz < t; ++qwertz) {
        for (int i = 0; i < MAXN; ++i) {
            scanf("%s", board[i]);
        }
        
        bool hasDot = false, gameOver = false;
        char currentSymbol_horizontal, currentSymbol_vertical, currentSymbol_left_diagonal, currentSymbol_right_diagonal;
        currentSymbol_left_diagonal = initCurrentSymbol(0,0);
        currentSymbol_right_diagonal = initCurrentSymbol(0, MAXN-1);
        bool foundWinner_left_diagonal = true, foundWinner_right_diagonal = true;
        for (int i = 0; i < MAXN; ++i) {
            currentSymbol_horizontal = initCurrentSymbol(i,0);
            currentSymbol_vertical = initCurrentSymbol(0,i);
            
            bool foundWinner_horizontal = true, foundWinner_vertical = true;
            for (int j = 1; j < MAXN; ++j) {
                if (board[i][j] == '.') hasDot = true;
                
                // horizontal
                if (currentSymbol_horizontal == 'T') {
                    if (board[i][j] == 'O' || board[i][j] == 'X') currentSymbol_horizontal = board[i][j];
                    else foundWinner_horizontal = false;
                }
                if (board[i][j] != currentSymbol_horizontal && board[i][j] != 'T') foundWinner_horizontal = false;
                
                // vertical
                if (currentSymbol_vertical == 'T') {
                    if (board[j][i] == 'O' || board[j][i] == 'X') currentSymbol_vertical = board[j][i];
                    else foundWinner_vertical = false;
                }
                if (board[j][i] != currentSymbol_vertical && board[j][i] != 'T') foundWinner_vertical = false;
            }
            
            if (foundWinner_horizontal) {
                printf("Case #%d: %c won\n", qwertz+1, currentSymbol_horizontal);
                gameOver = true;
                break;
            }
            if (foundWinner_vertical) {
                printf("Case #%d: %c won\n", qwertz+1, currentSymbol_vertical);
                gameOver = true;
                break;
            }
            
            // left diagonal
            if (currentSymbol_left_diagonal == 'T') {
                if (board[i][i] == 'O' || board[i][i] == 'X') currentSymbol_left_diagonal = board[i][i];
                else foundWinner_left_diagonal = false;
            }
            if (board[i][i] != currentSymbol_left_diagonal && board[i][i] != 'T') foundWinner_left_diagonal = false;
            
            // right diagonal
            if (currentSymbol_right_diagonal == 'T') {
                if (board[i][MAXN-i-1] == 'O' || board[i][MAXN-i-1] == 'X') currentSymbol_right_diagonal = board[i][MAXN-i-1];
                else foundWinner_right_diagonal = false;
            }
            if (board[i][MAXN-i-1] != currentSymbol_right_diagonal && board[i][MAXN-i-1] != 'T') foundWinner_right_diagonal = false;
        }
        
        if (!gameOver) {
            if (foundWinner_left_diagonal) {
                printf("Case #%d: %c won\n", qwertz+1, currentSymbol_left_diagonal);
            }
            else if (foundWinner_right_diagonal) {
                printf("Case #%d: %c won\n", qwertz+1, currentSymbol_right_diagonal);
            }
            else if (hasDot) printf("Case #%d: Game has not completed\n", qwertz+1);
            else printf("Case #%d: Draw\n", qwertz+1);
        }
    }
    
    return 0;
}
