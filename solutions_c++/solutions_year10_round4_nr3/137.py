#include <cstdio>

int t[2][110][110];

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int ti = 1; ti <= tc; ti++)
    {

        printf("Case #%d: ", ti);
        for(int i = 0; i <= 100; i++)
            for(int j = 0; j <= 100; j++)
            {
                t[0][i][j] = t[1][i][j] = 0;
            }
        int r;
        scanf("%d", &r);
        for(int w = 0; w < r; w++)
        {
            int x1, y1, x2, y2;
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            for(int i = x1; i <= x2; i++)
            for(int j = y1; j <= y2; j++)
            t[0][i][j] = 1;
        }
        for(int w = 0; w < 10000000; w++)
        {
            int end=1;
            for(int i = 1; i <= 100; i++)
                for(int j = 1; j <= 100; j++)
                if(t[w%2][i][j])end=0;
            if(end)
            {
                printf("%d\n", w);
                break;
            }
            for(int i = 1; i <= 100; i++)
                for(int j = 1; j <= 100; j++)
                {
                    if(t[w%2][i-1][j]==1 && t[w%2][i][j-1]==1)
                        t[(w+1)%2][i][j]=1;
                    else if(t[w%2][i-1][j]==0 && t[w%2][i][j-1]==0)
                        t[(w+1)%2][i][j]=0;
                    else t[(w+1)%2][i][j]=t[w%2][i][j];
                }
        }
    }
    return 0;
}
