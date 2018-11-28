#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
char s[10][10];
int i,j,ans,sum,cnt,cas,k;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&cas);
    for (k=1;k<=cas;k++)
    {
    for (i=0;i<=3;i++)
    scanf("%s",s[i]);
    sum=0;
    ans=0;
    for (i=0;i<=3;i++)
    {
        cnt=0;
        for (j=0;j<=3;j++)
        if (s[i][j]=='.')sum++;
        for (j=0;j<=3;j++)
        if (s[i][j]=='X'||s[i][j]=='T')
        cnt++;
        if (cnt==4)
        ans=1;
        cnt=0;
        for (j=0;j<=3;j++)
        if (s[i][j]=='O'||s[i][j]=='T')
        cnt++;
        if (cnt==4)
        ans=2;
    }
    for (i=0;i<=3;i++)
    {
        cnt=0;
        for (j=0;j<=3;j++)
        if (s[j][i]=='X'||s[j][i]=='T')
        cnt++;
        if (cnt==4)
        ans=1;
        cnt=0;
        for (j=0;j<=3;j++)
        if (s[j][i]=='O'||s[j][i]=='T')
        cnt++;
        if (cnt==4)
        ans=2;
    }
    cnt=0;
    for (i=0;i<=3;i++)
    if (s[i][i]=='X'||s[i][i]=='T')
    cnt++;
    if (cnt==4)
    ans=1;
    cnt=0;
        for (i=0;i<=3;i++)
    if (s[i][i]=='O'||s[i][i]=='T')
    cnt++;
    if (cnt==4)
    ans=2;
    cnt=0;
    for (i=0;i<=3;i++)
    if (s[i][3-i]=='X'||s[i][3-i]=='T')
    cnt++;
    if (cnt==4)
    ans=1;
    cnt=0;
    for (i=0;i<=3;i++)
    if (s[i][3-i]=='O'||s[i][3-i]=='T')
    cnt++;
    if (cnt==4)
    ans=2;
    if (ans==0&&sum)
    ans=3;
    else if (ans==0&&sum==0)ans=4;
    printf("Case #%d: ",k);
    if (ans==1)
    printf("X won\n");
    else if (ans==2)printf("O won\n");
    else if (ans==3)printf("Game has not completed\n");
    else printf("Draw\n");
    }
    return 0;
}
