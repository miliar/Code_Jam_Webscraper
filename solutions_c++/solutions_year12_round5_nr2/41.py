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

string testname = "B-large";

int dy[6] = {1, 1, 0, -1, -1, 0};
int dx[6] = {0, 1, 1, 0, -1, -1};
int n, m;

map<pii, int> num;
set<pii> vis;

bool inside(int y, int x) {
    if (y < 0 || x < 0 || y > 2*n-2 || x > 2*n-2) return false;
    if (abs(y-x) > n-1) return false;
    return true;
}

bool iscorner(int y, int x) {
    if (!inside(y, x)) return false;
    if (y == 0 && x == 0) return true;
    if (y == 2*n-2 && x == 2*n-2) return true;
    if (y == n-1 && x == 0) return true;
    if (y == 0 && x == n-1) return true;
    if (y == n-1 && x == 2*n-2) return true;
    if (y == 2*n-2 && x == n-1) return true;
    return false;
}

int isedge(int y, int x) {
    if (!inside(y, x)) return 0;
    if (iscorner(y, x)) return 0;
    if (y == 0) return 1;
    if (x == 0) return 2;
    if (y == 2*n-2) return 4;
    if (x == 2*n-2) return 8;
    if (y-x == n-1) return 16;
    if (x-y == n-1) return 32;
    return 0;
}

int bits(int x) {
    int res = 0;
    while (x) {
	x &= x-1;
	++res;
    }
    return res;
}


int edge, corner;

bool was[10000];

map<pii, int>::iterator it;
int g;

void rec(int y, int x) {
    it = num.find(pii(x, y));
    if (it == num.end()) return;
    g = it->Y;
    if (was[g]) return;
    was[g] = true;
    edge |= isedge(y, x);
    if (iscorner(y, x)) ++corner;
    REP (i, 6) {
	rec(y + dy[i], x + dx[i]);
    }
}

int S = 0;

bool inside2(int y, int x) {
    if (y < -1 || x < -1 || y > 2*n-2 + 1 || x > 2*n-2 + 1) return false;
    if (abs(y-x) > n-1 + 1) return false;
    return true;
}

void rec2(int y, int x) {
    vis.insert(pii(x, y));
    bool neigh = false;
    REP (i, 6) {
	if (num.count(pii(x + dx[i], y + dy[i]))) neigh = true;	
    }
    if (!neigh) return;
    REP (i, 6) {
	if (inside2(y + dy[i], x + dx[i]) && 
	    !vis.count(pii(x + dx[i], y + dy[i])) &&
	    !num.count(pii(x + dx[i], y + dy[i]))) {
	    rec2(y + dy[i], x + dx[i]);
	}
    }

}

void add(string & s, string f) {
    if (sz(s))
	s += "-";	
    s += f;
}

int main () {
    freopen((testname+".in").c_str(), "r", stdin);
    if (testname != "input") {
	freopen((testname+".out").c_str(), "w", stdout);
    }
    int tests;
    cin >> tests;
    FOR (test, 1, tests+1) {
	cin >> n;
	cin >> m;
	num.clear();
	bool out = false;
	cout << "Case #" << test << ": ";
	REP (i, m) {
	    int y, x;
	    cin >> y >> x;
	    if (out) continue;
	    --y, --x;
	    num[pii(x, y)] = i;
	    memset(was, 0, sizeof (was));
	    edge = corner = 0;
	    rec(y, x);
	    
	    vector<pii> haha;
	    REP (j, 6) {
		if (inside2(y + dy[j], x + dx[j]) && !num.count(pii(x + dx[j], y + dy[j]))) {
		    haha.pb(pii(x + dx[j], y + dy[j]));
	     	}
	    }
	    bool ring = false;
	    if (sz(haha)) {
		vis.clear();
		rec2(haha[0].Y, haha[0].X);
		REP (j, sz (haha)) {
		    if (!vis.count(haha[j]))
			ring = true;
		}
	    }
	    string s;
	    if (corner > 1) add(s, "bridge");
	    if (bits(edge) > 2) add(s, "fork");
	    if (ring) add(s, "ring"); 
	    if (sz(s)) {
		cout << s << " in move " << (i+1) << endl;
		out = true;
	    }
	}
	if (!out) {
	    cout << "none" << endl;
	}
    }
    return 0;
}
