// #include "common.h"

// -W -Wall -Werror -std=c++0x -Wno-sign-compare -Wfloat-equal

// alias valgrind='\valgrind --malloc-fill=AA --track-origins=yes
// --read-var-info=yes --num-callers=50 --db-attach=no --db-command="kdbg %f -p %p"'

// alias callgrind='\valgrind --tool=callgrind --simulate-cache=yes --dump-instr=yes'

// Valgrind with stdin + debug:
// valgrind --input-fd=3 --db-attach=yes build/foo <input 3</dev/tty

#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <deque>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <utility>
#include <vector>
#include <stack>

typedef int Int;
#define int long long

using namespace std;

bool lost(const vector<string>& board, char player) {
    // Check if X won in a row
    for (const auto& row : board) {
        for (char c : row)
            if (c == '.' || c == player)
                goto next_row;
        
        return true;
        
    next_row:;
    }
    
    // Check if X won in a col
    for (int col = 0; col < 4; col++) {
        
        for (int row = 0; row < 4; row++)
            if (board[row][col] == '.' || board[row][col] == player)
                goto next_col;
        
        return true;
        
    next_col:;
    }
    
    // Check if X won in the main diag
    for (int i = 0; i < 4; i++)
        if (board[i][i] == '.' || board[i][i] == player)
            goto next_diag;
    
    return true;
    
    next_diag:;
    
    // Check if X won in the other diag
    for (int i = 0; i < 4; i++)
        if (board[i][3-i] == '.' || board[i][3-i] == player)
            return false;
    
    return true;
}

bool full(const vector<string>& board) {
    for (const string& row : board)
        for (char c : row)
            if (c == '.')
                return false;
    return true;
}

void solve_test() {
    vector<string> board(4);
    for (auto& row : board)
        cin >> row;
    
    if (lost(board, 'X'))
        cout << "O won" << endl;
    else if (lost(board, 'O'))
        cout << "X won" << endl;
    else if (full(board))
        cout << "Draw" << endl;
    else
        cout << "Game has not completed" << endl;
}

Int main() {
    
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Case #" << (i+1) << ": ";
        solve_test();
    }
    
    return 0;
}
