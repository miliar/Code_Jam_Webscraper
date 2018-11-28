#include <iostream>
#include <cstdio>
using namespace std;
int s[10][10];
char ss[10][10];

bool func(int x)
{
    int ii,jj;
    int aa=0;
    for(int i=0;i<=3;i++)
    {
        for(int j=0;j<=3;j++)
        {
            if(s[i][j]==3)
            {
                s[i][j]=x;
                ii=i,jj=j;
                aa=1;
            }
        }
    }
    int flag=0;
    if(s[0][0]==x && s[0][1]==x && s[0][2]==x && s[0][3]==x)flag=1;
    else if(s[1][0]==x && s[1][1]==x && s[1][2]==x && s[1][3]==x)flag=1;
    else if(s[2][0]==x && s[2][1]==x && s[2][2]==x && s[2][3]==x)flag=1;
    else if(s[3][0]==x && s[3][1]==x && s[3][2]==x && s[3][3]==x)flag=1;
    else if(s[0][0]==x && s[1][0]==x && s[2][0]==x && s[3][0]==x)flag=1;
    else if(s[0][1]==x && s[1][1]==x && s[2][1]==x && s[3][1]==x)flag=1;
    else if(s[0][2]==x && s[1][2]==x && s[2][2]==x && s[3][2]==x)flag=1;
    else if(s[0][3]==x && s[1][3]==x && s[2][3]==x && s[3][3]==x)flag=1;
    else if(s[0][0]==x && s[1][1]==x && s[2][2]==x && s[3][3]==x)flag=1;
    else if(s[0][3]==x && s[1][2]==x && s[2][1]==x && s[3][0]==x)flag=1;
    if(aa==1)s[ii][jj]=3;
    if(flag==1)return true;
    else return false;
}

bool find_(int x)
{
    int flag=0;
    for(int i=0;i<=3;i++)
    {
        for(int j=0;j<=3;j++)
        {
            if(s[i][j]==x)flag=1;
        }
    }
    if(flag==1)return true;
    else return false;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int num=1;
    int cas ;
    scanf("%d",&cas);
    while(cas--)
    {
        for(int j=0;j<=3;j++)
        {
            getchar();
            scanf("%s",ss[j]);
        }

        for(int i=0;i<=3;i++)
        {
            for(int j=0;j<=3;j++)
            {
                if(ss[i][j]=='O')s[i][j]=1;
                else if(ss[i][j]=='X')s[i][j]=2;
                else if(ss[i][j]=='T')s[i][j]=3;
                else if(ss[i][j]=='.')s[i][j]=0;
            }
        }
        if(func(1)==true)
        {
            printf("Case #%d: O won\n",num++);
            continue;
        }
        if(func(2)==true)
        {
            printf("Case #%d: X won\n",num++);
            continue;
        }
        if(!find_(0))
        printf("Case #%d: Draw\n",num++);
        else
        printf("Case #%d: Game has not completed\n",num++);
    }
    return 0;
}

