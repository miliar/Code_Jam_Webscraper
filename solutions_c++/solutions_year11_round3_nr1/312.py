#include <cstdio>

int t, n, m;
char ch, a[60][60];

bool work()
{
     for (int i = 0; i < n - 1; i++)
         for (int j = 0; j < m - 1; j++)
             if (a[i][j] == '#')
             {
                         if (a[i][j + 1] == '#' && a[i + 1][j] == '#' && a[i + 1][j + 1] == '#')
                         {
                                    a[i][j] = a[i + 1][j + 1] = '/';
                                    a[i][j + 1] = a[i + 1][j] = '\\';
                         }
                         else return false;
             }
     for (int i = 0; i < n; i++)
         for (int j = 0; j < m; j++)
             if (a[i][j] == '#') return false;
     for (int i = 0; i < n; i++)
     {
         for (int j = 0; j < m; j++)
             printf("%c", a[i][j]);
         printf("\n");
     }
     return true;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas++)
    {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++)
        {
            scanf("%c", &ch);
            for (int j = 0; j < m; j++)
                scanf("%c", &a[i][j]);
        }
        printf("Case #%d:\n", cas);
        if (!work()) printf("Impossible\n");
    }
    return 0;
}
        
