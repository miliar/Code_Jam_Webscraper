#include <iostream>
#include <queue>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <list>
#include <sstream>
#include <cmath>
#include <ctime>
#include <algorithm>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define sz(a) ((int)a.size())
#define cl clear()
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))

typedef long long ll;

struct rect{
    int x1, y1, x2, y2;
    rect(int x = 0, int y = 0, int X = 0, int Y = 0) : x1(x), y1(y), x2(X), y2(Y) {}
};

vector <rect> a;

int b[101][101];
int c[101][101];

bool alive()
{
    REP(i, 101)
        REP(j, 101)
            if (b[i][j])
                return 1;
    return 0;
}

int main()
{
    int nn;
    scanf("%d", &nn);
    REP(ii, nn)
    {
        int n;
        a.cl;
        scanf("%d", &n);
        int x1, x2, y1, y2;
        memset(b, 0, sizeof(b));
        REP(i, n)
        {
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2), a.pb(rect(x1, y1, x2, y2));
            FOR(x, x1, x2 + 1)
                FOR(y, y1, y2 + 1)
                    b[x][y] = 1;
        }
        int t = 0;
        while (alive())
        {
            memset(c, 0, sizeof(c));
            REP(i, 101)
                REP(j, 101)
                    if ((b[i - 1][j] && b[i][j - 1]) || (b[i][j] && (b[i - 1][j] || b[i][j - 1])))
                        c[i][j] = 1;
            memcpy(b, c, sizeof(c));
            t++;
        }
        printf("Case #%d: %d\n", ii + 1, t);
        //int rt = scan_line();
    }
}
