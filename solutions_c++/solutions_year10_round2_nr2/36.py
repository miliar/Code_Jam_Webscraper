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

#define NMAX 55
#define INF 1000000000

int x[NMAX], t;
int b;
int v[NMAX];
int n, k;
int d[NMAX][NMAX];

void solve(int tc)
{
    printf("Case #%d: ", tc);
    cin >> n >> k >> b >> t;
    forn(i, n) cin >> x[i];
    forn(i, n) cin >> v[i];

    forn(i, n + 1) forn(j, n + 1) d[i][j] = INF;

    d[n][0] = 0;

    for (int i = n - 1; i >= 0; i--)
    {
        for (int j = 0; j < n - i; j++)
        {
            if (d[i + 1][j] == INF) continue;

            d[i][j] = min(d[i][j], d[i + 1][j]);
                
            if ((b - x[i]) <= v[i] * t)
            {
                d[i][j + 1] = min(d[i][j + 1], d[i + 1][j] + n - i - 1 - j);
            }
        }
    }

    int ans = INF;

    for (int i = k; i <= n; i++) ans = min(ans, d[0][i]);

    if (ans == INF) cout << "IMPOSSIBLE\n"; else cout << ans << endl;
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
            
