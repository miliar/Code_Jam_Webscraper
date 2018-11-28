#include <stdio.h>
#include <iostream>

using namespace std;

char field[4][4];

bool hasLine(char player, int startX, int startY, int dX, int dY, int thresh) {
    if (thresh <= 0) return true;
    if ((startX > 3 || startX < 0) || (startY > 3 || startY < 0)) return false;
    if(field[startX][startY] == player || field[startX][startY] == 'T') return hasLine(player, startX + dX, startY + dY, dX, dY, thresh - 1);
    return false;
}

bool hasWon(char player) {
    bool diag = hasLine(player, 0, 0, 1, 1, 4) || hasLine(player, 0, 3, 1, -1, 4); //left bottom, right up
    if (diag) {
        return true;
    }
    bool lines = false;
    for(int i = 0; i < 4; i++) {
        lines = hasLine(player, 0, i, 1, 0, 4) || hasLine(player, i, 0, 0, 1, 4);
        if(lines) break;
    } 
    return lines;
}

bool freeFields() {
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            if(field[i][j] == '.') return true;
    return false;
}

int main() {
    unsigned int testcases, current_case;
    cin >> testcases;
    
    for(current_case = 1; current_case <= testcases; current_case++) {
        for(size_t x = 0; x < 4; x++) {
            cin.ignore();
            for(size_t y = 0; y < 4; y++) {
                cin >> field[x][y];
            }
        }
        cout << "Case #" << current_case << ": ";
            bool X = hasWon('X');
            bool Y = hasWon('O');
            if(X && !Y)
                cout << "X won" << endl;
            else if (!X && Y)
                cout << "O won" << endl;
            else {
                if(freeFields())
                    cout << "Game has not completed" << endl;
                else
                    cout << "Draw" << endl;
            }
    }
}
