#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
int T,tt;
char a[5][5];
int solve(char ch)
{
    int cntch,cnt;
    for(int i=0;i<4;i++)
    {
        cntch=0,cnt=0;
        for(int j=0;j<4;j++)
        {
            if(a[i][j]==ch)cntch++;
            else if(a[i][j]=='T')cnt++;
        }
        if(cntch==3&&cnt==1||cntch==4)return 1;

        cntch=0,cnt=0;
        for(int j=0;j<4;j++)
        {
            if(a[j][i]==ch)cntch++;
            else if(a[j][i]=='T')cnt++;
        }
        if(cntch==3&&cnt==1||cntch==4)return 1;
    }
    cntch=0,cnt=0;
    for(int i=0;i<4;i++)
    {
        if(a[i][i]==ch)cntch++;
        else if(a[i][i]=='T')cnt++;
    }
    if(cntch==3&&cnt==1||cntch==4)return 1;

    cntch=0,cnt=0;
    for(int i=0;i<4;i++)
    {
        if(a[i][3-i]==ch)cntch++;
        else if(a[i][3-i]=='T')cnt++;
    }
    if(cntch==3&&cnt==1||cntch==4)return 1;
    return 0;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out","w",stdout);
    scanf("%d",&T);
    tt=0;
    while(T--)
    {
        for(int i=0;i<4;i++)scanf("%s",a[i]);
        int fx,fo;
        int cnt=0;
        for(int i=0;i<4;i++)for(int j=0;j<4;j++)
        if(a[i][j]=='.')cnt++;
        fx=solve('X');
        fo=solve('O');
        printf("Case #%d: ",++tt);
        if(fx)puts("X won");
        else if(fo)puts("O won");
        else if(cnt==0)puts("Draw");
        else puts("Game has not completed");
    }
    return 0;
}
