#include<stdio.h>
#include<string.h>
#include<stdlib.h>

bool vis[9][9];
char g[9][9];

char fun(int r, int c, int f)
{
    int t=0, x=0, o=0;
    for(int dx=0; dx<4; dx++)
    {
        if(f==1)
        {
            if(g[r+dx][c]=='X')x++;
            else if(g[r+dx][c]=='O')o++;
            else if(g[r+dx][c]=='T')t++;
        }
        else
        {
            if(g[r][c+dx]=='X')x++;
            else if(g[r][c+dx]=='O')o++;
            else if(g[r][c+dx]=='T')t++;
        }
    }

    if( (x==3 && t==1) || x==4 )return 'X';
    if( (o==3 && t==1) || o==4 )return 'O';

    return 'F';
}

char diag(int r, int c, int f)
{
    int t=0, x=0, o=0;
    for(int dx=0; dx<4; dx++)
    {
        if(f==1)
        {
            if( g[r+dx][c+dx]=='X' )x++;
            else if( g[r+dx][c+dx]=='O' )o++;
            else if( g[r+dx][c+dx]=='T' )t++;
        }
        else
        {
            if( g[r-dx][c+dx]=='X' )x++;
            else if( g[r-dx][c+dx]=='O' )o++;
            else if( g[r-dx][c+dx]=='T' )t++;
        }
    }

    if( (x==3 && t==1) || x==4 )return 'X';
    if( (o==3 && t==1) || o==4 )return 'O';

    return 'F';
}

int main()
{
    freopen("A.in","r", stdin);
    freopen("Aout.out","w",stdout);

    int T, kas=1, i, j;

    for(scanf("%d",&T); kas<=T; kas++)
    {
        scanf("%s",g[0]);
        scanf("%s",g[1]);
        scanf("%s",g[2]);
        scanf("%s",g[3]);

        bool game[3] = {0};
        char ch;
        for(i=0; i<4; i++)
        {
            ch = fun(0, i, 1);
            if(ch=='X')game[0]=1;
            else if(ch=='O') game[1]=1;

            ch = fun(i, 0, 2);
            if(ch=='X')game[0]=1;
            else if(ch=='O') game[1]=1;
        }

        ch = diag(0, 0, 1);
        if(ch=='X')game[0]=1;
        else if(ch=='O') game[1]=1;

        ch = diag(3, 0, 2);
        if(ch=='X')game[0]=1;
        else if(ch=='O') game[1]=1;

        if( !(game[0] || game[1]) )for(i=0; i<4; i++)for(j=0; j<4; j++)if(g[i][j]=='.') { game[2]=1;    i=4; break; }

        if(game[0])printf("Case #%d: X won\n",kas);
        else if(game[1])printf("Case #%d: O won\n",kas);
        else if(game[2])printf("Case #%d: Game has not completed\n",kas);
        else printf("Case #%d: Draw\n",kas);
    }

    return 0;
}
