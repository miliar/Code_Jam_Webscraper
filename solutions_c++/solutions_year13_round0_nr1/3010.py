#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;
char st[10][10];
bool judge(char s)
{
    int i,j;
    for(i=1;i<=4;i++)
    {
        for(j=1;j<=4;j++)
        {
            if(st[i][j]==s||st[i][j]=='T');
            else break;
        }
        if(j==5)return 1;

        for(j=1;j<=4;j++)
        {
            if(st[j][i]==s||st[j][i]=='T');
            else break;
        }
        if(j==5)return 1;
    }
    for(i=1;i<=4;i++)
    {
        if(st[i][i]==s||st[i][i]=='T');
        else break;
    }
    if(i==5)return 1;
    for(i=1;i<=4;i++)
    {
        if(st[i][4-i+1]==s||st[i][4-i+1]=='T');
        else break;
    }
    if(i==5)return 1;

    return 0;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cas,ca=0,i,j;
    scanf("%d",&cas);
    while(cas--)
    {
        printf("Case #%d:",++ca);
        for(i=1;i<=4;i++)
        {
            scanf("%s",st[i]+1);
        }
        bool f=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(st[i][j]=='.')
                {
                    f=1;
                }
            }
        }
        if(judge('X'))printf(" X won\n");
        else if(judge('O'))printf(" O won\n");
        else if(f)printf(" Game has not completed\n");
        else printf(" Draw\n");
    }
    return 0;
}
