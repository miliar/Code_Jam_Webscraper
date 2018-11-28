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

const int N = 100 + 13;

int n;
char a[N][N];

ld WP[N];
ld OWP[N];
ld OOWP[N];

void solve(int test)
{
    scanf("%d", &n);
    
    forn(i, n)
        scanf("%s", a[i]);
        
    forn(i, n)
    {
        ld sum = 0.0, tcnt = 0.0;
        
        forn(j, n)
            if (a[i][j] == '1')
                sum += 1.0, tcnt += 1.0;
            else if (a[i][j] == '0')
                tcnt += 1.0;
                
        WP[i] = sum / tcnt;
    }
        
    forn(i, n)
    {
        ld sum = 0.0, tcnt = 0.0;
        
        forn(j, n)
            if (j != i)
            {
                if (a[i][j] == '.')
                    continue;
            
                ld cnt = 0.0, all = 0.0;
                
                forn(k, n)
                {
                    if (k == i)
                        continue;
                
                    if (a[j][k] == '1')
                        cnt += 1.0, all += 1.0;
                    else if (a[j][k] == '0')
                        all += 1.0;
                }
                        
                sum += cnt / all;
                tcnt += 1.0;
            }
            
        if (abs(tcnt) > EPS)
            sum /= tcnt;
            
        OWP[i] = sum;
    }
    
    forn(i, n)
    {
        ld tcnt = 0.0;
        OOWP[i] = 0.0;
        
        forn(j, n)
            if (j != i && a[i][j] != '.')
                OOWP[i] += OWP[j], tcnt += 1.0;
                
        if (abs(tcnt) > EPS)
            OOWP[i] /= tcnt;
    }
    
    printf("Case #%d:\n", test + 1);
    
    forn(i, n)
        printf("%.10lf\n", double(0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]));
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
        solve(test);
    
    return 0;
}
