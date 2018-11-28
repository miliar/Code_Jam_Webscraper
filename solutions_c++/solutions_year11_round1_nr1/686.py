#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <utility>
#include <map>
#include <queue>
#include <vector>
#include <cstdlib>
#include <iostream>
#define MAXN ()
#define INF
#define x first
#define y second
using namespace std;
#warning use cin/cout or %I64d for long integers

typedef long long ll;
ll n, p, pb, ps;

inline void solve()
{
    if (ps > 0 && pb == 0) goto skip;
    if (ps < 100 && pb == 100) goto skip;

    p = 100;

    if (ps % 4 == 0) p /= 4;
    else if (ps % 2 == 0) p /= 2;

    if (ps % 25 == 0) p /= 25;
    else if (ps % 5 == 0) p /= 5;

    if (p <= n) { cout << "Possible\n"; return; }
    skip:;
    cout << "Broken\n";
}

inline void read()
{
    cin >> n >> ps >> pb;
}

int main()
{
    int brt, testNo=0;
    cin >> brt;
    while (brt--)
    {
        read();
        cout << "Case #" << ++testNo << ": ";
        solve();
    }
    return 0;
}
