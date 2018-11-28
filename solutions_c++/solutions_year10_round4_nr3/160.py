#include <cstdio>

int mat[110][110];

int main()
{
    int t, teste;
    int i, j;
    int r;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        for (i=0; i<110; i++)
        {
            for (j=0; j<110; j++)
            {
                mat[i][j] = 0;
            }
        }
        scanf("%d", &r);
        int a;
        int r1, r2, c1, c2;
        for (a=0; a<r; a++)
        {
            scanf("%d %d %d %d", &r1, &c1, &r2, &c2);
            for (i=r1; i<=r2; i++)
            {
                for (j=c1; j<=c2; j++)
                {
                    mat[i][j] = 1;
                } 
            }
        }
        
        int resp = 0;
        int count;
        for (;;resp++)
        {
            count = 0;
            for (i=109; i>0; i--)
            {
                for (j=109; j>0; j--)
                {
                    if (mat[i][j] == 0)
                    {
                        if (mat[i][j-1] == 1 && mat[i-1][j] == 1)
                        {
                            mat[i][j] = 1;
                            count++;
                        }
                    }
                    else
                    {
                        if (mat[i][j-1] == 0 && mat[i-1][j] == 0)
                        {
                            mat[i][j] = 0;
                        }
                        else
                        {
                            count++;                            
                        }
                    }
                }
            }
            if (count == 0)
                break;
        }
        printf("Case #%d: %d\n", t+1, resp+1);
    }
    return 0;
}
