#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

#define NMAX 1005

struct Line
{
    int w, len;
};

int S, R, t, n, x;
Line a[NMAX];

inline bool operator<(const Line& l1, const Line& l2)
{
    return l1.w < l2.w;
}

void solve(int test)
{
    printf("Case #%d: ", test);

    cin >> x >> S >> R >> t >> n;
    int total_len = 0;
    forn(i, n)
    {
        int b, e;
        cin >> b >> e >> a[i].w;
        a[i].len = e - b;
        total_len += a[i].len;
    }
    a[n].w = 0;
    a[n].len = x - total_len;
    n++;
    sort(a, a + n); 

    int l = 0;
    int nn = 0;
    while (l < n)
    {
        int r = l;
        int sum = 0;
        while (r < n && a[r].w == a[l].w) 
        {
            sum += a[r].len;
            r++;               
        }
        a[nn].w = a[l].w;
        a[nn].len = sum;
        nn++;

        l = r;
    }
    n = nn;

    ld tau = t;
    ld ans = 0;
    
    forn(i, n)
    {
        ld tmp = min(tau, ld(a[i].len * 1.0 / (R + a[i].w)));
        ans += tmp + (a[i].len - tmp * (R + a[i].w)) / (S + a[i].w);
        tau -= tmp;
    }

    cout << ans << endl;
}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    cout << fixed;
    cout.precision(15);

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    

    return 0;
}