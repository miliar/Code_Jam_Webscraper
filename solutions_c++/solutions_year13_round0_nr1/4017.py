#include <cstdio>
#include <iostream>

using namespace std;

char board[16];
char winner;

bool check(int i, int di) {
    int iMax = i + 4 * di;
    
    //skip first if it is a T
    if(board[i] == 'T') i += di;
    
    char c = board[i];
    if(c == '.') return false;
    
    for(; i < iMax; i += di) {
        if(board[i] != c && board[i] != 'T') return false;
    }

    winner = c;
    return true;
}

bool checkRow(int row) { return check(row * 4, 1); }
bool checkCol(int col) { return check(col, 4); }
bool checkDiag1()      { return check(0, 5); }
bool checkDiag2()      { return check(3, 3); }

void solveCase() {
    bool hasEmpty = false;

    //read board
    for(int i = 0; i < 16; i++) {
        char c;
        cin >> c;
        board[i] = c;
        if(c == '.') hasEmpty = true;
    }

    //check board
    bool hasWon = false;

    for(int i = 0; i < 4; i++) {
        hasWon |= checkRow(i) || checkCol(i);
        if(hasWon) break;
    }

    hasWon = hasWon || checkDiag1() || checkDiag2();

    //output result
    if(hasWon)        cout << winner << " won";
    else if(hasEmpty) cout << "Game has not completed";
    else              cout << "Draw";
    cout << endl;
}

int main() {
    int caseCount;
    cin >> caseCount;

    for(int i = 1; i <= caseCount; i++) {
        printf("Case #%d: ", i);
        solveCase();
    }

    return 0;
}
