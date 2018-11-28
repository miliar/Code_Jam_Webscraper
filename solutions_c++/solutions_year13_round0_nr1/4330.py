#include<stdio.h>
char s[10][10];int t;
bool full()
{
    for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
            if(s[i][j]=='.')
                return false;
    return true;
}
bool line(int i,char ch)
{
    for(int j=1;j<=4;j++)
        if(s[i][j]!=ch && s[i][j]!='T')
            return false;
    return true;
}
bool col(int i,char ch)
{
    for(int j=1;j<=4;j++)
        if(s[j][i]!=ch && s[j][i]!='T')
            return false;
    return true;
}
bool d1(char ch)
{
    for(int i=1;i<=4;i++)
        if(s[i][i]!=ch && s[i][i]!='T')
            return false;
    return true;
}
bool d2(char ch)
{
    for(int i=1;i<=4;i++)
        if(s[i][5-i]!=ch && s[i][5-i]!='T')
            return false;
    return true;
}
void solve()
{
    gets(s[1]+1);
    gets(s[2]+1);
    gets(s[3]+1);
    gets(s[4]+1);
    for(int i=1;i<=4;i++)
        if(line(i,'O') || col(i,'O'))
            {
                printf("Case #%d: O won\n",++t);
                return;
            }
        else if(line(i,'X') || col(i,'X'))
            {
                printf("Case #%d: X won\n",++t);
                return;
            }
    if(d1('O') || d2('O'))
    {
        printf("Case #%d: O won\n",++t);
        return;
    }
    else if(d1('X') || d2('X'))
    {
        printf("Case #%d: X won\n",++t);
        return;
    }
    if(full())
    {
        printf("Case #%d: Draw\n",++t);
        return;
    }
    printf("Case #%d: Game has not completed\n",++t);
}
int main()
{
    ///freopen("f.in","r",stdin);
    ///freopen("f.out","w",stdout);
    int T;
    for(scanf("%d",&T),getchar();T;T--,getchar())
        solve();
    return 0;
}

