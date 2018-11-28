////////////////////////////////////////////////////////////////////////////////
// 1.cc
////////////////////////////////////////////////////////////////////////////////
/*! @file
//      Solves Google Code Jam QR Problem 1
*/ 
//  Author:  Julian Panetta (jpanetta), julian.panetta@gmail.com
//  Company:  New York University
//
//  Created:  04/13/2013 17:06:15
//  Revision History:
//      04/13/2013  Julian Panetta    Initial Revision
////////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <cassert>

using namespace std;

char checkWin(char *board, int start_row, int start_col,
              int step_row, int step_col)
{
    char player = 'T';
    for (int r = start_row, c = start_col; (r < 4) && (c < 4);
             r += step_row, c += step_col) {
        char b = board[r * 4 + c];
        if (b == '.') return 0;
        else if (b == 'T') continue;
        else if ((player == 'T') || player == b) {
            player = b;
        }
        else return 0;
    }

    // The player has won!
    assert(player != 'T');
    return player;
}

////////////////////////////////////////////////////////////////////////////////
/*! Program entry point
//  @param[in]  argc    Number of arguments
//  @param[in]  argv    Argument strings
//  @return     status  (0 on sucess)
*///////////////////////////////////////////////////////////////////////////////
int main(int argc, const char *argv[])
{
    
    int numTests;
    cin >> numTests;
    char dummy;

    for (int t = 1; t <= numTests; ++t)  {
        char board[4 * 4];
        bool completeBoard = true;
        for (size_t r = 0; r < 4; ++r) {
            for (size_t c = 0; c < 4; ++c) {
                char b;
                cin >> b;
                board[r * 4 + c] = b;
                if (b == '.') completeBoard = false;
            }
        }

        // Check for wins along rows
        char winner = 0;
        for (size_t r = 0; (r < 4) && (winner == 0); ++r)
            winner = checkWin(board, r, 0, 0, 1);
        // Check for wins along cols
        for (size_t c = 0; (c < 4) && (winner == 0); ++c)
            winner = checkWin(board, 0, c, 1, 0);
        // Diagonal one
        if (winner == 0)
            winner = checkWin(board, 0, 0, 1, 1);
        // Diagonal two
        if (winner == 0)
            winner = checkWin(board, 0, 3, 1, -1);

        cout << "Case #" << t << ": ";
        if (winner == 0) {
            if (completeBoard) cout << "Draw";
            else               cout << "Game has not completed";
        }
        else {
            cout << winner << " won";
        }
        cout << endl;
    }

    return 0;
}
