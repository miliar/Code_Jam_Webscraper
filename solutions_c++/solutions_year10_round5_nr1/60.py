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

#define VMAX 1000006
#define KMAX 12

bool used[VMAX];
int p[VMAX];
int cp;
int k, d;
ll s[KMAX];

void ee(ll a, ll b, ll& x, ll& y)
{
    if (b == 0)
    {
        x = 1;
        y = 0;
        return;
    }

    ll x1, y1;

    ee(b, a % b, x1, y1);

    x = y1;
    y = x1 - (a / b) * y1;
}

ll get_rev(ll a, ll n)
{
    ll x, y;
    ee(a, n, x, y);
    return (x % n + n) % n;
}

ll calc(ll p)
{
    if (k == 1) return -2;
    if (k == 2)
    {
        if (s[0] == s[1]) return s[0];
        ll nx = -1;

        for (ll a = 0; a < p; a++)
        {
            ll b = (s[1] - (s[0] * a) % p + p) % p;
            ll c = (s[1] * a + b) % p;

            if (nx != -1 && c != nx) return -2; 

            nx = c;
        }

        return nx;
    }

    if (s[0] == s[1])
    {
        forn(i, k) if (s[i] != s[0]) return -1;
        return s[0];
    }

    ll v1 = (s[2] - s[1] + p) % p;
    ll v2 = (s[1] - s[0] + p) % p;

    ll a = v1 * get_rev(v2, p);

    ll b = (s[1] - (a * s[0]) % p + 2 * p) % p;

    for1(i, k - 1)
    {
        if (s[i] != (a * s[i - 1] + b) % p) return -1;
    }

    return (s[k - 1] * a + b) % p;
}

string toString(ll x)
{
    ostringstream sout;
    sout << x;
    return sout.str();
}

void read()
{
    cin >> d >> k;
    forn(i, k) cin >> s[i];
}

string solve()
{
    int mx = 0;

    forn(i, k) mx = max(mx, (int)s[i]);

    ll next = -1;

    int Q = 1;

    forn(it, d) Q *= 10;


    forn(i, cp)
    {
        if (p[i] <= mx) continue;

        if (p[i] > Q) break;

        ll c = calc(p[i]);

        if (c == -1) continue;

        if (c == -2)
        {
            return "I don't know.";
        } 

        if (next != -1 && c != next)
        {            
            return "I don't know.";
        }

        next = c;
    }

    if (next == -1)
    {
        assert(false);
    }

    return toString(next);
}

string stup()
{
    int mx = 0;

    forn(i, k) mx = max(mx, (int)s[i]);

    if (k == 1) return "I don't know.";

    int nx = -1;

    int Q = 1;

    forn(it, d) Q *= 10;

    forn(i, cp)
    {        
        if (p[i] <= mx) continue;

        if (p[i] > Q) break;

        cerr << p[i] << endl;

        int pp = p[i];

        for (int a = 0; a < pp; a++)
        {
            int b = (s[1] - (s[0] * a) % pp + pp) % pp;

            bool ok = true;

            for (int i = 2; i < k; i++)
            {
                if (s[i] != (s[i - 1] * a + b) % pp)
                {
                    ok = false;
                    break;
                }
            }

            if (!ok) continue;

            int c = (s[k - 1] * a + b) % pp;

            if (nx != -1 && c != nx) return "I don't know."; 

            nx = c;
        }

    }

    if (nx == -1)
    {
        assert(false);
    }

    return toString(nx);    
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    for (int i = 2; i < VMAX; i++)
    {
        if (used[i]) continue;
        p[cp++] = i;
        for (int j = i + i; j < VMAX; j += i) used[j] = true;
    }

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc)
    {
        read();
        printf("Case #%d: ", it + 1);

        cerr << it + 1 << endl;

        //assert(solve() == stup());

        cout << solve() << endl;
    }
    return 0;
}
            
