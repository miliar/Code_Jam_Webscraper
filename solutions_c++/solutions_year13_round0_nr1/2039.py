#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int XWON = 0;
const int OWON = 1;
const int DRAW = 2;
const int ONGO = 3;

string get_column(vector<string> &board, int col) {
    string res = "";

    for (int i = 0; i < 4; i++) {
        res += board[i][col];
    }

    return res;
}

string get_diag1(vector<string> &board) {
    string res = "";

    for (int i = 0; i < 4; i++) res += board[i][i];

    return res;
}

string get_diag2(vector<string> &board) {
    string res = "";

    for (int i = 0; i < 4; i++) res += board[i][3-i];

    return res;
}

string magia(vector<string> &board) {
    int tx, ty;
    bool tfound = false;

    for (int i = 0; i < 4 && !tfound; i++) {
        for (int j = 0; j < 4 && !tfound; j++) {
            if (board[i][j] == 'T') {
                tx = i;
                ty = j;
                tfound = true;
            }
        }
    }

    //Filas
    if (tfound) board[tx][ty] = 'X';
    for (int i = 0; i < 4; i++) {
        if (board[i] == "XXXX") return "X won";
    }
    if (tfound) board[tx][ty] = 'O';
    for (int i = 0; i < 4; i++) {
        if (board[i] == "OOOO") return "O won";
    }
    //Columnas
    if (tfound) board[tx][ty] = 'X';
    for (int j = 0; j < 4; j++) {
        if (get_column(board, j) == "XXXX") return "X won";
    }
    if (tfound) board[tx][ty] = 'O';
    for (int j = 0; j < 4; j++) {
        if (get_column(board, j) == "OOOO") return "O won";
    }
    //Diagonales
    if (tfound) board[tx][ty] = 'X';
    if (get_diag1(board) == "XXXX") return "X won";
    if (get_diag2(board) == "XXXX") return "X won";
    if (tfound) board[tx][ty] = 'O';
    if (get_diag1(board) == "OOOO") return "O won";
    if (get_diag2(board) == "OOOO") return "O won";
    //Draw?
    bool is_draw = true;
    for (int i = 0; i < 4 && is_draw; i++)
        for (int j = 0; j < 4 && is_draw; j++)
            if (board[i][j] == '.') is_draw = false;

    if (is_draw)
        return "Draw";
    else
        return "Game has not completed";
}

int main() {
    int t;
    string line;
    vector<string> board(4);

    cin >> t;

    for (int n_case = 1; n_case <= t; n_case++) {
        board.clear();
        board.resize(4);
        for (int i = 0; i < 4; i++) {
            cin >> board[i];
        }

        cout << "Case #" << n_case << ": " << magia(board) << endl;
    }

    return 0;
}
