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

#define NMAX 505

const ll M = 100003;

ll c[NMAX][NMAX], d[NMAX][NMAX];

void solve(int tc)
{
    printf("Case #%d: ", tc);
    int n;
    cin >> n;
    ll ans = 0;
    for1(i, n - 1) ans = (ans + d[n][i]) % M;

    cout << ans << endl;
}

void pre_calc()
{
    forn(i, NMAX)
    {
        c[0][i] = c[i][i] = 1;
    }    

    for (int j = 2; j < NMAX; j++)
    {
        for (int i = 1; i < j; i++)
        {
            c[i][j] = (c[i - 1][j - 1] + c[i][j - 1]) % M;
        }
    }

    for (int n = 2; n <= 500; n++)
    {
        d[n][1] = 1;

        for (int k = 2; k < n; k++)
        {
            for (int i = 1; i < k; i++)
            {
                d[n][k] = (d[n][k] + d[k][i] * c[k - i - 1][n - k - 1]) % M;
            }
        }
    }
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);
    pre_calc();
    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    return 0;
}
            
