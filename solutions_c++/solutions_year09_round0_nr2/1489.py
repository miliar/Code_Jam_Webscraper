#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <list>
#include <vector>
#include <cmath>
#include <algorithm>
#include <sstream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define mp make_pair
#define cl clear()
#define sz(a) ((int)a.size())
#define X first
#define Y second
#define pb push_back
#define sqr(a) ((a) * (a))

int t;
int h, w;
int a[100][100];
int b[100][100];

int v;

int color(int x, int y)
{
    if (b[x][y] != -1)
        return b[x][y];
    int x1 = -1, y1 = -1, mn = a[x][y];
    if (x > 0 && a[x - 1][y] < mn)
    {
        mn = a[x - 1][y];
        x1 = x - 1; y1 = y;
    }
    if (y > 0 && a[x][y - 1] < mn)
    {
        mn = a[x][y - 1];
        x1 = x; y1 = y - 1;
    }
    if (y < w - 1 && a[x][y + 1] < mn)
    {
        mn = a[x][y + 1];
        x1 = x; y1 = y + 1;
    }
    if (x < h - 1 && a[x + 1][y] < mn)
    {
        mn = a[x + 1][y];
        x1 = x + 1; y1 = y;
    }
    if (x1 == -1)
        b[x][y] = v++;
    else
        b[x][y] = color(x1, y1);
    return b[x][y];
}

int main()
{
    scanf("%d\n", &t);
    REP(k, t)
    {
        scanf("%d%d\n", &h, &w);
        v = 0;
        REP(i, h)
            REP(j, w)
                scanf("%d", &a[i][j]);
        memset(b, -1, sizeof(b));
        REP(i, h)
            REP(j, w)
                if (b[i][j] == -1)
                    color(i, j);
        printf("Case #%d:\n", k + 1);
        REP(i, h)
        {
            REP(j, w - 1)
                printf("%c ", 'a' + b[i][j]);
            printf("%c\n", 'a' + b[i][w - 1]);
        }
    }
	return 0;
}
