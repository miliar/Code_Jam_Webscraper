#include <cstdio>
#include <cstring>
int t,r,c,blue;
char mat[55][55];
void acomoda()
{
    for (int i=1; i<r; i++)
    {
        for (int j=1; j<c; j++)
        {
            if (mat[i][j]=='#')
            {
                if (mat[i+1][j]=='#' && mat[i+1][j+1]=='#' && mat[i][j+1]=='#')
                {
                    blue-=4;
                    mat[i][j]='/';
                    mat[i][j+1]=92;
                    mat[i+1][j]=92;
                    mat[i+1][j+1]='/';
                }
            }
        }
    }
}
int main()
{
    scanf("%d",&t);
    for (int g=1; g<=t; g++)
    {
        blue=0;
        scanf("%d%d\n",&r,&c);
        for (int i=1; i<=r; i++)
        {
            for (int j=1; j<=c; j++)
            {
                scanf("%c",&mat[i][j]);
                if (mat[i][j]=='#')
                    blue++;
            }
            scanf("\n");
        }
        acomoda();
        printf("Case #%d:\n",g);
        if (blue==0)
        {
            for (int i=1; i<=r; i++)
            {
                for (int j=1; j<=c; j++)
                    printf("%c",mat[i][j]);
                printf("\n");
            }
        }
        else
        {
            printf("Impossible\n");
        }
    }
}
