#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

#define NMAX 505
typedef ll Matr[NMAX][NMAX];

int n, m, d;
ll w[NMAX][NMAX];
Matr sm, sx, sy;

ll func(int i, int j, int k, Matr s)
{
    return s[i + k][j + k] - s[i][j + k] - s[i + k][j] + s[i][j];
}
bool can(int k)
{
    forn(i, n - k + 1)
    {
        forn(j, m - k + 1)
        {
            ll mass = func(i, j, k, sm) - (w[i][j] + w[i][j + k - 1] + w[i + k - 1][j] + w[i + k - 1][j + k - 1]);
            ll x = func(i, j, k, sx) - ((w[i][j] + w[i][j + k - 1]) * i + (w[i + k - 1][j] + w[i + k - 1][j + k - 1]) * (i + k - 1));
            ll y = func(i, j, k, sy) - ((w[i][j] + w[i + k - 1][j]) * j + (w[i][j + k - 1] + w[i + k - 1][j + k - 1]) * (j + k - 1));

            if (2 * x == mass * (2 * i + k - 1) && 2 * y == mass * (2 * j + k - 1)) return true;
        }
    }

    return false;
}


void solve(int test)
{
    printf("Case #%d: ", test);

    scanf("%d %d %d\n", &n, &m, &d);
    forn(i, n)
    {
        forn(j, m)
        {
            char c;
            scanf("%c", &c);
            w[i][j] = d + int(c - '0');
        }
        scanf("\n");
    }

    memset(sm, 0, sizeof(sm));
    memset(sx, 0, sizeof(sx));
    memset(sy, 0, sizeof(sy));

    forn(i, n)
    {
        forn(j, m)
        {
            sm[i + 1][j + 1] = sm[i][j + 1] + sm[i + 1][j] - sm[i][j] + w[i][j];
            sx[i + 1][j + 1] = sx[i][j + 1] + sx[i + 1][j] - sx[i][j] + ll(w[i][j]) * i;
            sy[i + 1][j + 1] = sy[i][j + 1] + sy[i + 1][j] - sy[i][j] + ll(w[i][j]) * j;
        }
    }

    for (int k = min(n, m); k >= 3; k--)
    {
        if (can(k)) 
        {
            cout << k << endl;
            return;
        }
    }

    cout << "IMPOSSIBLE\n";
}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}