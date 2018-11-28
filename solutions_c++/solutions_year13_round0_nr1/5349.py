#include<stdio.h>
#include<string.h>
char grid[5][5];
int sx,sy;
bool win(char tar)
{
    grid[sx][sy]=tar;
    for(int i=0;i<4;i++)
    {
        int flag=1;
        for(int j=0;j<4;j++) if(grid[i][j]!=tar)
            flag=0;
        if(flag)
            return true;
    }
    for(int i=0;i<4;i++)
    {
        int flag=1;
        for(int j=0;j<4;j++) if(grid[j][i]!=tar)
            flag=0;
        if(flag)
            return true;
    }
    int flag=1;
    for(int i=0;i<4;i++) if(grid[i][i]!=tar)
        flag=0;
    if(flag)
        return true;
    flag=1;
    for(int i=0;i<4;i++) if(grid[i][3-i]!=tar)
        flag=0;
    if(flag)
        return true;
    return false;
}
bool draw()
{
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++) if(grid[i][j]=='.')
            return false;
    return true;
}
int doit()
{
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++) if(grid[i][j]=='T')
            sx=i,sy=j;
    if(win('X'))
        return 1;
    else if(win('O'))
        return -1;
    else if(draw())
        return 0;
    return -2;
}
int main()
{
    int T;
    int ca=0;
    //freopen("in.in","r",stdin);
   // freopen("a.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        for(int i=0;i<4;i++)
            scanf("%s",grid[i]);
        int res=doit();
        printf("Case #%d: ",++ca);
        if(res==1)
            printf("X won\n");
        else if(res==-1)
            printf("O won\n");
        else if(res==0)
            printf("Draw\n");
        else
            printf("Game has not completed\n");
    }

}
