#include <cstdio>
#include <iostream>

#include <vector>
#include <list>
#include <string>

#include <algorithm>
#include <functional>
#include <cmath>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

bool is_field_full(string board[4])
{
    for(int i = 0; i < 4; ++i)
        for(int j = 0; j < 4; ++j)
            if(board[i][j] == '.')
                return false;

    return true;
}

bool check_row(string board[4], int row_number, char value)
{
    for(int i = 0; i < 4; ++i) {
        char x = board[row_number][i];
        if(x != value && x != 'T')
            return false;
    }

    return true;
}

bool check_column(string board[4], int column_number, char value)
{
    for(int i = 0; i < 4; ++i) {
        char x = board[i][column_number];
        if(x != value && x != 'T')
            return false;
    }

    return true;
}

bool check_main_dia(string board[4], char value)
{
    for(int i = 0; i < 4; ++i) {
        char x = board[i][i];
        if(x != value && x != 'T')
            return false;
    }

    return true;
}

bool check_minor_dia(string board[4], char value)
{
    for(int i = 0; i < 4; ++i) {
        char x = board[i][4 - i - 1];
        if(x != value && x != 'T')
            return false;
    }

    return true;
}

void solve_case(string board[4], int case_number)
{
    bool x = false;
    bool o = false;

    for(int i = 0; i < 4; ++i) {
        x = x || check_row(board, i, 'X');
        o = o || check_row(board, i, 'O');
        x = x || check_column(board, i, 'X');
        o = o || check_column(board, i, 'O');
    }

    x = x || check_main_dia(board, 'X');
    o = o || check_main_dia(board, 'O');
    x = x || check_minor_dia(board, 'X');
    o = o || check_minor_dia(board, 'O');

    cout << "Case #" << case_number << ": "; 

    if(x) {
        cout << "X won" << endl;
    } else if(o) {
        cout << "O won" << endl;
    } else if(is_field_full(board)) {
        cout << "Draw" << endl;
    } else {
        cout << "Game has not completed" << endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);

    int t;
    string board[4];
    cin >> t;

    for(int i = 1; i <= t; ++i) {
        for(int j = 0; j < 4; ++j)
            cin >> board[j];

        solve_case(board, i);
    }

    return 0;
}

// Local Variables:
// eval: (when (fboundp 'flymake-mode) (flymake-mode 1))
// End:
