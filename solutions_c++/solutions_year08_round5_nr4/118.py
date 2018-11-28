#include <stdio.h>
#include <string.h>

#define nmax 150
#define mod 10007

int T;
int h, w, r, x1, y1;
int a[nmax][nmax], c[nmax][nmax];

int main()
{
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);

    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%d%d%d", &h, &w, &r);
        memset(a, 0, sizeof(a));
        for(int i = 1; i <= r; i++)
        {
            scanf("%d%d", &x1, &y1);
            a[x1][y1] = 1;
        }

        memset(c, 0, sizeof(c));
        c[1][1] = 1;
        for(int i = 1; i <= h; i++)
            for(int j = 1; j <= w; j++)
            {
                if(i - 2 >= 0) c[i][j] += c[i - 2][j - 1];
                if(j - 2 >= 0) c[i][j] += c[i - 1][j - 2];
                if(a[i][j] == 1) c[i][j] = 0;
                while(c[i][j] >= mod) c[i][j] -= mod;
            }
        printf("Case #%d: %d\n", t, c[h][w]);
    }

    return 0;
}
