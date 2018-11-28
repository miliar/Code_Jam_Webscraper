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

#define VMAX 2100
#define PMAX 13
#define INF 1000000000

int cost[VMAX];
int d[VMAX][PMAX];
int p, n;
int m[VMAX];

void solve(int tc)
{
    printf("Case #%d: ", tc);
    cin >> p;
    n = (1 << p);
    forn(i, n) cin >> m[i];

    for (int i = p - 1; i >= 0; i--)
	{
		int id = (1 << i);
		forn(j, id)
		{
			cin >> cost[id + j];
		}
	}

    forn(i, 2 * n) forn(j, p + 2) d[i][j] = INF;

    forn(i, n)
    {
        d[i + n][m[i]] = 0;
    }

    for (int v = n - 1; v > 0; v--)
    {
        forn(i, p + 1)
        {
            int l = (v << 1);
            int r = (v << 1) + 1;

            for (int j = i; j <= p; j++)
            {
                for (int k = i; k <= p; k++)
                {
                    if (j > i && k > i)
                    {
                        d[v][i] = min(d[v][i], d[l][j] + d[r][k]);
                    }
                    else
                    {
                        d[v][i] = min(d[v][i], d[l][j] + d[r][k] + cost[v]);
                    }
                }
            } 
        }    
    }

    int ans = INF;

    forn(j, p + 1) ans = min(ans, d[1][j]);

    cout << ans << endl;
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);
    int tc;
    cin >> tc;
    forn(it, tc) solve(it + 1);
    return 0;
}
            
