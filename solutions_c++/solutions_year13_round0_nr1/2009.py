#include <iostream>
using namespace std;

char board[10][10];

bool isWin(char c)
{
    for(int i=1; i<=4; ++i)
    {
        bool win=true;
        for(int j=1; j<=4&&win; ++j)
            if(!(board[i][j]==c||board[i][j]=='T'))
                win=false;
        if(win) return true;
    }
    for(int j=1; j<=4; ++j)
    {
        bool win=true;
        for(int i=1; i<=4&&win; ++i)
            if(!(board[i][j]==c||board[i][j]=='T'))
                win=false;
        if(win) return true;
    }
    {
        bool win=true;
        for(int i=1; i<=4&&win; ++i)
            if(!(board[i][i]==c||board[i][i]=='T'))
                win=false;
        if(win) return true;
    }
    {
        bool win=true;
        for(int i=1; i<=4&&win; ++i)
            if(!(board[i][5-i]==c||board[i][5-i]=='T'))
                win=false;
        if(win) return true;
    }
    return false;
}

bool isFull()
{
    for(int i=1; i<=4; ++i)
        for(int j=1; j<=4; ++j)
            if(board[i][j]=='.')
                return false;
    return true;
}

int main()
{
    int numOfCases;
    cin>>numOfCases;
    for(int i=1; i<=numOfCases; ++i)
    {
        cout<<"Case #"<<i<<": ";
        for(int j=1; j<=4; ++j)
            cin>>(board[j]+1);
        if(isWin('O')) cout<<"O won";
        else if(isWin('X')) cout<<"X won";
        else if(isFull()) cout<<"Draw";
        else cout<<"Game has not completed";
        cout<<endl;
    }
    return 0;
}

