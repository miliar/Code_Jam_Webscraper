#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
    //freopen("E:\\A-large.in","r",stdin);
    //freopen("E:\\A-large.out","w",stdout);
    bool completed;
    char board[8][8];
    int T,O,X;
    cin>>T;
    for(int t=1;t<=T;++t)
    {
        for(int i=0;i<4;++i)
        {
            cin>>board[i];
        }
        for(int i=0;i<4;++i)
        {
            O=X=0;
            for(int j=0;j<4;++j)
            {
                if(board[i][j]=='O')
                {
                    ++O;
                }
                else if(board[i][j]=='X')
                {
                    ++X;
                }
                else if(board[i][j]=='T')
                {
                    ++O;
                    ++X;
                }
            }
            if(O==4||X==4)break;
            O=X=0;
            for(int j=0;j<4;++j)
            {
                if(board[j][i]=='O')
                {
                    ++O;
                }
                else if(board[j][i]=='X')
                {
                    ++X;
                }
                else if(board[j][i]=='T')
                {
                    ++O;
                    ++X;
                }
            }
            if(O==4||X==4)break;
        }
        if(O!=4&&X!=4)
        {
            O=X=0;
            for(int i=0;i<4;++i)
            {
                if(board[i][i]=='O')
                {
                    ++O;
                }
                else if(board[i][i]=='X')
                {
                    ++X;
                }
                else if(board[i][i]=='T')
                {
                    ++O;
                    ++X;
                }
            }
            if(O!=4&&X!=4)
            {
                O=X=0;
                for(int i=0,j=3;i<4;++i,--j)
                {
                    if(board[i][j]=='O')
                    {
                        ++O;
                    }
                    else if(board[i][j]=='X')
                    {
                        ++X;
                    }
                    else if(board[i][j]=='T')
                    {
                        ++O;
                        ++X;
                    }
                }
            }
        }
        cout<<"Case #"<<t<<": ";
        if(O==4)
        {
            cout<<"O won\n";
        }
        else if(X==4)
        {
            cout<<"X won\n";
        }
        else
        {
            completed=true;
            for(int i=0;i<4;++i)
            {
                for(int j=0;j<4;++j)
                {
                    if(board[i][j]=='.')
                    {
                        completed=false;
                        break;
                    }
                }
            }
            if(completed)
            {
                cout<<"Draw\n";
            }
            else
            {
                cout<<"Game has not completed\n";
            }
        }
        cin.get();
    }
}
