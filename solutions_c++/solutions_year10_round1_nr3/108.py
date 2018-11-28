#include <cstdio>
#include <iostream>
#include <string>
#include <memory.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <utility>
#include <cmath>
#include <set>
#include <sstream>
#include <map>
using namespace std;

#define mp make_pair
#define pb push_back
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(n); ++i)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

const int maxn = 1000005;

int g[maxn];



int calc(int a, int b)
{
    if (b < 1) return 0;
    if (b <= g[a-1]) return b;
    if (b <= g[a-1]+a) return g[a-1];
    return b-a;
}

int f[1024][1024];

int solve(int a, int b)
{
    if (a <= 0 || b <= 0) return 0;
    int& res = f[a][b];
    if (res != -1) return res;
    res = 0;
    for (int k=1; a*k<b; ++k)
        if (!solve(a, b-a*k)) return res=1;
    for (int k=1; b*k<a; ++k)
        if (!solve(a-b*k, b)) return res=1;
    return res;
}


int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);

    g[0] = 0;
    for (int i=1; i<maxn; ++i)
        g[i] = i-g[g[i-1]];

 



    int tc;
    scanf("%d", &tc);

    for (int tt=1; tt<=tc; ++tt)
    {
        printf("Case #%d: ", tt);
        int a1, a2, b1, b2;
        scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
        ll res = 0;
        for (int a=a1; a<=a2; ++a)
            res += calc(a, b2)-calc(a, b1-1);

        cout << res << endl;

    }

    return 0;
}
