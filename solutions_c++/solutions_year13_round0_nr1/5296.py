#include <iostream>
#include <cstring>

#define REP(i,a) for(int i=0;i<(a);i++)

using namespace std;

int eval(char b[4][4]) {
    int s;
    bool O, X, empty, d1O=true, d1X=true, d2O=true, d2X=true;
    REP(i,4) {
        d1O = d1O && (b[i][i]=='O' || b[i][i]=='T');
        d1X = d1X && (b[i][i]=='X' || b[i][i]=='T');
        d2O = d2O && (b[i][4-i-1]=='O' || b[i][4-i-1]=='T');
        d2X = d2X && (b[i][4-i-1]=='X' || b[i][4-i-1]=='T');
        O = true;
        X = true;
        REP(j,4) {
            int e = b[i][j];
            O = O && (e=='O' || e=='T');
            X = X && (e=='X' || e=='T');
            empty = empty || (e=='.');
        }
        if (X) return 1;
        if (O) return 2;
    }
    if (d1X||d2X) return 1;
    if (d1O||d2O) return 2;
    REP(j,4) {
        X=O=true;
        REP(i,4) {
            int e = b[i][j];
            O = O && (e=='O' || e=='T');
            X = X && (e=='X' || e=='T');
        }
        if (X) return 1;
        if (O) return 2;
    }
    if (empty) return 0;
    return 3;
}

int main() {
    int T;
    string buf;
    char board[4][4];
    cin >> T;
    REP(cas,T) {
        REP(i,4) {
            cin >> buf;
            REP(j,4) board[i][j] = buf[j];
        }
        int e = eval(board);
        cout << "Case #" << (cas+1) << ": ";
        switch (e) {
            case 0: cout << "Game has not completed"; break;
            case 1: cout << "X won"; break;
            case 2: cout << "O won"; break;
            case 3: cout << "Draw"; break;
        }
        cout << endl;
    }
    return 0;
}
