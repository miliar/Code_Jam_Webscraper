#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <queue>
#include <list>
#include <algorithm>
#include <cctype>
#include <cmath>
#include <sstream>
#include <fstream>
#include <functional>
#include <deque>
#include <utility>
#include <memory>

using namespace std;

typedef long long int64;

const int INF = 1000 * 1000 * 1000;
const int64 INF64 = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;
const double PI = 3.1415926535897932384626433832795;
const double EPS = 1e-8;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forn1(i, n) for(int i = 1; i <= (int)(n); ++i)
#define forv(i, v) forn(i, v.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define two(i) (1 << (i))
#define has(mask, i) ((((mask) & two(i)) == 0) ? false : true)

int n, m, d;
string a[550];

bool check(int i, int j, int k)
{
    int rx = 0, ry = 0;

    forn(di, k)
        forn(dj, k)
        {
            if ((di == 0 || di == k - 1) && (dj == 0 || dj == k - 1))
                continue;

            //rx += (di * 2 + 1 - k) * (d + a[i + di][j + dj] - '0');
            //ry += (dj * 2 + 1 - k) * (d + a[i + di][j + dj] - '0');

            rx += (di * 2 + 1 - k) * (d + a[i + di][j + dj] - '0');
            ry += (dj * 2 + 1 - k) * (d + a[i + di][j + dj] - '0');
        }

    return rx == 0 && ry == 0;
}

bool tryK(int k)
{
    forn(i, n - k + 1)
            forn(j, m - k + 1)
                if (check(i, j, k))
                    return true;

    return false;
}

int solve()
{
    int result = -1;

    for (int k = 3, bound = min(n, m); k <= bound; ++k)
        if (tryK(k))
            result = k;

    return result;
}

int main()
{
    //freopen("input.txt", "rt", stdin);

    int tests;
    scanf("%d", &tests);

    forn1(test, tests)
    {
        cin >> n >> m >> d;

        forn(i, n)
            cin >> a[i];

        cout << "Case #" << test << ": ";

        int result = solve();
        if (result == -1)
            cout << "IMPOSSIBLE";
        else
            cout << result;

        cout << endl;
    }

    return 0;
}
