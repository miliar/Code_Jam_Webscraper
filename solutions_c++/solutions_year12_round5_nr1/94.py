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

const int N = 1000 + 3;

int n;
pair<int, pt> a[N];

inline bool read()
{
    if (scanf("%d", &n) != 1)
        return false;
        
    forn(i, n)
    {
    	a[i].ft = i;
    	assert(scanf("%d", &a[i].sc.ft) == 1);
    }
    
    forn(i, n)
    	assert(scanf("%d", &a[i].sc.sc) == 1);
    	
    return true;
}

inline bool cmp(const pair<int, pt>& a, const pair<int, pt>& b)
{
	int l1 = a.sc.ft, l2 = b.sc.ft;
	ld p1 = ld(100 - a.sc.sc) / 100, p2 = ld(100 - b.sc.sc) / 100;
	
	ld v1 = l1 + p1 * l2;
	ld v2 = l2 + p2 * l1;
	
	if (abs(v1 - v2) > EPS)
		return v1 + EPS < v2;
		
	return a.ft < b.ft;
}

inline void solve(int test)
{
	cerr << test + 1 << endl;
	printf("Case #%d:", test + 1);
	
	sort(a, a + n, cmp);
	
	forn(i, n)
		printf(" %d", a[i].ft);
		
	puts("");
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
