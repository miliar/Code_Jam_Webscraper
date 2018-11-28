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
#define mp make_pair

int a, b;
char buf[10];
vector<pair<int, int> > result;


inline string shift(string &s, int pos)
{
    return s.substr(pos) + s.substr(0, pos);
}

inline int getLength(int n)
{
    int result = 0;

    while (n > 0)
        n /= 10, result++;

    return result;
}

inline bool ok(int n, int m)
{
    string a = itoa(n, buf, 10);
    string b = itoa(m, buf, 10);

    int len = getLength(n);
    for (int i = 0; i < len; ++i)
        if (shift(a, i) == b)
            return true;

    return false;
}

int solve()
{
    int ans = 0;
    
    forv(i, result)
        if (a <= result[i].first && result[i].second <= b)
            ans++;

    return ans;
}

void init()
{
    for (int n = 1; n < 1000; ++n)
        for (int m = n + 1; m <= 1000; ++m)
            if (getLength(n) == getLength(m) && ok(n, m))
                result.pb(mp(n, m));
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  
    int tests;
    scanf("%d\n", &tests);
    init();
    forn(test, tests)
    {
        scanf("%d %d", &a, &b);

        printf("Case #%d: %d\n", test + 1, solve());
    }

}