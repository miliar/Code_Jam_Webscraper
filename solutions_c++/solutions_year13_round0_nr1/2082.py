#include <functional>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fore(i, b, e) for (int i = (int)(b); i <= (int)(e); i++)
#define ford(i, n) for (int i = (int)(n)-1; i >= 0; i--)
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define eq(x, y) (abs((x)-(y))<eps)
#define lt(x, y) ((x)<(y)-eps)
#define le(x, y) ((x)<=(y)+eps)
#define gt(x, y) ((x)>(y)+eps)
#define ge(x, y) ((x)>=(y)-eps)
typedef long long i64;
typedef unsigned long long u64;
typedef unsigned int u32;
typedef double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
const int inf = 1e9+100500;
const int maxn = 10;

const int dx[] = {1, -1, 0, 0, 1, -1, 1, -1};
const int dy[] = {0, 0, 1, -1, 1, 1, -1, -1};
#define ok(x, y) ((x)>=0&&(y)>=0&&(x)<4&&(y)<4)

char a[maxn][maxn];

bool win(int X, int Y, char k)
{
    forn(i, 8) {
        int x = X, y = Y;
        bool good = true;
        forn(t, 4) {
            if (!ok(x, y)) {
                good = false;
                break;
            }
            if (a[x][y] != k && a[x][y] != 'T') {
                good = false;
                break;
            }
            x += dx[i];
            y += dy[i];
        }
        if (good)
            return true;
    }
    return false;
}
string solve()
{
    forn(i, 4) scanf("%s", a[i]);
    bool freecell = false;
    forn(i, 4) forn(j, 4) {
        if (a[i][j] == '.')
            freecell = true;
        if (win(i, j, 'X')) {
            return "X won";
        }
        if (win(i, j, 'O')) {
            return "O won";
        }
    }
    return freecell ? "Game has not completed" : "Draw";
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    forn(i, t) {
        printf("Case #%d: %s\n", i+1, solve().c_str());
    }

#ifdef HOME
    cerr << "time = " << clock()/1000 << " ms" << endl;
#endif
    return 0;
}
