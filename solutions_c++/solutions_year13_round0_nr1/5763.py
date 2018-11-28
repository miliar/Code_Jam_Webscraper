#include<iostream>
#include<fstream>
using namespace std;
ifstream fin;
ofstream fout;
void deal(int);
char g[5][5];

int main()
{
    fin.open("gcj2013-Q-A.in");
    fout.open("gcj2013-Q-A.out");
    int t;
    fin>>t;
    for (int i=0;i<t;i++)
        deal(i);
}

void deal(int p)
{
    for (int i=0;i<4;i++)
    {
        for (int j=0;j<4;j++)
            fin>>g[i][j];
        fin.get();
    }
    fin.get();
    char c;
    bool flag;
    for (int i=0;i<4;i++)
    {
        flag=true;
        c=g[i][0];
        if (c=='.') 
        {
            flag=false;
            continue;
        }
        for (int j=1;j<4;j++)
            if (!(g[i][j]==c || g[i][j]=='T'))
            {
                flag=false;
                break;
            }
        if (flag) break;
    }
    if (!flag)
    {
        for (int i=0;i<4;i++)
        {
            c=g[0][i];
            flag=true;
            if (c=='.') 
            {
                flag=false;
                continue;
            }
            for (int j=1;j<4;j++)
                if (!(g[j][i]==c || g[i][j]=='T'))
                {
                    flag=false;
                    break;
                }
            if (flag) break;
        }
    }
    if (!flag)
    {
        flag=true;
        c=g[0][0];
        if (c!='.')
        {
            for (int i=1;i<4;i++)
                if (!(g[i][i]==c || g[i][i]=='T'))
                {
                    flag=false;
                    break;
                }
        }
        else flag=false;
    }
    if (!flag)
    {
        flag=true;
        c=g[0][3];
        if (c!='.')
        {
            for (int i=1;i<4;i++)
                if (!(g[i][3-i]==c || g[i][3-i]=='T'))
                {
                    flag=false;
                    break;
                }
        }
        else flag=false;
    }
    fout<<"Case #"<<p+1<<": ";
    if (flag)
    {
        fout<<c<<" won"<<endl;
    }
    else 
    {
        flag=false;
        for (int i=0;i<4;i++)
        {
            for (int j=0;j<4;j++)
                if (g[i][j]=='.')
                {
                    flag=true;
                    break;
                }
            if (flag) break;
        }
        if (flag)
            fout<<"Game has not completed"<<endl;
        else
            fout<<"Draw"<<endl;
    }           
}
