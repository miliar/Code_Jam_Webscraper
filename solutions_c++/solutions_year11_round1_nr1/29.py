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

ll gcd(ll a, ll b)
{
    if (a == 0) return b;
    return gcd(b % a, a);
}

void solve(int test)
{
    printf("Case #%d: ", test);

    ll n, pd, pg;
    cin >> n >> pd >> pg;

    ll d = gcd(pd, 100);
    if (d !=0 && 100 / d > n)
    {
        cout << "Broken\n";
        return;
    }

    if (pg == 0 && pd != 0)
    {
        cout << "Broken\n";
        return;
    }

    if (pg == 100 && pd != 100)
    {
        cout << "Broken\n";
        return;
    }

    cout << "Possible\n";
}

void solve2(int test)
{
    printf("Case #%d: ", test);
    int n, pd, pg;
    cin >> n >> pd >> pg;
    
    for (int d = 1; d <= n; d++)
    {
        for (int g = d; g <= 1000000; g++)
        {
            if ((d * pd) % 100 == 0 && (g * pg) % 100 == 0 && d * pd <= g * pg && (100 - pd) * d <= (100 - pg) * g)
            {
                cout << "Possible\n";
                return;
            }
        }
    }
    cout << "Broken\n";
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