#include <cstdio>
#include <cstdlib>
#include <cstring>

char tab[100][100];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out1.txt", "w", stdout);

    int tc, ti;
    scanf("%d", &tc);
    for(ti = 1; ti <= tc; ti++)
    {
        int n, k;
        scanf("%d %d", &n, &k);
        memset(tab,'.', 100*100);
        for(int i = 1; i <= n; i++)
        {
            scanf("%s", &tab[i][1]);
            tab[i][n+1] = '.';
        }
        for(int i = 1; i <= n; i++)
        {
            int a = n;
            for(int j = n; j > 0; j--)
            {
                if(tab[i][j] != '.')
                {
                    char x = tab[i][a];
                    tab[i][a] = tab[i][j];
                    tab[i][j] = x;
                    a--;
                }
            }
        }
        int found = 0;
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= n; j++)
            {
                if(tab[i][j] == '.')continue;
                int a;
                for(a = 0; a < k && a+j <= n; a++)
                    if(tab[i][j] != tab[i][j+a])break;
                if(a == k)
                {
                    if(found == 0)
                    {
                        if(tab[i][j] == 'R')found = 1;
                        else found = 2;
                    }
                    else
                    {
                        if(found == 2 && tab[i][j] == 'R')found = 3;
                        if(found == 1 && tab[i][j] == 'B')found = 3;
                    }
                }
                for(a = 0; a < k && a+i <= n; a++)
                    if(tab[i][j] != tab[i+a][j])break;
                if(a == k)
                {
                    if(found == 0)
                    {
                        if(tab[i][j] == 'R')found = 1;
                        else found = 2;
                    }
                    else
                    {
                        if(found == 2 && tab[i][j] == 'R')found = 3;
                        if(found == 1 && tab[i][j] == 'B')found = 3;
                    }
                }
                for(a = 0; a < k && a+i <= n && a+j <= n; a++)
                    if(tab[i][j] != tab[i+a][j+a])break;
                if(a == k)
                {
                    if(found == 0)
                    {
                        if(tab[i][j] == 'R')found = 1;
                        else found = 2;
                    }
                    else
                    {
                        if(found == 2 && tab[i][j] == 'R')found = 3;
                        if(found == 1 && tab[i][j] == 'B')found = 3;
                    }
                }
                for(a = 0; a < k && a+i <= n && j-a > 0; a++)
                    if(tab[i][j] != tab[i+a][j-a])break;
                if(a == k)
                {
                    if(found == 0)
                    {
                        if(tab[i][j] == 'R')found = 1;
                        else found = 2;
                    }
                    else
                    {
                        if(found == 2 && tab[i][j] == 'R')found = 3;
                        if(found == 1 && tab[i][j] == 'B')found = 3;
                    }
                }

            }
            printf("Case #%d: ", ti);
            if(found == 0)printf("Neither\n");
            if(found == 1)printf("Red\n");
            if(found == 2)printf("Blue\n");
            if(found == 3)printf("Both\n");
    }
    return 0;
}
