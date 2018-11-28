#include<iostream>
#include<string>

using namespace std;

char board[4][4];
#define XWINS "X won"
#define OWINS "O won"
#define DRAW "Draw"
#define NOTDONE "Game has not completed"
string test()
{
    bool notcomplete=false;
    for(int i=0;i<4;i++)
    {
        bool xholds=true, oholds=true;
        int T=0;
        for(int j=0;j<4;j++)
        {
            if(board[i][j]=='X')
                oholds=false;
            if(board[i][j]=='O')
                xholds=false;
            if(board[i][j]=='T')
            {
                T++;
                if(T==2)
                {
                    oholds=xholds=false;
                }
            }
            if(board[i][j]=='.')
            {
                notcomplete=true;
                oholds=xholds=false;
            }
        }
        if(xholds) return XWINS;
        if(oholds) return OWINS;
    }
    for(int j=0;j<4;j++)
    {
        bool xholds=true, oholds=true;
        int T=0;
        for(int i=0;i<4;i++)
        {
            if(board[i][j]=='X')
                oholds=false;
            if(board[i][j]=='O')
                xholds=false;
            if(board[i][j]=='T')
            {
                T++;
                if(T==2)
                {
                    oholds=xholds=false;
                }
            }
            if(board[i][j]=='.')
            {
                notcomplete=true;
                oholds=xholds=false;
            }
        }
        if(xholds) return XWINS;
        if(oholds) return OWINS;
    }
    bool xholds=true, oholds=true;
    int T=0;
    for(int i=0;i<4;i++)
    {
        if(board[i][i]=='X')
            oholds=false;
        if(board[i][i]=='O')
            xholds=false;
        if(board[i][i]=='T')
        {
            T++;
            if(T==2)
            {
                oholds=xholds=false;
            }
        }
        if(board[i][i]=='.')
        {
            notcomplete=true;
            oholds=xholds=false;
        }

    }
    if(xholds) return XWINS;
    if(oholds) return OWINS;
    xholds=true, oholds=true;
    T=0;
    for(int i=0;i<4;i++)
    {
        if(board[i][3-i]=='X')
            oholds=false;
        if(board[i][3-i]=='O')
            xholds=false;
        if(board[i][3-i]=='T')
        {
            T++;
            if(T==2)
            {
                oholds=xholds=false;
            }
        }
        if(board[i][3-i]=='.')
        {
            notcomplete=true;
            oholds=xholds=false;
        }

    }
    if(xholds) return XWINS;
    if(oholds) return OWINS;
    if(notcomplete)
        return NOTDONE;
    else
        return DRAW;
}

int main()
{
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>board[i][j];
            }
        }
        cout<<"Case #"<<k<<": "<<test()<<endl;
    }
    return 0;
}
