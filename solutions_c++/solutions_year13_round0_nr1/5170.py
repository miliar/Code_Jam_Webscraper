#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;
    char game[4][4];
    int results[T];
    bool complete, xWin, oWin;
    int xCount, oCount;
    char piece;
    for (int i = 0; i < T; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                cin >> piece;
                game[j][k] = piece;
            }
        }
        complete = true;
        xWin = false;
        oWin = false;
        xCount = 0;
        oCount = 0;
        for (int j = 0; j < 4; j++)
        {
            piece = game[j][j];
            if (piece == 'T')
            {
                xCount++;
                oCount++;
            }
            else if (piece == 'X')
                xCount++;
            else if (piece == 'O')
                oCount++;
            else
                complete = false;
        }
        if (xCount == 4)
            xWin = true;
        if (oCount == 4)
            oWin = true;

        xCount = 0;
        oCount = 0;
        for (int j = 0; j < 4; j++)
        {
            piece = game[j][3-j];
            if (piece == 'T')
            {
                xCount++;
                oCount++;
            }
            else if (piece == 'X')
                xCount++;
            else if (piece == 'O')
                oCount++;
            else
                complete = false;
        }
        if (xCount == 4)
            xWin = true;
        if (oCount == 4)
            oWin = true;

        for (int j = 0; j < 4; j++)
        {
            xCount = 0;
            oCount = 0;
            for (int k = 0; k < 4; k++)
            {
                piece = game[j][k];
                if (piece == 'T')
                {
                    xCount++;
                    oCount++;
                }
                else if (piece == 'X')
                    xCount++;
                else if (piece == 'O')
                    oCount++;
                else
                    complete = false;
            }
            if (xCount == 4)
                xWin = true;
            if (oCount == 4)
                oWin = true;
        }

        for (int j = 0; j < 4; j++)
        {
            xCount = 0;
            oCount = 0;
            for (int k = 0; k < 4; k++)
            {
                piece = game[k][j];
                if (piece == 'T')
                {
                    xCount++;
                    oCount++;
                }
                else if (piece == 'X')
                    xCount++;
                else if (piece == 'O')
                    oCount++;
                else
                    complete = false;
            }
            if (xCount == 4)
                xWin = true;
            if (oCount == 4)
                oWin = true;
        }

        if (xWin)
            results[i] = 0;
        else if (oWin)
            results[i] = 1;
        else if (complete)
            results[i] = 2;
        else
            results[i] = 3;
    }

    string zero = "X won";
    string one = "O won";
    string two = "Draw";
    string three = "Game has not completed";
    for (int i = 0; i < T; i++)
    {
        cout << "Case #" << (1 + i) << ": ";
        if (results[i] == 0)
            cout << zero << endl;
        else if (results[i] == 1)
            cout << one << endl;
        else if (results[i] == 2)
            cout << two << endl;
        else
            cout << three << endl;
    }
    return 0;
}
