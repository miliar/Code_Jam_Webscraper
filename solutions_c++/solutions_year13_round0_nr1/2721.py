#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
char str[5][5];
int judge()
{
    bool isdraw=true;
    int O,X,T;
    for(int i=0; i<4; i++)
    {
        O=X=T=0;
        for(int j=0; j<4; j++)
        {
            if(str[i][j]=='O')
                O++;
            else if(str[i][j]=='X')
                X++;
            else if(str[i][j]=='T')
            {
                if(!T)
                    T=1;
            }
            else isdraw=false;
        }
        if(O+T==4)
            return 1;
        if(X+T==4)
            return 2;
    }
    for(int j=0; j<4; j++)
    {
        O=X=T=0;
        for(int i=0; i<4; i++)
        {
            if(str[i][j]=='O')
                O++;
            else if(str[i][j]=='X')
                X++;
            else if(str[i][j]=='T')
            {
                if(!T)
                    T=1;
            }
            else isdraw=false;
        }
        if(O+T==4)
            return 1;
        if(X+T==4)
            return 2;
    }
    O=X=T=0;
    for(int i=0; i<4; i++)
    {
        if(str[i][i]=='O')
            O++;
        else if(str[i][i]=='X')
            X++;
        else if(str[i][i]=='T')
            T++;
    }
    if(O+T==4)
        return 1;
    if(X+T==4)
        return 2;
    O=X=T=0;
    for(int i=0; i<4; i++)
    {
        if(str[i][3-i]=='O')
            O++;
        else if(str[i][3-i]=='X')
            X++;
        else if(str[i][3-i]=='T')
            T++;
    }
    if(O+T==4)
        return 1;
    if(X+T==4)
        return 2;
    if(isdraw)
        return 3;
    else return 4;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1; cas<=t; cas++)
    {
        for(int i=0; i<4; i++)
            scanf("%s",str[i]);
        printf("Case #%d: ",cas);
        int type=judge();
        if(type==1)
            cout<<"O won"<<endl;
        else if(type==2)
            cout<<"X won"<<endl;
        else if(type==3)
            cout<<"Draw"<<endl;
        else cout<<"Game has not completed"<<endl;
    }
}
