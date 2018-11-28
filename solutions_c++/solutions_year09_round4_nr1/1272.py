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
#define has(mask, i) ((((mask) & two(i)) != 0) ? true : false)

typedef long long int64;

const double EPS = 1e-8;
const double PI = 3.1415926535897932384626433832795;
const int INF = 1000000000;

int n;
map<vector<int>, int> d;

inline bool ok(const vector<int>& p)
{
    forv(i, p)
        if (p[i] > i)
            return false;

    return true;
}

queue<vector<int> > q;

int get(vector<int> p)
{
    d.clear();
    while (!q.empty())
        q.pop();

    q.push(p);
    d[p] = 0;

    while (!q.empty())
    {
        p = q.front();
        q.pop();

        int dst = d[p];

        if (ok(p))
            return dst;
        
        forn(i, n - 1)
        {
            swap(p[i], p[i + 1]);
            if (d.count(p) == 0)
            {
                d[p] = dst + 1;
                q.push(p);
            }
            swap(p[i], p[i + 1]);
        }
    }

    return INF;
}

int main()
{
#ifdef _DEBUG
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

    int tests;
    scanf("%d", &tests);

    char s[100];

    forn(test, tests)
    {
        scanf("%d", &n);
        vector<int> p;
        forn(i, n)
        {
            scanf("%s", s);
            int ind = -1;
            for (int j = n - 1; j >= 0; --j)
                if (s[j] == '1')
                {
                    ind = j;
                    break;
                }
            p.pb(ind);
        }
        printf("Case #%d: %d\n", test + 1, get(p));
    }

    return 0;
}
