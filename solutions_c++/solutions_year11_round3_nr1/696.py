#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

#define MAXN 60
int n, m;
int r, c, tot;
int d[4][2] = {-1,0, 0,1, 1,0, 0,-1};

int rcnt[MAXN], ccnt[MAXN];
char g[MAXN][MAXN];
int flg[MAXN][MAXN];

bool in(int x, int y) { return x >= 0 && x < r && y >= 0 && y < c;}

bool isOk()
{
    int i, j, k, x, y, cnt;
    for (i = 0; i < r; i++)
        if (rcnt[i] % 2) return 0;

    for (i = 0; i < c; i++)
        if (ccnt[i] % 2) return 0;

    for (i = 0; i < r; i++)
        for (j = 0; j < c; j++)
        {
            if (g[i][j] == '.') continue;
            cnt = 0;
            for (k = 0; k < 4; k++)
            {
                x = i + d[k][0];
                y = j + d[k][1];
                if (in(x, y) && g[x][y] == '#') cnt++;
            }
            if (cnt == 0) return 0;
        }

    return 1;
}

void solve()
{
    int i, j;
    for (i = 0; i < r - 1; i++)
    {
        for (j = 0; j < c - 1; j++)
        {
            if (g[i][j] == '#')
            {
                g[i][j] = g[i+1][j+1] = '/';
                g[i][j+1] = g[i+1][j] = '\\';
            }
        }
    }

    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
            printf ("%c", g[i][j]);
        puts("");
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("1.out", "w", stdout);

    int i, j, cs, csnum;
    scanf ("%d", &csnum);

    for (cs = 1; cs <= csnum; cs++)
    {
        scanf ("%d %d", &r, &c);
        tot = 0;
        memset(rcnt, 0, sizeof(rcnt));
        memset(ccnt, 0, sizeof(ccnt));

        for (i = 0; i < r; i++)
        {
            for (j = 0; j < c; j++)
            {
                scanf (" %c", &g[i][j]);
                if (g[i][j] == '#')
                {
                    rcnt[i]++;
                    ccnt[j]++;
                    tot++;
                }
            }
        }

        printf ("Case #%d:\n", cs);
        if (!isOk())
            printf ("Impossible\n");
        else
            solve();
    }

}
