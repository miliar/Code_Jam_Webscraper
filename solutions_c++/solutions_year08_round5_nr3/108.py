#include <stdio.h>
#include <string.h>
#include <vector>

#define pb push_back
#define nmax 85

using namespace std;

int T, m, n, crt;
char a[nmax][nmax];
int b[nmax][nmax], curent;
int cuplat[nmax * nmax], v[nmax * nmax];
vector <int> e[nmax * nmax];

int cupleaza(int x)
{
    if(v[x] == curent) return 0;
    v[x] = curent;
    for(int i = 0; i < (int)e[x].size(); i++)
        if(!cuplat[e[x][i]])
        {
            cuplat[x] = e[x][i];
            cuplat[e[x][i]] = x;
            return 1;
        }

    for(int i = 0; i < (int)e[x].size(); i++)
        if(cupleaza(cuplat[e[x][i]]))
        {
            cuplat[x] = e[x][i];
            cuplat[e[x][i]] = x;
            return 1;
        }

    return 0;
}

int main()
{
    freopen("cl.in", "r", stdin);
    freopen("cl.out", "w", stdout);

    scanf("%d\n", &T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%d%d\n", &m, &n); crt = 0; int tot = 0;
        memset(v, 0, sizeof(v));
        for(int i = 0; i <= m + 1; i++) for(int j = 0; j <= n + 1; j++) a[i][j] = 'x';
        for(int i = 1; i <= m; i++)
        {
            for(int j = 1; j <= n; j++)
            {
                scanf("%c", &a[i][j]);
                if(a[i][j] == '.') tot++;
                crt++;
                b[i][j] = crt;
            }
            scanf("\n");
        }

        for(int i = 1; i <= crt; i++) e[i].clear();
        for(int j = 1; j <= n; j++)
            for(int i = 1; i <= m; i++)
                if(a[i][j] == '.')
                {
                    if(a[i][j - 1] == '.')
                    {
                        e[b[i][j - 1]].pb(b[i][j]);
                        e[b[i][j]].pb(b[i][j - 1]);
                    }
                    if(a[i][j + 1] == '.')
                    {
                        e[b[i][j + 1]].pb(b[i][j]);
                        e[b[i][j]].pb(b[i][j + 1]);
                    }
                    if(a[i - 1][j - 1] == '.')
                    {
                        e[b[i - 1][j - 1]].pb(b[i][j]);
                        e[b[i][j]].pb(b[i - 1][j - 1]);
                    }
                    if(a[i - 1][j + 1] == '.')
                    {
                        e[b[i - 1][j + 1]].pb(b[i][j]);
                        e[b[i][j]].pb(b[i - 1][j + 1]);
                    }
                }

        memset(v, 0, sizeof(v));
        memset(cuplat, 0, sizeof(cuplat));
        for(int i = 1; i <= crt; i++)
            if(!cuplat[i])
            {
                curent++;
                if(cupleaza(i))
                {
                    tot--;
                }
            }

        printf("Case #%d: %d\n", t, tot);
    }

    return 0;
}
