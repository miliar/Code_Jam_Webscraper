#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

#define MAXR 64
#define MAXN 2525

int r, c;
map<int,char> mapa;
int gr[MAXN];

int a[MAXR][MAXR];
char g[MAXR][MAXR];

int main (void)
{
    int cases;
    scanf ("%d", &cases);

    mapa[1] = '/';
    mapa[2] = '\\';
    mapa[3] = '\\';
    mapa[4] = '/';

    for (int caso = 1; caso <= cases; ++caso)
    {
        scanf ("%d %d", &r, &c);

        memset(gr, 0, sizeof(gr));
        memset(g, 0, sizeof(g));

        for (int i = 0; i < r; ++i)
        {
            for (int j = 0; j < c; ++j)
            {
                scanf (" %c", &g[i][j]);
            }
        }

        int grupos = 0;
        bool possible = true;
        for (int i = 0; i < r && possible; ++i)
        {
            for (int j = 0; j < c && possible; ++j)
            {
                if (g[i][j] == '#')
                {
                    if (g[i][j+1] == '#' && g[i+1][j] == '#' && g[i+1][j+1] == '#')
                    {
                        ++grupos;
                        a[i][j] = a[i][j+1] = a[i+1][j] = a[i+1][j+1] = grupos;
                        g[i][j] = 0;
                        g[i][j+1] = 0;
                        g[i+1][j] = 0;
                        g[i+1][j+1] = 0;
                    }
                    else
                    {
                        possible = false;
                    }
                }
                else if (g[i][j] == '.')
                {
                    a[i][j] = 0;
                }
            }
        }

        printf ("Case #%d:\n", caso);
/*
        for (int i = 0; i < r; ++i)
        {
            for (int j = 0; j < c; ++j)
            {
                printf ("%d ", a[i][j]);
            }
            printf ("\n");
        }
*/
        if (!possible)
        {
            printf ("Impossible\n");
            continue;
        }

        for (int i = 0; i < r; ++i)
        {
            for (int j = 0; j < c; ++j)
            {
                if (a[i][j] == 0)
                {
                    printf (".");
                }
                else
                {
                    printf ("%c", mapa[++gr[a[i][j]]]);
                }
            }
            printf ("\n");
        }
    }

    return 0;
}

