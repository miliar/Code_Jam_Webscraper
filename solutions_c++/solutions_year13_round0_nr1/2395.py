#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

const int EMPTY = 0;
const int CROSS = 1;
const int CIRCLE = 2;
const int TCell = 3;

const int CROSS_WIN = 0;
const int CIRCLE_WIN = 1;
const int DRAW = 2;
const int NOT_COMPLETE = 3;

int gameResult(const int board[4][4])
{
    // Rows.
    for (int row = 0; row < 4; ++row)
    {
        int crossSum = (board[row][0] & 1)
                       + (board[row][1] & 1) 
                       + (board[row][2] & 1) 
                       + (board[row][3] & 1);

        int circleSum = (board[row][0] & 2) 
                        + (board[row][1] & 2) 
                        + (board[row][2] & 2) 
                        + (board[row][3] & 2);

        if (crossSum == 4)
            return CROSS_WIN;
        else if (circleSum == 8)
            return CIRCLE_WIN;
    }

    for (int col = 0; col < 4; ++col)
    {
        int crossSum = (board[0][col] & 1) 
                       + (board[1][col] & 1) 
                       + (board[2][col] & 1) 
                       + (board[3][col] & 1);

        int circleSum = (board[0][col] & 2) 
                        + (board[1][col] & 2) 
                        + (board[2][col] & 2) 
                        + (board[3][col] & 2);
        if (crossSum == 4)
            return CROSS_WIN;
        else if (circleSum == 8)
            return CIRCLE_WIN;
    }

    // Diagonal lines.
    int crossSum = (board[0][0] & 1)
                   + (board[1][1] & 1)
                   + (board[2][2] & 1)
                   + (board[3][3] & 1);
    int circleSum = (board[0][0] & 2)
                    + (board[1][1] & 2)
                    + (board[2][2] & 2)
                    + (board[3][3] & 2);
    if (crossSum == 4)
        return CROSS_WIN;
    else if (circleSum == 8)
        return CIRCLE_WIN;

    crossSum = (board[3][0] & 1)
               + (board[2][1] & 1)
               + (board[1][2] & 1)
               + (board[0][3] & 1);
    circleSum = (board[3][0] & 2)
                + (board[2][1] & 2)
                + (board[1][2] & 2)
                + (board[0][3] & 2);
    if (crossSum == 4)
        return CROSS_WIN;
    else if (circleSum == 8)
        return CIRCLE_WIN;

    // NOT_COMPLETE?
    for (int row = 0; row < 4; ++row)
        for (int col = 0; col < 4; ++col)
            if (board[row][col] == EMPTY)
                return NOT_COMPLETE;

    return DRAW;
}

int main ()
{
    int T;
    int caseCount = 0;
    cin >> T;
    while ( T-- )
    {
        caseCount++;
        int board[4][4];
        for (int row = 0; row < 4; ++row)
            for (int col = 0; col < 4; ++col)
            {
                char c;
                cin >> c;
                switch (c)
                {
                case ('.'):
                    board[row][col] = EMPTY;
                    break;
                case ('X'):
                    board[row][col] = CROSS;
                    break;
                case ('O'):
                    board[row][col] = CIRCLE;
                    break;
                case ('T'):
                    board[row][col] = TCell;
                    break;
                }
            }

        int result = gameResult(board);
        cout << "Case #"
             << caseCount
             << ": ";
        switch (result)
        {
        case (CROSS_WIN):
            cout << "X won";
            break;
        case (CIRCLE_WIN):
            cout << "O won";
            break;
        case (DRAW):
            cout << "Draw";
            break;
        case (NOT_COMPLETE):
            cout << "Game has not completed";
            break;
        }
        cout << endl;
    }
    return 0;
}