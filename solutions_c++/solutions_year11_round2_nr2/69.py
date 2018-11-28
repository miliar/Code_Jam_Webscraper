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
const ld EPS = 1e-10, PI = 3.1415926535897932384626433832795;

const int N = 200 + 13;

int n, d;
pt a[N];

inline bool check(ld maxt)
{
    ld last = -1e18;
    
    forn(i, n)
    {
        forn(j, a[i].sc)
        {
            ld mom = last + d;
            ld lf = a[i].ft - maxt, rg = a[i].ft + maxt;
            
            if (mom - EPS > rg)
                return false;
                
            last = max(mom, lf);
        }
    }
    
    return true;
}

void solve(int test)
{
    scanf("%d%d", &n, &d);
    
    forn(i, n)
    {
        scanf("%d%d", &a[i].ft, &a[i].sc);
        
        //a[i].ft = i;
        //a[i].sc = 5000;
    }
        
    ld lf = 0.0, rg = 1e15;
    
    forn(i, 100)
    {
        ld mid = (lf + rg) / 2.0;
        
        if (check(mid))
            rg = mid;
        else
            lf = mid;
    }
    
    printf("Case #%d: %.10lf\n", test + 1, double(rg));
    
    cerr << test + 1 << ' ' << clock() << endl;
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
        solve(test);
        
    cerr << clock() << endl;
    
    return 0;
}
