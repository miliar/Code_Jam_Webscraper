#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>
#include <deque>
#include <queue>
#include <list>
#include <functional>
#include <cstring>
#include <utility>
#include <cmath>
#include <cctype>

using namespace std;

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forn1(i, n) for(int i = 1; i <= (int)(n); ++i)
#define forv(i, v) forn(i, v.size())
#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))
#define two(i) (1 << (i))
#define has(mask, i) ((((mask) & two(i)) != 0) ? true : false)

const int INF = 1000 * 1000 * 1000;
const int64 INF64 = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;
const long double PI = 3.1415926535897932384626433832795;
const long double EPS = 1e-8;

inline vector<string> split(const string& path)
{
    vector<string> result;

    string buf;
    forv(i, path)
    {
        if (path[i] == '/')
        {
            if (!buf.empty())
            {
                result.pb(buf);
                buf = "";
            }
        }
        else
        {
            buf += path[i];
        }
    }

    if (!buf.empty())
    {
        result.pb(buf);
    }

    return result;
}

struct Catalog
{
    string name;
    vector<Catalog> children;

    Catalog(const string& name): name(name) {}
};

Catalog root("");

int go(const vector<string>& dirs, const int idx, Catalog& catalog)
{
    if (idx >= (int)dirs.size())
    {
        return 0;
    }

    forv(i, catalog.children)
    {
        if (catalog.children[i].name == dirs[idx])
        {
            return go(dirs, idx + 1, catalog.children[i]);
        }
    }

    catalog.children.pb(Catalog(dirs[idx]));
    return 1 + go(dirs, idx + 1, catalog.children.back());
}

inline int mkdir(const string& path)
{
    return go(split(path), 0, root);
}

char buf[1024];

int main()
{
    int tests;
    scanf("%d", &tests);

    forn(test, tests)
    {
        root.children.clear();

        int n, m;
        scanf("%d%d", &n, &m);

        forn(i, n)
        {
            scanf("%s", buf);
            mkdir(buf);
        }

        int result = 0;
        forn(i, m)
        {
            scanf("%s", buf);
            result += mkdir(buf);
        }

        printf("Case #%d: %d\n", test + 1, result);
    }

    return 0;
}
