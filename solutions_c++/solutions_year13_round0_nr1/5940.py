#include<stdio.h>

char grid[4][4];

int main()
{
    int T,i,j,cases=1;
    int x_win=0,y_win=0,draw;
    freopen("A-large.in","r",stdin);
    freopen("sub-4.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        getchar();
        x_win=0;
        y_win=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%c",&grid[i][j]);
            }
            getchar();
        }
        for(i=0;i<4;i++)
        {
            if((grid[i][0]=='X' || grid[i][0]=='T')&&(grid[i][1]=='X' || grid[i][1]=='T')&&(grid[i][2]=='X' || grid[i][2]=='T')&&(grid[i][3]=='X' || grid[i][3]=='T'))
            {
                x_win++;
            }
            else if((grid[i][0]=='O' || grid[i][0]=='T')&&(grid[i][1]=='O' || grid[i][1]=='T')&&(grid[i][2]=='O' || grid[i][2]=='T')&&(grid[i][3]=='O' || grid[i][3]=='T'))
            {
                y_win++;
            }
            if(x_win>0 || y_win>0)
                break;
        }
        for(i=0;i<4;i++)
        {
            if(x_win>0 || y_win>0)
                break;
            if((grid[0][i]=='X' || grid[0][i]=='T')&&(grid[1][i]=='X' || grid[1][i]=='T')&&(grid[2][i]=='X' || grid[2][i]=='T')&&(grid[3][i]=='X' || grid[3][i]=='T'))
            {
                x_win++;
            }
            else if((grid[0][i]=='O' || grid[0][i]=='T')&&(grid[1][i]=='O' || grid[1][i]=='T')&&(grid[2][i]=='O' || grid[2][i]=='T')&&(grid[3][i]=='O' || grid[3][i]=='T'))
            {
                y_win++;
            }
        }
        if((grid[0][0]=='X' || grid[0][0]=='T')&&(grid[1][1]=='X' || grid[1][1]=='T')&&(grid[2][2]=='X' || grid[2][2]=='T')&&(grid[3][3]=='X' || grid[3][3]=='T'))
        {
            x_win++;
        }
        else if((grid[0][0]=='O' || grid[0][0]=='T')&&(grid[1][1]=='O' || grid[1][1]=='T')&&(grid[2][2]=='O' || grid[2][2]=='T')&&(grid[3][3]=='O' || grid[3][3]=='T'))
        {
            y_win++;
        }
        if((grid[0][3]=='X' || grid[0][3]=='T')&&(grid[1][2]=='X' || grid[1][2]=='T')&&(grid[2][1]=='X' || grid[2][1]=='T')&&(grid[3][0]=='X' || grid[3][0]=='T'))
        {
            x_win++;
        }
        else if((grid[0][3]=='O' || grid[0][3]=='T')&&(grid[1][2]=='O' || grid[1][2]=='T')&&(grid[2][1]=='O' || grid[2][1]=='T')&&(grid[3][0]=='O' || grid[3][0]=='T'))
        {
            y_win++;
        }

        printf("Case #%d: ",cases++);

        if(x_win>0)
        {
            printf("X won\n");
        }
        else if(y_win>0)
        {
            printf("O won\n");
        }
        else
        {
            draw=1;
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    if(grid[i][j]=='.')
                    {
                        draw=0;
                    }
                }
            }
            if(draw==0)
            {
                printf("Game has not completed\n");
            }
            else printf("Draw\n");
        }
    }
    return 0;
}
