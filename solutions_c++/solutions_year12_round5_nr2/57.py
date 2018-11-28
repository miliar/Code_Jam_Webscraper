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

const int N = 4000 + 3;

int s, m;

inline bool read()
{
	return scanf("%d%d", &s, &m) == 2;
}

int u = 0, used[N][N];
int dsu[N * N];

inline int getIdx(int x, int y) { return x * (2 * s + 1) + y; }
inline int getIdx(pt p) { return getIdx(p.x, p.y); }

int leader(int v) { return dsu[v] = (dsu[v] == v ? v : leader(dsu[v])); }

inline bool merge(int a, int b)
{
	a = leader(a), b = leader(b);
	
	if (a == b)
		return false;
		
	if (rand() & 1)
		dsu[a] = b;
	else
		dsu[b] = a;
		
	return true;
}

int dx[] = { 1, 1, 0, -1, -1, 0 };
int dy[] = { 0, 1, 1, 0, -1, -1 };

inline void add(int x, int y)
{
	used[x][y] = u;
	
	bool ans = false;
	
	forn(i, 6)
	{
		int xx = x + dx[i], yy = y + dy[i];
		
		if (xx < 1 || xx > 2 * s - 1)
			continue;
			
		if (yy < 1 || yy > 2 * s - 1)
			continue;
			
		if (used[xx][yy] == u)
			merge(getIdx(x, y), getIdx(xx, yy));
	}
}

vector<pt> corners;

inline bool bridge()
{
	forn(i, sz(corners))
		forn(j, i)
			if (leader(getIdx(corners[i])) == leader(getIdx(corners[j])))
			{
				//assert(used[corners[i].x][corners[i].y] == u);
				//assert(used[corners[j].x][corners[j].y] == u);
				return true;
			}
				
	return false;
}

inline bool fork()
{
	pt sx[] = { mp(1, 1), mp(1, s), mp(s, 2 * s - 1), mp(2 * s - 1, 2 * s - 1), mp(s, 2 * s - 1), mp(1, s) };
	pt sy[] = { mp(1, s), mp(s, 2 * s - 1), mp(2 * s - 1, 2 * s - 1), mp(s, 2 * s - 1), mp(1, s), mp(1, 1) };
	
	map< int, set<int> > cnt;
	
	forn(i, 6)
	{
		int x1 = sx[i].ft + (sx[i].ft != sx[i].sc), x2 = sx[i].sc - (sx[i].ft != sx[i].sc), dx = 1;
		int y1 = sy[i].ft + (sy[i].ft != sy[i].sc), y2 = sy[i].sc - (sy[i].ft != sy[i].sc), dy = 1;
		
		if (sx[i].ft == sx[i].sc || sy[i].ft == sy[i].sc)
		{
    		for (int x = x1; x <= x2; x += dx)
    			for (int y = y1; y <= y2; y += dy)
    			{
    				//cerr << x << ' ' << y << endl;
    				cnt[leader(getIdx(x, y))].insert(i);
    			}
		}
		else
		{
    		for (int x = x1, y = y1; x <= x2 && y <= y2; x += dx, y += dy)
    			{
    				//cerr << x << ' ' << y << endl;
    				cnt[leader(getIdx(x, y))].insert(i);
    			}
		}
	}
	
	for (map<int, set<int> >::iterator i = cnt.begin(); i != cnt.end(); i++)
		if (sz(i->sc) > 2)
			return true;
			
	return false;
}

int uu = 0, us[N][N];

int dfs(int x, int y)
{
	int ans = 1;
	us[x][y] = uu;
	
	forn(i, 6)
	{
		int xx = x + dx[i], yy = y + dy[i];
		
		if (!correct(xx, yy, 2 * s + 1, 2 * s + 1))
			continue;
			
		if (used[xx][yy] == u || us[xx][yy] == uu)
			continue;
			
		ans += dfs(xx, yy);
	}
	
	return ans;
}

inline bool ring()
{
	uu++;
	dfs(0, 0);
	
	forl(i, 2 * s - 1)
		forl(j, 2 * s - 1)
			if (used[i][j] != u && us[i][j] != uu)
				return true;
				
	return false;
}

inline void solve(int test)
{
	u++;
	
	cerr << test + 1 << endl;
	printf("Case #%d: ", test + 1);
	
	forn(i, 2 * s + 1)
		forn(j, 2 * s + 1)
			dsu[getIdx(i, j)] = getIdx(i, j);
			
	corners.clear();
	corners.pb(mp(1, 1));
	corners.pb(mp(1, s));
	corners.pb(mp(s, 2 * s - 1));
	corners.pb(mp(2 * s - 1, 2 * s - 1));
	corners.pb(mp(2 * s - 1, s));
	corners.pb(mp(s, 1));
	
	vector<string> ans;
	
	forn(i, m)
	{
		int x, y;
		assert(scanf("%d%d", &x, &y) == 2);
		
		add(x, y);
		
		if (ring())
			ans.pb("ring");
			
		if (bridge())
			ans.pb("bridge");
			
		if (fork())
			ans.pb("fork");
			
		if (!ans.empty())
		{
			sort(all(ans));
			
			string res;
			
			forn(j, sz(ans))
			{
				if (j > 0)
					res.pb('-');
				res += ans[j];
			}
			
			printf(res.c_str());
			printf(" in move %d\n", i + 1);
			
			i++;
			
			while (i < m)
			{
				assert(scanf("%d%d", &x, &y) == 2);
				i++;
			}
			
			return;
		}
	}
	
	puts("none");
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
