#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


int solve (vector < vector <char> > & board)
{
    int ocount_row, xcount_row, ocount_col,xcount_col;
    bool dot = false;
    for (int i = 0; i < 4; i++)
    {
        ocount_row = 0; xcount_row = 0;
        ocount_col = 0; xcount_col = 0;
        for (int j = 0; j < 4; j++)
        {
            if (board[i][j] == '.' )
                dot = true;
            if ( board[i][j] == 'X' )
                xcount_row ++;
            if ( board[i][j] == 'O')
                ocount_row ++;
            if (board[i][j] == 'T')
            {
                ocount_row ++;
                xcount_row ++;
            }
            if ( board[j][i] == 'X' )
                xcount_col ++;
            if ( board[j][i] == 'O')
                ocount_col ++;
            if (board[j][i] == 'T')
            {
                ocount_col ++;
                xcount_col ++;
            }
        }
        if (xcount_col >=4 || xcount_row >=4 || ocount_col >= 4 || ocount_row >=4)
            break;

    }
    int xdigc, odigc;
    xdigc = 0; odigc = 0;

    for (int i = 0; i < 4; i ++)
    {
        if ( board[i][i] == 'X' )
            xdigc ++;
        if ( board[i][i] == 'O')
            odigc ++;
        if (board[i][i] == 'T')
        {
            xdigc ++;
            odigc ++;
        }
    }

    int xdigc2, odigc2;
    xdigc2 = 0; odigc2 = 0;

    for (int i = 0; i < 4; i ++)
    {
        if ( board[3-i][i] == 'X' )
            xdigc2 ++;
        if ( board[3-i][i] == 'O')
            odigc2 ++;
        if (board[3-i][i] == 'T')
        {
            xdigc2 ++;
            odigc2 ++;
        }
    }

    if (xcount_row >=4 || xcount_col >=4 || xdigc >= 4 || xdigc2 >=4)
        return 1;
    if (ocount_row >= 4 || ocount_col >=4 || odigc >=4 || odigc2 >=4)
        return 2;
    if (!dot)
        return 3;
    else
        return 4;
}


int main ()
{
    int cases;
    ifstream f1 ("input");
    ofstream f2 ("output");

    f1 >> cases;

    for (int i = 0; i < cases; i++)
    {
        vector < vector < char > > board;
        {
            for (int j = 0; j < 4; j++)
            {
                vector <char> row;
                for (int k = 0; k < 4; k ++)
                {
                    char temp;
                    f1 >> temp;
                    row.push_back(temp);
                }
                board.push_back(row);
            }
            int s = solve (board);
            f2 << "Case #" << i + 1<<": ";
            if (s == 1)
                f2 << "X won" << endl;
            if (s == 2)
                f2 << "O won" << endl;
            if (s == 3)
                f2 << "Draw" << endl;
            if (s == 4)
                f2 << "Game has not completed" <<endl;
        }
    }
    return 0;
}


