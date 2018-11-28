#include <iostream>
#include <vector>
#include <map>
#include <cstring>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

#define SIZE 4

string board[SIZE];

bool is_valid(char c1, char c2)
{
    return ((c1 == c2) || c1 == 'T');
}

bool check_h(char c)
{
    bool ret = false;

    for (int i = 0; i < SIZE; i++) {
        if (is_valid(board[i][0], c) &&
          is_valid(board[i][1], c) &&
          is_valid(board[i][2], c) && 
          is_valid(board[i][3], c)) {
            ret = true;
            break;
        }
    }

    return ret;
}

bool check_v(char c)
{
    bool ret = false;

    for (int i = 0; i < SIZE; i++) {
        if (is_valid(board[0][i], c) &&
          is_valid(board[1][i], c) &&
          is_valid(board[2][i], c) && 
          is_valid(board[3][i], c)) {
            ret = true;
            break;
        }
    }

    return ret;
}

bool check_d(char c)
{
    bool ret = false;

    if (is_valid(board[0][0], c) &&
      is_valid(board[1][1], c) &&
      is_valid(board[2][2], c) && 
      is_valid(board[3][3], c)) {
        ret = true;
    }

    if (is_valid(board[0][3], c) &&
      is_valid(board[1][2], c) &&
      is_valid(board[2][1], c) && 
      is_valid(board[3][0], c)) {
        ret = true;
    }

    return ret;
}

bool check_board()
{
    bool ret = true;

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] == '.') {
                ret = false;
                break;
            }
        }
    }

    return ret;
}

int main()
{
    int T;
    string status;
    bool is_full;

    cin >> T;
    for (int i = 1; i <= T; i++) {
        for (int j = 0; j < SIZE; j++) {
            cin >> board[j];
        }

        is_full = check_board();

        if (check_h('X') || check_v('X') || check_d('X')) {
            status = "X won";
        } else if (check_h('O') || check_v('O') || check_d('O')) {
            status = "O won";
        } else if (is_full) {
            status = "Draw";
        } else {
            status = "Game has not completed";
        }

        cout << "Case #" << i << ": " << status << endl;
    }
}
