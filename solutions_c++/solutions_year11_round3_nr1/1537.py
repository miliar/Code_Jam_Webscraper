#include <stdio.h>
#include <stdlib.h>
char pic[100][100];

int main()
{
    int t;
    int ck;
    //freopen("A-large.in","r",stdin);
    //freopen("google1.out","w",stdout);
    scanf("%d",&t);
    for (ck = 0; ck < t; ck++)
    {
        int r, c;
        int i, j;
        int bFailed = 0;
        scanf("%d %d",&r,&c);
        for(i=0; i<r; i++)
            scanf("%s",pic[i]);
        for(i=0; i<r && !bFailed; i++)
        {
            for(j=0; j<c && !bFailed; j++)
            {
                if(pic[i][j] == '#')
                {
                    pic[i][j] = '/';
                    if(pic[i][j+1] == '#')
                    {
                        pic[i][j+1] = '\\';
                    }
                    else
                        bFailed = 1;
                    if(pic[i+1][j] == '#')
                    {
                        pic[i+1][j] = '\\';
                    }
                    else
                        bFailed = 1;

                    if(pic[i+1][j+1] == '#')
                    {
                        pic[i+1][j+1] = '/';
                    }
                    else
                        bFailed = 1;
                }
            }
        }
        printf("Case #%d:\n", ck+1);
        if(bFailed == 1)
        {
            printf("Impossible\n");
        }
        else
        {
            for(i=0; i<r; i++)
                printf("%s\n",pic[i]);
        }
    }
    return 0;
}