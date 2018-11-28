#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int BOARD_DIM = 4;
char TOMEK = 'T';
char EMPTY = '.';


void print_board(std::vector<std::vector<char> > &board) {
    for (int row=0; row<BOARD_DIM; row++) {
        for (int col=0; col<BOARD_DIM; col++)
            cout << board[row][col];
        cout << endl;
    }
}


bool completed(std::vector<std::vector<char> > &board) {
    for (int row=0; row<BOARD_DIM; row++)
        for (int col=0; col<BOARD_DIM; col++)
            if (board[row][col] == EMPTY) return false;
    return true;
}


bool victory(std::vector<std::vector<char> > &board, char player) {

    // check winning rows
    for (int row=0; row<BOARD_DIM; row++) {
        bool row_victory = true;
        for (int col=0; col<BOARD_DIM; col++)
            if (!(board[row][col] == player || board[row][col] == TOMEK)) {
                row_victory = false;
                break;
            }
        if (row_victory) return true;
    }

    // check winning columns
    for (int col=0; col<BOARD_DIM; col++) {
        bool col_victory = true;
        for (int row=0; row<BOARD_DIM; row++)
            if (!(board[row][col] == player || board[row][col] == TOMEK)) {
                col_victory = false;
                break;
            }
        if (col_victory) return true;
    }

    // check winning diagonals
    bool diag_victory = true;
    for (int d=0; d<BOARD_DIM; d++) {
        if (!(board[d][d] == player || board[d][d] == TOMEK)) {
            diag_victory = false;
            break;
        }
    }
    if (diag_victory) return true;

    diag_victory = true;
    for (int d=0; d<BOARD_DIM; d++) {
        if (!(board[d][BOARD_DIM-d-1] == player || board[d][BOARD_DIM-d-1] == TOMEK)) {
            diag_victory = false;
            break;
        }
    }
    if (diag_victory) return true;

    return false;
}



int main(int argc, char **argv) {

    ifstream testf(argv[1]);
    string line;
    stringstream linestream;
    int num_tests;

    getline(testf, line);
    linestream.str(line);
    linestream >> num_tests;

    std::vector<std::vector<char> > board;
    board.resize(BOARD_DIM);
    for (int row=0; row<BOARD_DIM; row++)
        board[row].resize(BOARD_DIM);

    for (int t=0; t<num_tests; t++) {
        for (int row=0; row<BOARD_DIM; row++) {
            getline(testf, line);
            for (int col=0; col<BOARD_DIM; col++)
                board[row][col] = line[col];
        }
        getline(testf, line);

        cout << "Case #" << t+1 << ": ";
        if (victory(board, 'X'))
            cout << "X won";
        else if (victory(board, 'O'))
            cout << "O won";
        else if (completed(board))
            cout << "Draw";
        else
            cout << "Game has not completed";
        cout << endl;
    }

    return 0;
}

