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

int fact(int n)
{
    if (n == 0)
        return 1;

    return n * fact(n - 1);
}

inline int countBlocks(string s)
{
    int n = (int)s.length();
    int result = 1;

    for (int i = 1; i < n; ++i)
        if (s[i] != s[i - 1])
            ++result;

    return result;
}

inline int countAns(const vector<int>& p, string s)
{
    string result = s;

    int k = (int)p.size();
    int bound = (int)s.length() / k;
    forn(j, bound)
    {
        forn(i, k)
        {
            result[i + j * k] = s[j * k + p[i]];
        }
    }

    return countBlocks(result);
}

int getAns(int k, string s)
{
    int cnt = fact(k);
    vector<int> p;
    forn(i, k)
        p.pb(i);

    int result = INF;

    forn(i, cnt)
    {
        result = min(result, countAns(p, s));
        next_permutation(all(p));
    }

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
        int k;
        string s;
        cin >> k >> s;
        printf("Case #%d: %d\n", test + 1, getAns(k, s));
    }

    return 0;
}
