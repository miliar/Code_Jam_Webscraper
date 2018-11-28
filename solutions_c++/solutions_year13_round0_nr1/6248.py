#include <cstdio>
char s[8][8];
bool check_line(int x,char c)
{
    int i;
    for (i=0; i<4; ++i)
        if (s[x][i]!=c && s[x][i]!='T')
            break;
    if (i<4)
        return false;
    return true;
}
bool check_row(int x,char c)
{
    int i;
    for (i=0; i<4; ++i)
        if (s[i][x]!=c && s[i][x]!='T')
            break;
    if (i<4)
        return false;
    return true;
}
bool diagonal1(char c)
{
    for (int i=0; i<4; ++i)
        if (s[i][i]!=c && s[i][i]!='T')
            return false;
    return true;
}
bool diagonal2(char c)
{
    if (s[0][3]!=c && s[0][3]!='T')
        return false;
    if (s[1][2]!=c && s[1][2]!='T')
        return false;
    if (s[2][1]!=c && s[2][1]!='T')
        return false;
    if (s[3][0]!=c && s[3][0]!='T')
        return false;
    return true;
}
bool X()
{
    int i;
    for (i=0; i<4; ++i)
        if (check_line(i,'X') || check_row(i,'X'))
            return true;
    if (diagonal1('X') || diagonal2('X'))
        return true;
    return false;
}
bool O()
{
    int i;
    for (i=0; i<4; ++i)
        if (check_line(i,'O') || check_row(i,'O'))
            return true;
    if (diagonal1('O') || diagonal2('O'))
        return true;
    return false;
}
bool draw()
{
    for (int i=0; i<4; ++i)
        for (int j=0; j<4; ++j)
            if (s[i][j]=='.')
                return false;
    return true;
}
int main()
{
//    freopen("A-small-attempt0.in","r",stdin);
//    freopen("A-small-attempt0.out","w",stdin);
    int i,j,T;
    scanf("%d",&T);
    for (int kcase=1; kcase<=T; ++kcase)
    {
        getchar();
        for (i=0; i<4; ++i)
            gets(s[i]);
        if (X())
            printf("Case #%d: X won\n",kcase);
        else if (O())
            printf("Case #%d: O won\n",kcase);
        else if (draw())
            printf("Case #%d: Draw\n",kcase);
        else
            printf("Case #%d: Game has not completed\n",kcase);
    }
    return 0;
}
