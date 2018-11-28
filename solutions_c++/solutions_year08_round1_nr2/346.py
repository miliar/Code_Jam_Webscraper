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
const int INF = 1000000000;

int getBest(int n, const vector<vector<pair<int, int> > > a)
{
    int cnt = INF;
    int resultMask = -1;

    forn(mask, two(n))
    {
        int tCnt = 0;
        forn(i, n)
            if (has(mask, i))
                ++tCnt;

        bool flag = true;

        forv(i, a)
        {
            bool ok = false;

            forv(j, a[i])
            {
                if (a[i][j].second == 0 && !has(mask, a[i][j].first))
                {
                    ok = true;
                    break;
                }

                if (a[i][j].second == 1 && has(mask, a[i][j].first))
                {
                    ok = true;
                    break;
                }
            }

            if (!ok)
            {
                flag = false;
                break;
            }
        }

        if (flag && tCnt < cnt)
        {
            cnt = tCnt;
            resultMask = mask;
        }
    }

    return resultMask;
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
        int n, m;
        scanf("%d%d", &n, &m);

        vector<vector<pair<int, int> > > a(m);

        forn(i, m)
        {
            int t;
            scanf("%d", &t);

            a[i].resize(t);

            forn(j, t)
            {
                int x, y;
                scanf("%d%d", &x, &y);
                --x;
                a[i][j] = mp(x, y);
            }
        }

        int mask = getBest(n, a);

        printf("Case #%d:", test + 1);

        if (mask == -1)
        {
            printf(" IMPOSSIBLE\n");
            continue;
        }

        forn(i, n)
            if (has(mask, i))
                printf(" 1");
            else
                printf(" 0");

        printf("\n");
    }

    return 0;
}
