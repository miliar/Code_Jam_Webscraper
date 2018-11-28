#include <iostream>
#include <string>
#include <string.h>
#include <cstring>

using namespace std;

int t, h, w;
int i, j;

int a[200][200];
int x[200][200], y[200][200];

int d[200][200];

bool used[200][200];

int dx[4] = {-1, 0, 0, 1};
int dy[4] = { 0,-1, 1, 0};

int tu = 0;

char cv[30];

bool val(int p, int q)
{
    if (p >= 1 && p <= h && q >= 1 && q <= w) return true; 
    return false;
}

void is_sliv(int p, int q)
{
    int mf = 1000000000;
    for (int i = 0; i < 4; i ++)
        if (val(p + dx[i], q + dy[i]) && a[p + dx[i]][q + dy[i]] < mf) mf = a[p + dx[i]][q + dy[i]];

    if (mf >= a[p][q]) tu ++, d[p][q] = tu, used[p][q] = true;
}

void dfs(int p, int q)
{
    if (used[p][q]) return;
    used[p][q] = true;
    int mf = 1000000000, k = -1;
    for (int i = 0; i < 4; i ++)
        if (val(p + dx[i], q + dy[i]) && a[p + dx[i]][q + dy[i]] < mf) mf = a[p + dx[i]][q + dy[i]], k = i;

    if (mf < a[p][q])
    {
        if (used[p + dx[k]][q + dy[k]]) d[p][q] = d[p + dx[k]][q + dy[k]]; else
        {
            dfs(p + dx[k], q + dy[k]);
            d[p][q] = d[p + dx[k]][q + dy[k]];
        }
    }
}

void solve()
{
    bool used[30];
    char c = 'a' - 1;

    for (int i = 0; i < 30; i ++) used[i] = false;

    for (int i = 1; i <= h; i ++)
        for (int j = 1; j <= w; j ++)
            if (!used[d[i][j]]) c ++, cv[d[i][j]] = c, used[d[i][j]] = true;    
}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt ++)
    {
        tu = 0;
        scanf("%d%d", &h, &w);
        for (i = 1; i <= h; i ++)
            for (j = 1; j <= w; j ++)
                scanf("%d", &a[i][j]), used[i][j] = false;

        for (i = 1; i <= h; i ++)
            for (j = 1; j <= w; j ++)
                is_sliv(i, j);

        for (i = 1; i <= h; i ++)
            for (j = 1; j <= w; j ++)
                dfs(i, j);

        printf("Case #%d:\n", tt);

        solve();
        for (i = 1; i <= h; i ++)
        {
            for (j = 1; j <= w; j ++)
                printf("%c ", cv[d[i][j]]);
            printf("\n");
        }
    }
    return 0;
}