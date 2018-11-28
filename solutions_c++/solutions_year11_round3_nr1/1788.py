#include <stdio.h>
#include <stdlib.h>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n,cases,x,y,i,j,k;
    scanf("%d",&n);
    for(cases=1;cases<=n;cases++)
    {
        scanf("%d%d",&x,&y);
        char map[x+2][y+2];
        for(i=1;i<x+1;i++)
        {
            scanf("%s",&map[i][1]);
        }
        for(i=0;i<x+2;i++)
        {
            map[i][0]='.';
            map[i][y+1]='.';
        }
        for(i=0;i<y+2;i++)
        {
            map[0][i]='.';
            map[x+1][i]='.';
        }
        k=0;
        for(i=1;i<x+2;i++)
        {
            for(j=1;j<y+2;j++)
            {
                if(map[i][j]=='#'&&map[i][j+1]=='#'&&map[i+1][j]=='#'&&map[i+1][j+1]=='#')
                {
                    map[i][j]='/';
                    map[i][j+1]='\\';
                    map[i+1][j]='\\';
                    map[i+1][j+1]='/';
                }
                if(map[i][j]=='#'){k=1;break;}
            }
            if(k==1)break;
        }
        printf("Case #%d:\n",cases);
        if(k==1)
        {
            printf("Impossible\n");
        }
        else
        {
            for(i=1;i<x+1;i++)
            {
                for(j=1;j<y+1;j++)
                {
                    printf("%c",map[i][j]);
                }
                printf("\n");
            }
        }
    }

}
