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
#define has(mask, i) (((mask) & two(n)) != 0) ? true : false

typedef long long int64;

const double EPS = 1e-8;
const double PI = 3.1415926535897932384626433832795;
const int INF = 1000000000;

int fact(int n)
{
    if (n == 0)
        return 1;

    return n * fact(n - 1);
}

int64 solve(vector<int64> a, vector<int64> b)
{
    sort(all(a));
    sort(all(b));
    reverse(all(b));

    int64 result1 = 0;

    forv(i, a)
        result1 += a[i] * b[i];

    sort(all(a));
    sort(all(b));
    reverse(all(a));

    int64 result2 = 0;

    forv(i, a)
        result2 += a[i] * b[i];

    return min(result1, result2);
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
        int n;
        scanf("%d", &n);

        vector<int64> a(n), b(n);

        forn(i, n)
            scanf("%I64d", &a[i]);
        forn(i, n)
            scanf("%I64d", &b[i]);

        printf("Case #%d: %I64d\n", test + 1, solve(a, b));
    }

    return 0;
}
