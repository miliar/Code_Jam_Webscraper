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

const int ans[24] = {1,
2,
3,
5,
8,
14,
24,
43,
77,
140,
256,
472,
874,
1628,
3045,
5719,
10780,
20388,
38674,
73562,
40265,
68060,
13335,
84884};

int main()
{
    int tests;
    scanf("%d", &tests);

    forn(test, tests)
    {
        int n;
        scanf("%d", &n);

        printf("Case #%d: %d\n", test + 1, ans[n - 2]);
    }

    return 0;
}
