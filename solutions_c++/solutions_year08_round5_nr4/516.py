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

int w, h, n;
bool rocks[200][200];
int d[200][200];

int get(int x, int y)
{
    if (x == h - 1 && y == w - 1)
        return 1;

    int& result = d[x][y];
    if (result != -1)
        return result;

    result = 0;

    int nx = x + 1, ny = y + 2;
    if (nx >= h || ny >= w || rocks[nx][ny]);
    else
        result += get(nx, ny);

    nx = x + 2, ny = y + 1;
    if (nx >= h || ny >= w || rocks[nx][ny]);
    else
        result += get(nx, ny);

    result %= 10007;

    return result;
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
        int R;
        scanf("%d%d%d", &h, &w, &R);

        memset(rocks, 0, sizeof(rocks));

        forn(i, R)
        {
            int r, c;
            scanf("%d%d", &r, &c);
            rocks[r - 1][c - 1] = true;
        }

        memset(d, 255, sizeof(d));

        printf("Case #%d: %d\n", test + 1, get(0, 0));
    }

    return 0;
}
