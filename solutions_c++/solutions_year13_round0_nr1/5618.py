#include<iostream>
#include<string>
#include <stdio.h>
using namespace std;
int Ti,Tj;
bool checkX(char status[4][4]);
bool checkGameEnd(char status[4][4]);
bool checkO(char status[4][4]);
int main()
{
    int TT;
    cin>>TT;
    //freopen ("in1.txt","r",stdin);
    freopen ("outputsmall.txt","w",stdout);
    int count =0;
    while(TT--)
    {
        count++;

        bool xflag=false,yflag=false;
        char status[4][4];
        string flagd="undecided";

        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
            {
                cin>>status[i][j];
                if(status[i][j]=='.'){
                    flagd="Game has not completed";
                    }
                else if(status[i][j]=='T'){
                    Ti=i;
                    Tj=j;
                }
            }


        if(checkX(status))
            cout<<"Case #"<<count<<": "<<"X won"<<endl;
        else if(checkO(status))
            cout<<"Case #"<<count<<": "<<"O won"<<endl;
        else if(checkGameEnd(status))
            cout<<"Case #"<<count<<": "<<"Draw"<<endl;
        else
            cout<<"Case #"<<count<<": "<<"Game has not completed"<<endl;

    }
    fclose(stdout);
    return 0;
}


bool checkX(char status[4][4])
{
    status[Ti][Tj] = 'X';
    for(int i=0;i<4;++i)
        {
        if(status[i][0]=='X' && status[i][1]=='X' && status[i][2]=='X' && status[i][3]=='X')
        {

            return true;

        }
        else if(status[0][i]=='X' && status[1][i]=='X' && status[2][i]=='X'  && status[3][i]=='X')
        {


            return true;
        }


        }
        if(status[0][0]=='X' && status[1][1]=='X' && status[2][2]=='X' && status[3][3]=='X')
        {

             return true;

        }
        else if(status[3][0]=='X' && status[2][1]=='X' && status[1][2]=='X' && status[0][3]=='X')
        {

             return true;

        }
        else
            return false;

}


bool checkO(char status[4][4])
{
status[Ti][Tj]='O';
        for(int i=0;i<4;++i)
        {
        if(status[i][0]=='O' && status[i][1]=='O' && status[i][2]=='O' && status[i][3]=='O')
        {
            return true;

        }
        else if(status[0][i]=='O' && status[1][i]=='O' && status[2][i]=='O' && status[3][i]=='O')
        {

            return true;
        }

        }
          if(status[0][0]=='O' && status[1][1]=='O'  && status[2][2]=='O' && status[3][3]=='O')
        {

            return true;
        }
        else if(status[3][0]=='O' && status[2][1]=='O' && status[1][2]=='O' && status[0][3]=='O')
        {
            return true;

        }
        else
            return false;
}


bool checkGameEnd(char status[4][4])
{
    bool flag = false;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
    {
        if(status[i][j]=='.')
        {
            return false;

        }
        else flag = true;

    }
    if (flag)
        return true;
}


