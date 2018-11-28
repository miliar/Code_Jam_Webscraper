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

// TODO
const double MAX_TIME = 1e13;

double dist;
vector<int> a;

inline bool ok(double t)
{
    int n = (int)a.size();

    double l = (double)a.front() - t + dist;

    for (int i = 1; i < n; ++i)
    {
        double x = (double)a[i];
        double ro = abs(x - l);

        if (l - EPS > x)
        {
            if (ro - EPS > t)
                return false;
            else
            {
                l += dist;
            }
        }
        else
        {
            l = x - min(t, ro) + dist;
        }
    }

    return true;
}

double binSearch(double l, double r)
{
    if (r - l < EPS)
        return -1.0;

    double mid = (l + r) / 2.0;
    if (ok(mid))
    {
        double result = binSearch(l, mid);
        if (result > -0.5)
            return result;
        else
            return mid;
    }
    else
    {
        return binSearch(mid, r);
    }
}

int main()
{
    //freopen("input.txt", "rt", stdin);

    int tests;
    scanf("%d", &tests);

    forn1(test, tests)
    {
        a.clear();

        int c, d;
        scanf("%d%d", &c, &d);
        dist = d;

        forn(i, c)
        {
            int p, v;
            scanf("%d%d", &p, &v);
            forn(j, v)
                a.pb(p);
        }

        sort(all(a));

        printf("Case #%d: %.12lf\n", test, binSearch(0, MAX_TIME));
    }

    return 0;
}
