#include <iostream>
#include <stdio.h>

using namespace std;

char board[5][5];

bool fill()
{
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            if(board[i][j] == '.')
                return false;
    return true;
}

bool xWins()
{
    int i, j, xNo, tNo;
    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[0][i] == 'X')  xNo++;
        if(board[0][i] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[1][i] == 'X')  xNo++;
        if(board[1][i] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[2][i] == 'X')  xNo++;
        if(board[2][i] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[3][i] == 'X')  xNo++;
        if(board[3][i] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;



    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[i][0] == 'X')  xNo++;
        if(board[i][0] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[i][1] == 'X')  xNo++;
        if(board[i][1] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[i][2] == 'X')  xNo++;
        if(board[i][2] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[i][3] == 'X')  xNo++;
        if(board[i][3] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;


    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[i][i] == 'X')  xNo++;
        if(board[i][i] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    xNo = 0;    tNo = 0;
    for(i = 0, j = 3; i < 4; i++, j--)
    {
        if(board[i][j] == 'X')  xNo++;
        if(board[i][j] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    return false;
}

bool oWins()
{
    int i, j, xNo, tNo;
    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[0][i] == 'O')  xNo++;
        if(board[0][i] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[1][i] == 'O')  xNo++;
        if(board[1][i] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[2][i] == 'O')  xNo++;
        if(board[2][i] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[3][i] == 'O')  xNo++;
        if(board[3][i] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;



    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[i][0] == 'O')  xNo++;
        if(board[i][0] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[i][1] == 'O')  xNo++;
        if(board[i][1] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[i][2] == 'O')  xNo++;
        if(board[i][2] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[i][3] == 'O')  xNo++;
        if(board[i][3] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;


    xNo = 0;    tNo = 0;
    for(i = 0; i < 4; i++)
    {
        if(board[i][i] == 'O')  xNo++;
        if(board[i][i] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    xNo = 0;    tNo = 0;
    for(i = 0, j = 3; i < 4; i++, j--)
    {
        if(board[i][j] == 'O')  xNo++;
        if(board[i][j] == 'T')  tNo++;
    }
    if((xNo == 4) || (xNo == 3 && tNo == 1))
        return true;

    return false;
}

bool draw()
{
    if(fill() && !xWins() && !oWins())
        return true;
    return false;
}

int main()
{
    //freopen("one.in", "r", stdin);
    //freopen("one.out", "w", stdout);
    int i, j, k, T, t;
    cin >> T;
    for(t = 1; t <= T; t++)
    {
        for(i = 0; i < 4; i++)
            for(j = 0; j < 4; j++)
                cin >> board[i][j];

        if(xWins())
            cout << "Case #" << t << ": X won\n";
        else if(oWins())
            cout << "Case #" << t << ": O won\n";
        else if(draw())
            cout << "Case #" << t << ": Draw\n";
        else
            cout << "Case #" << t << ": Game has not completed\n";

    }
    return 0;
}
