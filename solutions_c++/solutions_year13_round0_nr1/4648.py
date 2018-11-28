#include <iostream>

using namespace std;

void doCase()
{
    char board[16];
    for(int i=0; i<16; i++)
        cin >> board[i];

    bool tie=true;
    for(int row=0; row<4; row++)
    {
        bool xwon=true;
        bool owon=true;

        for(int col=0; col<4; col++)
        {
            if(board[4*row+col] == 'X')
                owon = false;
            else if(board[4*row+col] == '.')
            {
                owon = false;
                xwon = false;
                tie = false;
            }
            else if(board[4*row+col] == 'O')
                xwon = false;
        }
        if(xwon)
        {
            cout << "X won" << endl;
            return;
        }
        else if(owon)
        {
            cout << "O won" << endl;
            return;
        }
    }

    for(int col=0; col<4; col++)
    {
        bool xwon=true;
        bool owon=true;

        for(int row=0; row<4; row++)
        {
            if(board[4*row+col] == 'X')
                owon = false;
            else if(board[4*row+col] == '.')
            {
                owon = false;
                xwon = false;
                tie = false;
            }
            else if(board[4*row+col] == 'O')
                xwon = false;
        }
        if(xwon)
        {
            cout << "X won" << endl;
            return;
        }
        else if(owon)
        {
            cout << "O won" << endl;
            return;
        }

    }

    bool xwon=true;
    bool owon=true;
    for(int diag=0; diag<4; diag++)
    {
        if(board[4*diag+diag] == 'X')
            owon = false;
        else if(board[4*diag+diag] == '.')
        {
            owon = false;
            xwon = false;
            tie = false;
        }
        else if(board[4*diag+diag] == 'O')
            xwon = false;

    }
    if(xwon)
    {
        cout << "X won" << endl;
        return;
    }
    else if(owon)
    {
        cout << "O won" << endl;
        return;
    }

    xwon=owon=true;

    for(int diag=0; diag<4; diag++)
    {
        if(board[4*diag+3-diag] == 'X')
            owon = false;
        else if(board[4*diag+3-diag] == '.')
        {
            owon = false;
            xwon = false;
            tie = false;
        }
        else if(board[4*diag+3-diag] == 'O')
            xwon = false;

    }
    if(xwon)
    {
        cout << "X won" << endl;
    }
    else if(owon)
    {
        cout << "O won" << endl;
    }
    else if(tie)
    {
        cout << "Draw" << endl;
    }
    else
        cout << "Game has not completed" << endl;
}

int main()
{
    int sets;
    cin >> sets;
    for(int i=0; i<sets; i++)
    {
        cout << "Case #" << i+1 << ": ";
        doCase();
    }
}


