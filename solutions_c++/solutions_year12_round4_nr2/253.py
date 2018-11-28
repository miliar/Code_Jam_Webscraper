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

const int N = 10000 + 3;

int n, w, l;
pt q[N];
int r[N];
int perm[N];

inline bool read()
{
	if (scanf("%d%d%d", &n, &w, &l) != 3)
		return false;
		
	forn(i, n)
	{
		assert(scanf("%d", &r[i]) == 1);
		q[i] = mp(r[i], i);
	}
	
	sort(r, r + n, greater<int> ());
	sort(q, q + n, greater<pt> ());
	
	forn(i, n)
		perm[q[i].sc] = i;
		
	return true;
}

int x[N], y[N];

pt z[N];
int sz, xs[N];

inline bool solve2(bool inv)
{
	forn(i, n)
	{
		sz = 0;
		xs[sz++] = 0;
		xs[sz++] = w;
		
		forn(j, i)
		{
			int xx[] = { x[j] - r[j] - r[i], x[j] - r[i], x[j] + r[i], x[j] + r[j] + r[i] };
			
			forn(k, 4)
				if (0 <= xx[k] && xx[k] <= w)
					xs[sz++] = xx[k];
					
			z[j] = mp(x[j] - r[j], j);
		}
		
		sort(xs, xs + sz);
		sort(z, z + i);
		
		/*cerr << i << endl;
		
		forn(j, i)
			cerr << z[j].ft << ' ' << z[j].sc << endl;
		
		cerr << endl << endl;*/
		
		set<pt> a;
		set< pt, greater<pt> > b;
		
		int p = 0;
		
		bool found = false;
		
		forn(j, sz)
		{
			while (p < i && z[p].ft < xs[j] + r[i])
			{
				int idx = z[p].sc;
				a.insert(mp(z[p].ft + 2 * r[idx], z[p].sc));
				b.insert(mp(y[idx] + r[idx], idx));
				p++;
			}
			
			while (!a.empty() && a.begin()->ft <= xs[j] - r[i])
			{
				int idx = a.begin()->sc;
				b.erase(mp(y[idx] + r[idx], idx));
				a.erase(a.begin());
			}
			
			if (b.empty() || b.begin()->ft + r[i] <= l)
			{
				x[i] = xs[j];
				y[i] = b.empty() ? 0 : (b.begin()->ft + r[i]);
				found = true;
				break;
			}
		}
		
		assert(found);
	}
	
	forn(i, n)
		if (!inv)
			printf(" %d %d", x[perm[i]], y[perm[i]]);
		else
			printf(" %d %d", y[perm[i]], x[perm[i]]);
			
	puts("");
	
	return true;
}

inline void solve(int test)
{
	cerr << test + 1 << endl;
	printf("Case #%d:", test + 1);
	
	forn(i, 2)
	{
		if (solve2(i))
			return;
			
		swap(w, l);
	}
	
	throw;
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
