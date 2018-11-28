#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string status(string board[4])
{
    //beg of X won?
    bool X_won;
    for (int i=0; i<4; ++i)
    {
        X_won=true;
        for (int j=0; j<4; ++j)
            if (board[i].at(j)=='O'||board[i].at(j)=='.')
            {
                X_won=false;
                break;
            }
        if(X_won)
            return "X won";
    }
    for (int i=0; i<4; ++i)
    {
        X_won=true;
        for (int j=0; j<4; ++j)
            if (board[j].at(i)=='O'||board[j].at(i)=='.')
            {
                X_won=false;
                break;
            }
        if(X_won)
            return "X won";
    }
    X_won=true;
    for (int i=0; i<4; ++i)
        if (board[i].at(i)=='O'||board[i].at(i)=='.')
        {
            X_won=false;
            break;
        }
    if(X_won)
        return "X won";
    X_won=true;
    for (int i=0; i<4; ++i)
        if (board[3-i].at(i)=='O'||board[3-i].at(i)=='.')
        {
            X_won=false;
            break;
        }
    if(X_won)
        return "X won";
    //end of X won?
    ///////////////
    //beg of O won?
    bool O_won;
    for (int i=0; i<4; ++i)
    {
        O_won=true;
        for (int j=0; j<4; ++j)
            if (board[i].at(j)=='X'||board[i].at(j)=='.')
            {
                O_won=false;
                break;
            }
        if(O_won)
            return "O won";
    }
    for (int i=0; i<4; ++i)
    {
        O_won=true;
        for (int j=0; j<4; ++j)
            if (board[j].at(i)=='X'||board[j].at(i)=='.')
            {
                O_won=false;
                break;
            }
        if(O_won)
            return "O won";
    }
    O_won=true;
    for (int i=0; i<4; ++i)
        if (board[i].at(i)=='X'||board[i].at(i)=='.')
        {
            O_won=false;
            break;
        }
    if(O_won)
        return "O won";
    O_won=true;
    for (int i=0; i<4; ++i)
        if (board[3-i].at(i)=='X'||board[3-i].at(i)=='.')
        {
            O_won=false;
            break;
        }
    if(O_won)
        return "O won";
    //end of O won?
    ///////////////
    //beg of incomplete game?
    for (int i=0; i<4; ++i)
        for (int j=0; j<4; ++j)
            if (board[i].at(j)=='.')
                return "Game has not completed";
    //end of incomplete game?
    ///////////////
    return "Draw";
}

int main()
{
    int T;
    string board[4];
    ifstream in("A-large.in");
    ofstream out("A-large.out");
    in >> T;
    for (int i=1; i<=T ; ++i)
    {
        for (int j=0; j<4; ++j)
            in >> board[j];
        out << "Case #" << i << ": " << status(board) << endl;
    }
    return 0;
}
