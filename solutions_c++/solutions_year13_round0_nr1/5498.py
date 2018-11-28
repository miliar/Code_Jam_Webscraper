#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int boardFull(char **);
int xWin(char **);
int oWin(char **);

int main() {
    string inputFile, line;
    const char * iF;
    ifstream input;
    ofstream output;
    char ** board;
    int cases;
    
    cout << "Enter Input File: ";
    getline(cin, inputFile);
    iF = inputFile.c_str();
    input.open(iF);
    output.open("Tic-Tac-Toe_Output.txt");
    if (!input.is_open()) {
        cout << "Failed to open input file\n";
        return -1;
    }
    if (!output.is_open()) {
        cout << "Failed to open output file\n";
        return -1;
    }
    board = (char **)malloc(4 * sizeof(char *));
    for (int i = 0; i < 4; i++)
        board[i] = (char *)malloc(4 * sizeof(char));
    getline(input, line);
    cases = atoi(line.c_str());
    for (int i = 1; i <= cases; i++) {
        if (i > 1)
           getline(input, line);
        for (int j = 0; j < 4; j++) {
            getline(input, line);
            for (int k = 0; k < 4; k++)
                board[j][k] = line[k];
        }
        output << "Case #" << i << ": ";
        if (xWin(board))
            output << "X won";
        else if (oWin(board))
            output << "O won";
        else if (boardFull(board))
            output << "Draw";
        else
            output << "Game has not completed";
        if (i < cases)
            output << "\n";
    }
    input.close();
    output.close();
    return 0;
}

int boardFull(char ** board) {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (board[i][j] == '.')
                return 0;
        }
    }
    return 1;
}

int xWin(char ** board) {
    char c0, c1, c2, c3;
    /* check horizontal */
    for (int i = 0; i < 4; i++) {
        c0 = board[i][0];
        c1 = board[i][1];
        c2 = board[i][2];
        c3 = board[i][3];
        if ((c0 == 'X' || c0 == 'T') && (c1 == 'X' || c1 == 'T') &&
                (c2 == 'X' || c2 == 'T') && (c3 == 'X' || c3 == 'T')) {
            return 1;
        }
    }
    /* check vertical */
    for (int j = 0; j < 4; j++) {
        c0 = board[0][j];
        c1 = board[1][j];
        c2 = board[2][j];
        c3 = board[3][j];
        if ((c0 == 'X' || c0 == 'T') && (c1 == 'X' || c1 == 'T') &&
                (c2 == 'X' || c2 == 'T') && (c3 == 'X' || c3 == 'T')) {
            return 1;
        }
    }
    /* check forward diagonal */
    c0 = board[0][0];
    c1 = board[1][1];
    c2 = board[2][2];
    c3 = board[3][3];
    if ((c0 == 'X' || c0 == 'T') && (c1 == 'X' || c1 == 'T') &&
            (c2 == 'X' || c2 == 'T') && (c3 == 'X' || c3 == 'T')) {
        return 1;
    }
    /* check backwards diagonal */
    c0 = board[0][3];
    c1 = board[1][2];
    c2 = board[2][1];
    c3 = board[3][0];
    if ((c0 == 'X' || c0 == 'T') && (c1 == 'X' || c1 == 'T') &&
            (c2 == 'X' || c2 == 'T') && (c3 == 'X' || c3 == 'T')) {
        return 1;
    }
    return 0;
}

int oWin(char ** board) {
    char c0, c1, c2, c3;
    /* check horizontal */
    for (int i = 0; i < 4; i++) {
        c0 = board[i][0];
        c1 = board[i][1];
        c2 = board[i][2];
        c3 = board[i][3];
        if ((c0 == 'O' || c0 == 'T') && (c1 == 'O' || c1 == 'T') &&
                (c2 == 'O' || c2 == 'T') && (c3 == 'O' || c3 == 'T')) {
            return 1;
        }
    }
    /* check vertical */
    for (int j = 0; j < 4; j++) {
        c0 = board[0][j];
        c1 = board[1][j];
        c2 = board[2][j];
        c3 = board[3][j];
        if ((c0 == 'O' || c0 == 'T') && (c1 == 'O' || c1 == 'T') &&
                (c2 == 'O' || c2 == 'T') && (c3 == 'O' || c3 == 'T')) {
            return 1;
        }
    }
    /* check forward diagonal */
    c0 = board[0][0];
    c1 = board[1][1];
    c2 = board[2][2];
    c3 = board[3][3];
    if ((c0 == 'O' || c0 == 'T') && (c1 == 'O' || c1 == 'T') &&
            (c2 == 'O' || c2 == 'T') && (c3 == 'O' || c3 == 'T')) {
        return 1;
    }
    /* check backwards diagonal */
    c0 = board[0][3];
    c1 = board[1][2];
    c2 = board[2][1];
    c3 = board[3][0];
    if ((c0 == 'O' || c0 == 'T') && (c1 == 'O' || c1 == 'T') &&
            (c2 == 'O' || c2 == 'T') && (c3 == 'O' || c3 == 'T')) {
        return 1;
    }
    return 0;
}
