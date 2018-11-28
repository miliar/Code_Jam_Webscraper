#pragma comment(linker, "/stack:64000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cstring>
#include <ctime>
#include <cmath>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <utility>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define ft first
#define sc second
#define X first
#define Y second

using namespace std;

typedef unsigned int uint;
typedef unsigned char byte;
typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
typedef pair<ld, ld> ptd;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

const int N = 500 + 13;

int n, m, d;
char c[N][N];
int a[N][N];

void read()
{
    scanf("%d%d%d", &n, &m, &d);
    
    forn(i, n)
        scanf("%s", c[i]);
        
    forn(i, n)
        forn(j, m)
            a[i][j] = (c[i][j] - '0') + d;
}

li mh[N][N], mv[N][N];

inline li hmass(int i, int l, int r)
{
    return mh[i][r] - (l == 0? 0: mh[i][l - 1]);
}

inline li vmass(int j, int l, int r)
{
    return mv[j][r] - (l == 0? 0: mv[j][l - 1]);
}

li xh[N][N], xv[N][N];

inline li xhmass(int i, int l, int r)
{
    return xh[i][r] - (l == 0? 0: xh[i][l - 1]);
}

inline li xvmass(int j, int l, int r)
{
    return xv[j][r] - (l == 0? 0: xv[j][l - 1]);
}

li yh[N][N], yv[N][N];

inline li yhmass(int i, int l, int r)
{
    return yh[i][r] - (l == 0? 0: yh[i][l - 1]);
}

inline li yvmass(int j, int l, int r)
{
    return yv[j][r] - (l == 0? 0: yv[j][l - 1]);
}

li mass[N][N], massx[N][N], massy[N][N];

void solve(int test)
{
    forn(i, n)
        forn(j, m)
        {
            mh[i][j] = (j == 0? 0: mh[i][j - 1]) + a[i][j];
            mv[j][i] = (i == 0? 0: mv[j][i - 1]) + a[i][j];
            
            xh[i][j] = (j == 0? 0: xh[i][j - 1]) + a[i][j] * i;
            xv[j][i] = (i == 0? 0: xv[j][i - 1]) + a[i][j] * i;
            
            yh[i][j] = (j == 0? 0: yh[i][j - 1]) + a[i][j] * j;
            yv[j][i] = (i == 0? 0: yv[j][i - 1]) + a[i][j] * j;
        }

    int ansVal = 0;

    for (int len = min(n, m); len >= 3; len--)
    {
        mass[0][0] = 0;
        massx[0][0] = 0;
        massy[0][0] = 0;
        
        forn(i, len)
        {
            mass[0][0] += hmass(i, 0, len - 1);
            massx[0][0] += xhmass(i, 0, len - 1);
            massy[0][0] += yhmass(i, 0, len - 1);
        }
            
        forn(i, n - len + 1)
            forn(j, m - len + 1)
            {
                if (i > 0)
                    mass[i][j] = mass[i - 1][j] - hmass(i - 1, j, j + len - 1) + hmass(i + len - 1, j, j + len - 1);
                else if (j > 0)
                    mass[i][j] = mass[i][j - 1] - vmass(j - 1, i, i + len - 1) + vmass(j + len - 1, i, i + len - 1);
                    
                if (i > 0)
                    massx[i][j] = massx[i - 1][j] - xhmass(i - 1, j, j + len - 1) + xhmass(i + len - 1, j, j + len - 1);
                else if (j > 0)
                    massx[i][j] = massx[i][j - 1] - xvmass(j - 1, i, i + len - 1) + xvmass(j + len - 1, i, i + len - 1);
                    
                if (i > 0)
                    massy[i][j] = massy[i - 1][j] - yhmass(i - 1, j, j + len - 1) + yhmass(i + len - 1, j, j + len - 1);
                else if (j > 0)
                    massy[i][j] = massy[i][j - 1] - yvmass(j - 1, i, i + len - 1) + yvmass(j + len - 1, i, i + len - 1);
                    
                li curm = mass[i][j] - a[i][j] - a[i + len - 1][j] - a[i][j + len - 1] - a[i + len - 1][j + len - 1];
                li curmx = massx[i][j] - a[i][j] * i - a[i + len - 1][j] * (i + len - 1) - a[i][j + len - 1] * i - a[i + len - 1][j + len - 1] * (i + len - 1);
                li curmy = massy[i][j] - a[i][j] * j - a[i + len - 1][j] * j - a[i][j + len - 1] * (j + len - 1) - a[i + len - 1][j + len - 1] * (j + len - 1);
                
                if ((i + (i + len - 1)) * curm == 2 * curmx && (j + (j + len - 1)) * curm == 2 * curmy)
                {
                    ansVal = len;
                    goto done;
                }
            }
    }
    
done:;

    printf("Case #%d: ", test + 1);
    
    if (ansVal == 0)
        puts("IMPOSSIBLE");
    else
        printf("%d\n", ansVal);
        
    cerr << test + 1 << endl;
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
    {
        read();
        solve(test);
    }
    
    return 0;
}
