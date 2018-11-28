#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
char m[5][5];
int main()
{
    int t;
    bool isend;
    int cas=1;
    //freopen("A-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>t;
    while(cas<=t)
    {
        isend=true;
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                cin>>m[i][j];
        int num1,num2;
        bool won1,won2;
        won1=false;
        won2=false;
        for(int i=1; i<=4; i++)
        {
            num1=num2=0;
            for(int j=1; j<=4; j++)
            {
                if(m[i][j]=='.')
                {
                    isend=false;
                    continue;
                }
                if(m[i][j]=='X' || m[i][j]=='T')num1++;
                if(m[i][j]=='O' || m[i][j]=='T')num2++;
            }
            if(num1==4)
            {
                won1=true;
                break;
            }
            if(num2==4)
            {
                won2=true;
                break;
            }
        }
        if(won1==false && won2==false)
        {

            for(int i=1; i<=4; i++)
            {
                num1=num2=0;
                for(int j=1; j<=4; j++)
                {
                    if(m[j][i]=='.')
                    {
                        isend=false;
                        continue;
                    }
                    if(m[j][i]=='X' || m[j][i]=='T')num1++;
                    if(m[j][i]=='O' || m[j][i]=='T')num2++;
                }
                if(num1==4)
                {
                    won1=true;
                    break;
                }
                if(num2==4)
                {
                    won2=true;
                    break;
                }

            }
        }
        if(won1==false && won2==false)
        {
            num1=num2=0;
            for(int i=1; i<=4; i++)
            {
                if(m[i][i]=='X' || m[i][i]=='T')num1++;
                if(m[i][i]=='O' || m[i][i]=='T')num2++;
            }
            if(num1==4)
            {
                won1=true;
            }
            if(num2==4)
            {
                won2=true;
            }
            num1=num2=0;
            for(int i=1; i<=4; i++)
            {
                if(m[i][5-i]=='X' || m[i][5-i]=='T')num1++;
                if(m[i][5-i]=='O' || m[i][5-i]=='T')num2++;
            }
            if(num1==4)
            {
                won1=true;
            }
            if(num2==4)
            {
                won2=true;
            }

        }
        printf("Case #%d: ",cas++);
        if(won1)printf("X won\n");
        else if(won2)printf("O won\n");
        else if(isend)printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
