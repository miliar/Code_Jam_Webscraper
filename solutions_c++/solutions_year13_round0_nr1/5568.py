// -*- mode:c++; tab-width:4; c-basic-offset:4; indent-tabs-mode:nil -*-  
#include <iostream>
#include <string>
using namespace std;

int winner[10][4] = {
    {0, 1, 2, 3},
    {4, 5, 6, 7},
    {8, 9, 10, 11},
    {12, 13, 14, 15},
    {0, 4, 8, 12},
    {1, 5, 9, 13},
    {2, 6, 10, 14},
    {3, 7, 11, 15},
    {0, 5, 10, 15},
    {3, 6, 9, 12}};

const int size = 4;
const int winnerLines = 10;

int main()
{
    int n, i, j, k;
    string s;
    bool finished, xWon, oWon, valid;
    char board[size*size];
    cin >> n;

    for (i=0; i<n; i++) {
        cout << "Case #" << i+1 << ": ";
        // Read the board
        for (j=0; j<size; j++) {
            cin >> s;
            //            cout << s;
            for (k=0; k<size; k++)
                board[j*size+k] = s[k];
        }

        // check the board
        finished = true;
        xWon = false;
        oWon = false;
        for (j=0; j<winnerLines && !xWon && !oWon; j++) {
            for (k=0, valid=true; k<size && valid; k++) {
                switch (board[winner[j][k]]) {
                case '.':
                    valid = false;
                    finished = false;
                    break;
                case 'T':
                    break;
                case 'X':
                    if (oWon)
                        valid = false;
                    else
                        xWon = true;
                    break;
                case 'O':
                    if (xWon)
                        valid = false;
                    else
                        oWon =true;
                    break;
                }
            }

            if (!valid) {
                oWon = false;
                xWon = false;
            }
        }
            
        if (xWon)
            cout << "X won" << endl;
        else if (oWon)
            cout << "O won" << endl;
        else if (finished)
            cout << "Draw" << endl;
        else
            cout << "Game has not completed" << endl;

    }

    return 0;
}
