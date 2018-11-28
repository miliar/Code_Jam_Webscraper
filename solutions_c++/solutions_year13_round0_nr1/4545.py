#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <math.h>
#include <string>
#include <map>
#include <queue>
#include <sstream>

using namespace std;

int T;
string mat[4];
int cas = 0;
bool f;
void  Xwon()
{
    cout<<"Case #"<<++cas<<": X won"<<endl;
    f = false;
}
void  Owon()
{
    cout<<"Case #"<<++cas<<": O won"<<endl;
    f = false;
}
void  Draw()
{
    cout<<"Case #"<<++cas<<": Draw"<<endl;
    f = false;
}
void  Not()
{
    cout<<"Case #"<<++cas<<": Game has not completed"<<endl;
    f = false;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    while(T--)
    {
        f = true;
        for(int i = 0; i < 4; i++)
            cin>>mat[i];
        for(int i = 0; i < 4 && f; i++)
        {
            int nx,no,nt;
            nx = no = nt = 0;
            for(int j = 0; j < 4; j++)
            {
                switch(mat[i][j])
                {
                case 'X':
                    nx++;
                    break;
                case 'O':
                    no++;
                    break;
                case 'T':
                    nt++;
                    break;
                }
            }
            if(nx == 4 || (nx == 3 && nt == 1))
                Xwon();
            if(no == 4 || (no == 3 && nt == 1))
                Owon();
        }

        for(int j = 0; j < 4 && f; j++)
        {
            int nx,no,nt;
            nx = no = nt = 0;
            for(int i = 0; i < 4; i++)
            {
                switch(mat[i][j])
                {
                case 'X':
                    nx++;
                    break;
                case 'O':
                    no++;
                    break;
                case 'T':
                    nt++;
                    break;
                }
            }
            if(nx == 4 || (nx == 3 && nt == 1))
                Xwon();
            if(no == 4 || (no == 3 && nt == 1))
                Owon();
        }
        int nx,no,nt;
        nx = no = nt = 0;
        for(int i = 0; i < 4 && f; i++)
        {
            switch(mat[i][i])
            {
            case 'X':
                nx++;
                break;
            case 'O':
                no++;
                break;
            case 'T':
                nt++;
                break;
            }
        }

        if(nx == 4 || (nx == 3 && nt == 1))
            Xwon();
        if(no == 4 || (no == 3 && nt == 1))
            Owon();

        nx = no = nt = 0;
        for(int i = 0; i < 4 && f; i++)
        {
            switch(mat[i][3 - i])
            {
            case 'X':
                nx++;
                break;
            case 'O':
                no++;
                break;
            case 'T':
                nt++;
                break;
            }
        }

        if(nx == 4 || (nx == 3 && nt == 1))
            Xwon();
        if(no == 4 || (no == 3 && nt == 1))
            Owon();

        int cnt = 0;
        if(!f) continue;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                if(mat[i][j] == '.') cnt++;
        if(!cnt) Draw();
        else Not();
    }
    fclose(stdin);
    fclose(stdout);
}
