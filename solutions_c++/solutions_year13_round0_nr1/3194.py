#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char map[5][5];

int main()
{
    int n,c=0,toltal;
    scanf("%d",&n);
    getchar();
    while(n--)
    {
        c++;
        toltal=0;
        for(int i=0;i<=4;++i)
        {
            gets(map[i]);
        }
        printf("Case #%d: ",c);
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                if(map[i][j]!='.')
                    toltal++;
            }

        }
        int i,j;bool ok=false;
        for(i=0;i<4;++i)
        {
            char temp=map[i][0];
            if(temp=='T')
                temp=map[i][1];
            if(temp=='.')
                continue;
            for(j=0;j<4;++j)
            {
                if(map[i][j]!=temp&&map[i][j]!='T')
                   break;
            }
            if(j==4&&!ok)
                if(ok=true,temp=='X')
                    printf("X won\n");
                else if(ok=true,temp=='O')
                    printf("O won\n");
        }
        for(j=0;j<4;++j)
        {
            char temp=map[0][j];
            if(temp=='T')
                temp=map[1][j];
            if(temp=='.')
                continue;
            for(i=0;i<4;++i)
            {
                if(map[i][j]!=temp&&map[i][j]!='T')
                    break;
            }
            if(i==4&&!ok)
                if(ok=true,temp=='X')
                    printf("X won\n");
                else if(ok=true,temp=='O')
                    printf("O won\n");
        }
        char temp;
        for(i=0,j=0;i<4;++i,++j)
        {
            temp=map[0][0];
            if(temp=='T')
                temp=map[1][1];
            if(temp=='.')
                break;
            if(map[i][j]!=temp&&map[i][j]!='T')
                    break;
        }
        if(i==4&&!ok)
                if(ok=true,temp=='X')
                    printf("X won\n");
                else if(ok=true,temp=='O')
                    printf("O won\n");
        for(i=0,j=3;i<4;++i,--j)
        {
           temp=map[0][3];
            if(temp=='T')
                temp=map[1][2];
            if(temp=='.')
                break;
            if(map[i][j]!=temp&&map[i][j]!='T')
                break;
        }
        if(i==4&&!ok)
                if(ok=true,temp=='X')
                    printf("X won\n");
                else if(ok=true,temp=='O')
                    printf("O won\n");
        if(!ok)
            if(toltal==16)
                printf("Draw\n");
            else
                printf("Game has not completed\n");
    }
    return 0;
}
