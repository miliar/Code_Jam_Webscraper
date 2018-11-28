#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

bool is_incomplete(char grid[4][4]) {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (grid[i][j] == '.') {
                return true;
            }
        }
    }

    return false;
}

bool check_win(char grid[4][4], char player) {
    bool won = true;

    //check horizontals
    for (int i = 0; i < 4; i++) {
        won = true;
        
        for (int j = 0; j < 4; j++) {
            if (grid[i][j] != 'T' && grid[i][j] != player) {
                won = false;
                break;
            }
        }
        
        if (won) {
            return true;
        }
    }
    
    //check verticals
    for (int i = 0; i < 4; i++) {
        won = true;
        
        for (int j = 0; j < 4; j++) {
            if (grid[j][i] != 'T' && grid[j][i] != player) {
                won = false;
                break;
            }
        }
        
        if (won) {
            return true;
        }
    }
    
    //check first diagonal
    won = true;
    for (int k = 0, i = 0, j = 0; k < 4; k++, i+=1, j+=1) {
        if (grid[i][j] != 'T' && grid[i][j] != player) {
            won = false;
            break;
        }
    }
    
    if (won) {
        return true;
    }
    
    //check second diagonal
    won = true;
    for (int k = 0, i = 0, j = 3; k < 4; k++, i+=1, j-=1) {
        if (grid[i][j] != 'T' && grid[i][j] != player) {
            won = false;
            break;
        }
    }
    
    return won;
}

int main()
{
    char grid[4][4];
    int T, case_ = 0;
    
    cin >> T;
    
    while (T--) {
        ++case_;
        for (int i = 0; i < 4; i++) {
            cin >> grid[i];
        }
        
        if (check_win(grid, 'X')) {
            cout << "Case #" << case_ << ": X won" << endl;
        } else if (check_win(grid, 'O')) {
            cout << "Case #" << case_ << ": O won" << endl;
        } else if (is_incomplete(grid)) {
            cout << "Case #" << case_ << ": Game has not completed" << endl;
        } else {
            cout << "Case #" << case_ << ": Draw" << endl;
        }
        
        
    
    }

    return 0;
}

