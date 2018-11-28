#pragma comment(linker, "/STACK:1000000000")

#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <iostream>
#include <cstring>
#include <utility>
#include <memory>
#include <cstdlib>
#include <cctype>
#include <queue>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forn1(i, n) for(int i = 1; i <= (int)(n); ++i)
#define forv(i, v) forn(i, v.size())
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define sqr(a) ((a) * (a))
#define two(n) (1 << (n))
#define has(mask, i) (((mask) & two(i)) != 0) ? true : false

typedef long long int64;

const double EPS = 1e-8;
const double PI = 3.1415926535897932384626433832795;
const int INF = 1000000000;

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

int n, m;
int a[110][110];
char ans[110][110];
bool used[110][110];

vector<pair<int, int> > g[110][110];

void go(int x, int y)
{
    if (used[x][y])
        return;

    used[x][y] = true;

    int minH = INF, minI = -1;

    forn(i, 4)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 || nx >= n || ny < 0 || ny >= m)
            continue;

        if (a[nx][ny] < minH)
        {
            minH = a[nx][ny];
            minI = i;
        }
    }

    if (minH < a[x][y])
    {
        g[x][y].pb(mp(x + dx[minI], y + dy[minI]));
        g[x + dx[minI]][y + dy[minI]].pb(mp(x, y));
    }
}

void dfs(int x, int y, char color)
{
    used[x][y] = true;
    ans[x][y] = color;
    
    forv(i, g[x][y])
    {
        int nx = g[x][y][i].first;
        int ny = g[x][y][i].second;

        if (!used[nx][ny])
            dfs(nx, ny, color);
    }
}

int main()
{
#ifdef _DEBUG
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

    int tests;
    scanf("%d", &tests);

    forn(test, tests)
    {
        scanf("%d%d", &n, &m);
        forn(i, n)
            forn(j, m)
                scanf("%d", &a[i][j]);

        forn(i, n)
            forn(j, m)
                g[i][j].clear();

        memset(used, 0, sizeof(used));

        forn(i, n)
            forn(j, m)
                go(i, j);

        memset(used, 0, sizeof(used));

        char color = 'a';
        forn(i, n)
            forn(j, m)
                if (!used[i][j])
                    dfs(i, j, color++);

        printf("Case #%d:\n", test + 1);

        forn(i, n)
        {
            forn(j, m)
            {
                if (j > 0)
                    printf(" ");
                printf("%c", ans[i][j]);
            }
            printf("\n");
        }
    }

    return 0;
}
