#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <sstream>
#include <ctime>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

#define NMAX 105
#define SMAX 1000000

const ll INF = (ll)4e18;

ll L;
int n;
int b[NMAX];
ll d[SMAX + 1];

ll greedy()
{
    sort(b, b + n);

    ll v = L;

    ll ret = 0;

    for (int i = n - 1; i >= 0; i--)
    {
        ll c = v / b[i];

        ret += c;

        v %= b[i];
    }

    if (v != 0) return INF;

    return ret;
}

void solve(int tc)
{
    printf("Case #%d: ", tc);

    cerr << tc << endl;

    cin >> L >> n;

    forn(i, n) cin >> b[i];

    forn(s, SMAX + 1) d[s] = INF;

    d[0] = 0;

    forn(i, n)
    {
        for (int s = 0; s + b[i] <= SMAX; s++)
        {  
            d[s + b[i]] = min(d[s + b[i]], d[s] + 1);
        }
    }

    ll ans = INF;

    forn(i, n)
    {
        ll cur = 0;
        ll t = L;
        if (t > SMAX)
        {
            ll k = (t - SMAX + b[i] - 1) / b[i];

            cur += k;

            t -= k * b[i]; 
        }

        cur += d[t];

        ans = min(ans, cur);
    }

    if (ans == INF)
    {
        cout << "IMPOSSIBLE\n";
        return;
    }

    ans = min(ans, greedy());

    cout << ans << endl;
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);
    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    return 0;
}
            
