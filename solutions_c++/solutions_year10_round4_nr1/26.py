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

#define NMAX 205

int k;
int t[NMAX][NMAX];
int a[NMAX][NMAX];
int last[NMAX];

void solve(int tc)
{
    printf("Case #%d: ", tc);
    cerr << tc << endl;

    cin >> k;

    forn(i, 2 * k - 1)
    {
        int len;
        if (i < k) len = i + 1; else len = 2 * k - i - 1;

        forn(j, len)
        {
            cin >> t[i][j];
        } 

        last[i] = len - 1;
    }

    forn(i, k)
    {
        int qnt = 0;

        forn(j, 2 * k - 1)
        {
            if (last[j] == -1) continue;

            a[i][qnt++] = t[j][last[j]];
            last[j]--;

            if (qnt == k) break;
        }
    }

    for (int n = k;; n++)
    {
        for (int x0 = 0; x0 + k <= n; x0++)
        {
            for (int y0 = 0; y0 + k <= n; y0++)
            {
                bool ok = true;

                forn(i, k)
                {
                    forn(j, k)
                    {
                        int x = x0 + i;
                        int y = y0 + j;

                        int ii = y - x0;
                        int jj = x - y0;

                        if (ii >= 0 && jj >= 0 && ii < k && jj < k && a[i][j] != a[ii][jj])
                        {
                            ok = false;
                            break;
                        }

                        ii = n - y - 1 - x0;
                        jj = n - x - 1 - y0;

                        if (ii >= 0 && jj >= 0 && ii < k && jj < k && a[i][j] != a[ii][jj])
                        {
                            ok = false;
                            break;
                        }
                    }
                    if (!ok) break;
                }

                if (ok)
                {
                    cout << n * n - k * k << endl;
                    return;
                }
            }
        }
    }
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
            
