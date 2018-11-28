#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<map>
#include<queue>
#include<string>
#include<vector>
#include<ctime>
#include<stack>
#include<sstream>
using namespace std;
char s[10][10];
int check(int n)
{
    int i;
    for(i=0;i<4;i++)
        if(s[n][i]=='O' || s[n][i]=='.')
            break;
    if(i==4)return 1;
    for(i=0;i<4;i++)
        if(s[i][n]=='O' || s[i][n]=='.')
            break;
    if(i==4)return 1;
    for(i=0;i<4;i++)
        if(s[n][i]=='X' || s[n][i]=='.')
            break;
    if(i==4)return 2;
    for(i=0;i<4;i++)
        if(s[i][n]=='X' || s[i][n]=='.')
            break;
    if(i==4)return 2;
    return 0;
}
int check2()
{
    int i;
    for(i=0;i<4;i++)
        if(s[i][i]=='O' || s[i][i]=='.')
            break;
    if(i==4)return 1;
    for(i=0;i<4;i++)
        if(s[i][i]=='X' || s[i][i]=='.')
            break;
    if(i==4)return 2;
    for(i=0;i<4;i++)
        if(s[i][3-i]=='O' || s[i][3-i]=='.')
            break;
    if(i==4)return 1;
    for(i=0;i<4;i++)
        if(s[i][3-i]=='X' || s[i][3-i]=='.')
            break;
    if(i==4)return 2;
    return 0;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,tt=0,i,j;
    scanf("%d",&t);
    while(t--)
    {
        tt++;
        for(i=0;i<4;i++)scanf("%s",s[i]);
        for(i=0;i<4;i++)
        {
            if(check(i)==1)
            {
                printf("Case #%d: X won\n",tt);
                goto done;
            }
            else if(check(i)==2)
            {
                printf("Case #%d: O won\n",tt);
                goto done;
            }
        }
        if(check2()==1)
        {
            printf("Case #%d: X won\n",tt);
            goto done;
        }
        else if(check2()==2)
        {
            printf("Case #%d: O won\n",tt);
            goto done;
        }
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                if(s[i][j]=='.')
                {
                    printf("Case #%d: Game has not completed\n",tt);
                    goto done;
                }
        printf("Case #%d: Draw\n",tt);
        done:;
    }
    return 0;
}
