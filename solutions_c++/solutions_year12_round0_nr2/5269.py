#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

const int INF = 1e9;

#define forn(i, n) for(int i = 0; i < (int)n; ++i)
#define forv(i, v) forn(i, v.size())
#define pb push_back

int n, s, p;
int t[1000];

inline int getSurprise(int n)
{
    if (n >= 2 && (((n - 2) % 3) == 0))
        return (((n - 2) / 3) + 2 >= p) ? 1 : 0;
    if (n >= 3 && (((n - 3) % 3) == 0))
        return (((n - 3) / 3) + 2 >= p) ? 1 : 0;
    if (n >= 4 && (((n - 4) % 3) == 0))
        return (((n - 4) / 3) + 2 >= p) ? 1 : 0;

    return -1e3;
}

inline int getCasual(int n)
{
    if (n >= 0 && ((n % 3) == 0))
        return ((n / 3) >= p) ? 1 : 0;
    if (n >= 1 && (((n - 1) % 3) == 0))
        return (((n - 1) / 3) + 1 >= p) ? 1 : 0;
    if (n >= 2 && (((n - 2) % 3) == 0))
        return (((n - 2) / 3) + 1 >= p) ? 1 : 0;
}


inline int get(int mask)
{
    int result = 0;

    forn(i, n)
    {
        if ((mask >> i) & 1)
            result += getSurprise(t[i]);
        else
            result += getCasual(t[i]);
    }

    return result;
}

int count(int mask)
{
    int result = 0;

    forn(i, n)
        result += ((mask >> i) & 1);

    return result;
}

int solve()
{
    int result = 0;
    forn(mask, (1 << n))
        if (count(mask) == s)
            result = max(result, get(mask));

    return result;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  
    int tests;
    scanf("%d\n", &tests);
    forn(test, tests)
    {
        scanf("%d %d %d", &n, &s, &p);
        forn(i, n)
            scanf("%d", &t[i]);

        printf("Case #%d: %d\n", test + 1, solve());
    }

}