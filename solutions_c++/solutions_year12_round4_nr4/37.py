#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define all(a) (a).begin(),(a).end()
#define UN(a) sort(all(a)),(a).resize(unique(all(a))-(a).begin())
#define sz(a) ((int) (a).size())
#define pb push_back
#define CL(a,b) memset ((a), (b), sizeof (a))
#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;

string testname = "D-small-attempt0";

vector<string> a;
vector<pii> b;
int n, m;

void go(int y, int x) {
    if (y < 0 || x < 0 || y >= n || x >= m) return;
    if (a[y][x] == '#') return;
    if (count(all(b), pii(y, x))) return;
    b.pb(pii(y, x));
    go(y, x-1);
    go(y, x+1);
    go(y-1, x);
}

set<vector<pii> > was;
int maxy;

bool rec(vector<pii> h) {
    UN(h);
    if (was.count(h)) return false;
    // REP (i, sz (h)) {
    // 	cout << h[i].X << ' ' << h[i].Y << endl;
    // }
    // cout << endl;
    if (sz(h) == 1) return true;
    was.insert(h);
    vector<pii> g(h);
    REP (i, sz (g)) {
	g[i].Y--;
	if (a[g[i].X][g[i].Y] == '#')
	    g[i].Y++;
    }
    if (rec(g)) return true;
    g = h;
    REP (i, sz (g)) {
	g[i].Y++;
	if (a[g[i].X][g[i].Y] == '#')
	    g[i].Y--;
    }
    if (rec(g)) return true;
    g = h;
    bool bad = false;
    REP (i, sz (g)) {
	g[i].X++;
	if (a[g[i].X][g[i].Y] == '#')
	    g[i].X--;
	if (g[i].X > h.back().X) {
	    bad = true;
	    break;
	}
    }
    if (!bad)
	if (rec(g)) return true;
    return false;
}

bool solve(vector<pii> b) {
    sort(all(b));
    was.clear();
    maxy = b.back().X;
    return rec(b);
}

int main () {
    freopen((testname+".in").c_str(), "r", stdin);
    freopen((testname+".out").c_str(), "w", stdout);
    int tests;
    cin >> tests;
    FOR (test, 1, tests+1) {
	cin >> n >> m;
	a.clear();
	a.resize(n);
	REP (i, n) {
	    cin >> a[i];
	}
	int d = 0;
	REP (i, n) {
	    REP (j, m) if (isdigit(a[i][j])) d = max(d, a[i][j]-'0');
	}
	printf("Case #%d:\n", test);
	REP (k, d+1) {
	    REP (i, n) {
		REP (j, m) if (a[i][j] == k+'0') {
		    b.clear();
		    go(i, j);
		    printf("%d: %d", k, sz(b));
		    if (solve(b)) {
			puts(" Lucky");
		    } else {
			puts(" Unlucky");
		    }
		}
	    }
	}
    }
    return 0;
}
