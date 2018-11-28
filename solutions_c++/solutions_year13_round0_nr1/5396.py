#include <iostream>
#include <fstream>

using namespace std;
char c[4][4];

bool rowo()
{
    for(int i=0; i<4; i++)
    {
        if((c[i][0]=='O' || c[i][0]=='T') &&
           (c[i][1]=='O' || c[i][1]=='T') &&
           (c[i][2]=='O' || c[i][2]=='T') &&
           (c[i][3]=='O' || c[i][3]=='T'))
           return true;
    }
    return false;
}

bool rowx()
{
    for(int i=0; i<4; i++)
    {
        if((c[i][0]=='X' || c[i][0]=='T') &&
           (c[i][1]=='X' || c[i][1]=='T') &&
           (c[i][2]=='X' || c[i][2]=='T') &&
           (c[i][3]=='X' || c[i][3]=='T'))
           return true;
    }
    return false;
}

bool colx()
{
    for(int i=0; i<4; i++)
    {
        if((c[0][i]=='X' || c[0][i]=='T') &&
           (c[1][i]=='X' || c[1][i]=='T') &&
           (c[2][i]=='X' || c[2][i]=='T') &&
           (c[3][i]=='X' || c[3][i]=='T'))
           return true;
    }
    return false;
}

bool colo()
{
    for(int i=0; i<4; i++)
    {
        if((c[0][i]=='O' || c[0][i]=='T') &&
           (c[1][i]=='O' || c[1][i]=='T') &&
           (c[2][i]=='O' || c[2][i]=='T') &&
           (c[3][i]=='O' || c[3][i]=='T'))
           return true;
    }
    return false;
}

bool diagO()
{
     if((c[0][0]=='O' || c[0][0]=='T') &&
           (c[1][1]=='O' || c[1][1]=='T') &&
           (c[2][2]=='O' || c[2][2]=='T') &&
           (c[3][3]=='O' || c[3][3]=='T'))
           return true;

    if((c[0][3]=='O' || c[0][0]=='T') &&
           (c[1][2]=='O' || c[1][2]=='T') &&
           (c[2][1]=='O' || c[2][1]=='T') &&
           (c[3][0]=='O' || c[3][0]=='T'))
           return true;
    return false;
}

bool diagX()
{
     if((c[0][0]=='X' || c[0][0]=='T') &&
           (c[1][1]=='X' || c[1][1]=='T') &&
           (c[2][2]=='X' || c[2][2]=='T') &&
           (c[3][3]=='X' || c[3][3]=='T'))
           return true;

    if((c[0][3]=='X' || c[0][3]=='T') &&
           (c[1][2]=='X' || c[1][2]=='T') &&
           (c[2][1]=='X' || c[2][1]=='T') &&
           (c[3][0]=='X' || c[3][0]=='T'))
           return true;
    return false;
}

int main()
{
    ofstream out;
    out.open ("out.txt");
    ifstream in;
    in.open("A-small-attempt0.in");
    int t;
    in>>t;
    int temp=0;
    while(t!=0)
    {
        t--;
        temp++;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                in>>c[i][j];
            }
        }
        if(rowx()||colx()||diagX())
        {
            out<<"Case #"<<temp<<": X won"<<endl;
        }
        else if(rowo() || colo() || diagO())
        {
            out<<"Case #"<<temp<<": O won"<<endl;
        }
        else
        {
            bool flag=true;
            for(int i=0; i<4; i++)
            {
                for(int j=0; j<4; j++)
                {
                    if(c[i][j]=='.')
                    {
                        flag=false;
                    }
                }
            }
            if(flag)
            {
                out<<"Case #"<<temp<<": Draw"<<endl;
            }
            else
                out<<"Case #"<<temp<<": Game has not completed"<<endl;
        }
    }
    in.close();
    out.close();
}
