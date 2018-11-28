#pragma comment(linker, "/stack:65000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <functional>
#include <numeric>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

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
#define x first
#define y second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef unsigned int uint;
typedef unsigned char byte;
typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
typedef pair<ld, ld> ptd;
typedef pair<li, li> ptl;

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

const int N = 10 * 1000 + 3;

int n;
pt a[N];

inline bool read()
{
	if (scanf("%d", &n) != 1)
		return false;
		
	forn(i, n)
		assert(scanf("%d%d", &a[i].ft, &a[i].sc) == 2);
		
	assert(scanf("%d", &a[n].ft) == 1);
	a[n].sc = 0;
	n++;
		
	return true;
}

int d[N];

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	
	memset(d, -1, sizeof(d));
	
	d[0] = a[0].ft;
	
	forn(i, n)
		fore(j, i + 1, n - 1)
		{
			if (d[i] == -1 || a[j].ft - a[i].ft > d[i])
				break;
				
			d[j] = max(d[j], min(a[j].sc, a[j].ft - a[i].ft));
		}
		
	puts(d[n - 1] == -1 ? "NO" : "YES");
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
    {
        assert(read());
        solve(test);
    }
    
    return 0;
}
