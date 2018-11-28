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
const int INF = 10000000;

int n, v;
int values[31000];
int types[31000];
bool changeable[31000];
int d[31000][2];

int get(int cur, int need)
{
    int& result = d[cur][need];
    if (result != -1)
        return result;

    result = INF;

    if (cur * 2 + 1 > n)
    {
        result = values[cur] == need ? 0 : INF;
        return result;
    }

    if (!changeable[cur])
    {
        if (types[cur] == 1)
        {
            if (need == 0)
            {
                int t1 = get(cur * 2, 0) + get(cur * 2 + 1, 0);
                int t2 = get(cur * 2, 0) + get(cur * 2 + 1, 1);
                int t3 = get(cur * 2, 1) + get(cur * 2 + 1, 0);

                result = min(t1, min(t2, t3));
            }
            else
            {
                result = get(cur * 2, 1) + get(cur * 2 + 1, 1);
            }
        }
        else
        {
            if (need == 0)
            {
                result = get(cur * 2, 0) + get(cur * 2 + 1, 0);
            }
            else
            {
                int t1 = get(cur * 2, 1) + get(cur * 2 + 1, 1);
                int t2 = get(cur * 2, 0) + get(cur * 2 + 1, 1);
                int t3 = get(cur * 2, 1) + get(cur * 2 + 1, 0);

                result = min(t1, min(t2, t3));
            }
        }

        return result;
    }

    int result1 = INF, result2 = INF;

    if (need == 0)
    {
        int t1 = get(cur * 2, 0) + get(cur * 2 + 1, 0);
        int t2 = get(cur * 2, 0) + get(cur * 2 + 1, 1);
        int t3 = get(cur * 2, 1) + get(cur * 2 + 1, 0);

        result1 = min(t1, min(t2, t3));
    }
    else
    {
        result1 = get(cur * 2, 1) + get(cur * 2 + 1, 1);
    }

    if (need == 0)
    {
        result2 = get(cur * 2, 0) + get(cur * 2 + 1, 0);
    }
    else
    {
        int t1 = get(cur * 2, 1) + get(cur * 2 + 1, 1);
        int t2 = get(cur * 2, 0) + get(cur * 2 + 1, 1);
        int t3 = get(cur * 2, 1) + get(cur * 2 + 1, 0);

        result2 = min(t1, min(t2, t3));
    }

    if (types[cur] == 1)
        ++result2;
    else
        ++result1;

    result = min(result1, result2);

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
        scanf("%d%d", &n, &v);

        memset(values, 255, sizeof(values));
        memset(types, 255, sizeof(types));
        memset(changeable, 0, sizeof(changeable));

        forn(i, (n - 1) / 2)
        {
            int g, c;
            scanf("%d%d", &g, &c);
            types[i + 1] = g;
            changeable[i + 1] = (c == 0 ? false : true);
        }

        for (int i = (n - 1) / 2 + 1; i <= n; ++i)
        {
            scanf("%d", &values[i]);
        }

        memset(d, 255, sizeof(d));

        int result = get(1, v);
        if (result < INF / 2)
        {
            printf("Case #%d: %d\n", test + 1, result);
        }
        else
        {
            printf("Case #%d: IMPOSSIBLE\n", test + 1);
        }
    }

    return 0;
}
