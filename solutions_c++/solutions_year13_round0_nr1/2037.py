// =========================================================
//
//       Filename:  Tic-Tac-Toe-Tomek
//
//    Description:
//
//        Version:  1.0
//        Created:  04/12/2013
//       Revision:  none
//       Compiler:  gcc
//
//         Author:  Tao Lin, tlin005@gmail.com
//        Company:  U of California Riverside
//      Copyright:  Copyright (c) 04/12/2013
//
// =========================================================

#include <iostream>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

unsigned long long int solve(unsigned int N, unsigned int K, vector< unsigned long long int >::iterator a)
{
    unsigned long long int result = 0l;

    return result;
}

int main()
{
    unsigned int case_no;
    char board[4][4];

    // load input
    cin >> case_no;

    for (unsigned int t = 0; t < case_no; ++t)
    {
        // load board
        int empty = 0;
        for (unsigned i = 0; i < 4; ++i)
            for (unsigned j = 0; j < 4; ++j)
            {
                cin >> board[i][j];
                if (board[i][j] == '.')
                    empty++;
            }

        // sove problem
        int dir[][4] = { {0, 0, 1, 0}, {0, 1, 1, 0}, {0, 2, 1, 0}, {0, 3, 1, 0},
                         {0, 0, 0, 1}, {1, 0, 0, 1}, {2, 0, 0, 1}, {3, 0, 0, 1},
                         {0, 0, 1, 1}, {0, 3, 1, -1} };

        bool complete = false;

        // count X
        for (unsigned int i = 0; i < 10; ++i)
        {
            unsigned x = dir[i][0];
            unsigned y = dir[i][1];

            unsigned int n = 0;
            while ( (n < 4) && ((board[x][y] == 'X') || (board[x][y] == 'T')) )
            {
                x += dir[i][2];
                y += dir[i][3];
                n++;
            }
            if (n >= 4)
            {
                cout << "Case #" << t+1 << ": X won" << endl;
                complete = true;
                break;
            }
        }
        // count O
        for (unsigned int i = 0; i < 10; ++i)
        {
            unsigned x = dir[i][0];
            unsigned y = dir[i][1];

            unsigned int n = 0;
            while ( (n < 4) && ((board[x][y] == 'O') || (board[x][y] == 'T')) )
            {
                x += dir[i][2];
                y += dir[i][3];
                n++;
            }
            if (n >= 4)
            {
                cout << "Case #" << t+1 << ": O won" << endl;
                complete = true;
                break;
            }
        }

        if (complete)
            continue;

        if (empty > 0)
            cout << "Case #" << t+1 << ": Game has not completed" << endl;
        else
            cout << "Case #" << t+1 << ": Draw" << endl;
    }

    return 0;

}
