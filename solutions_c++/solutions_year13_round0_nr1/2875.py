#include <iostream>
#include <fstream>

using namespace std;

char board[4][5];

int status()
{
    int cX,cO;
    for(int i=0;i<4;i++)
    {
        cX=0;
        cO=0;
        for(int j=0;j<4;j++)
        {
            if(board[i][j]=='X')
            {
                cX++;
            }
            if(board[i][j]=='O')
            {
                cO++;
            }
            if(board[i][j]=='T')
            {
                cX++;
                cO++;
            }
        }
        if(cX==4)
        {
            return 1;
        }
        if(cO==4)
        {
            return 2;
        }
    }
    for(int j=0;j<4;j++)
    {
        cX=0;
        cO=0;
        for(int i=0;i<4;i++)
        {
            if(board[i][j]=='X')
            {
                cX++;
            }
            if(board[i][j]=='O')
            {
                cO++;
            }
            if(board[i][j]=='T')
            {
                cX++;
                cO++;
            }
        }
        if(cX==4)
        {
            return 1;
        }
        if(cO==4)
        {
            return 2;
        }
    }
    cX=0;
    cO=0;
    for(int i=0,j=0;i<4&&j<4;i++,j++)
    {
        if(board[i][j]=='X')
        {
            cX++;
        }
        if(board[i][j]=='O')
        {
            cO++;
        }
        if(board[i][j]=='T')
        {
            cX++;
            cO++;
        }
    }
    if(cX==4)
    {
        return 1;
    }
    if(cO==4)
    {
        return 2;
    }
    cX=0;
    cO=0;
    for(int i=0,j=3;i<4&&j>=0;i++,j--)
    {
        if(board[i][j]=='X')
        {
            cX++;
        }
        if(board[i][j]=='O')
        {
            cO++;
        }
        if(board[i][j]=='T')
        {
            cX++;
            cO++;
        }
    }
    if(cX==4)
    {
        return 1;
    }
    if(cO==4)
    {
        return 2;
    }
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(board[i][j]=='.')
            {
                return 3;
            }
        }
    }
    return 4;
}

int main()
{
    ifstream fin;
    fin.open("in.txt",ios::in);
    ofstream fout;
    fout.open("out.txt",ios::out|ios::trunc);
    int t;
    fin>>t;
    char *ans[4]={"X won","O won","Game has not completed","Draw"};
    for(int i=0;i<t;i++)
    {
        for(int j=0;j<4;j++)
        {
            fin>>board[j];
        }
        int key=status();
        fout<<"Case #"<<(i+1)<<": "<<ans[(key-1)]<<endl;
    }
    return 0;
}
