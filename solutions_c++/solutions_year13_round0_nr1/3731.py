#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <sstream>
#include <complex>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long       li;
typedef vector<li>      vi;
typedef complex<double> pt;
typedef pair<pt, pt>    line;
typedef pair<li, li>    pi;
typedef vector<string>  vs;

#define rep(i,to)       for(li i=0;i<((li)to);i++)
#define foreach(it,set) for(__typeof((set).begin()) it=(set).begin();it!=(set).end();it++)
#define all(v)          v.begin(), v.end()

inline li bit(li n){ return 1LL<<n; }
template <class T> ostream& operator<<(ostream& os, vector<T> x){
  foreach(it, x) os << *it << ' ';
  return os;
}
template <class T> inline void dbg(T x){
  // return;
  cerr << x << endl; 
}

li vx[8] = {1, -1, 0,  0, -1, 1,  1, -1};
li vy[8] = {0,  0, 1, -1, -1, 1, -1,  1};

int check(string row) {
    const int n = 4;

    int o = 0, x = 0;
    rep(i, n) {
	if (row[i] == 'O' || row[i] == 'T') o++;
	if (row[i] == 'X' || row[i] == 'T') x++;
    }

    if (o == 4) return 1;
    if (x == 4) return -1;
    return 0;
}

void solve(int caseNum) {
    const int n = 4;

    vector<string> b(n);
    rep(i, n) cin >> b[i];

    int res;
    string ans, row;
    bool finished = true;
    rep(i, n) {
	row = "";
	rep (j, n) {
	    row.push_back(b[i][j]);
	}
	int res = check(row);
	if (res) {
	    ans = res > 0 ? "O won" : "X won";
	    goto solved;
	}
    }

    rep(j, n) {
	row = "";
	rep (i, n) {
	    row.push_back(b[i][j]);
	}
	int res = check(row);
	if (res) {
	    ans = res > 0 ? "O won" : "X won";
	    goto solved;
	}
    }

    row = "";
    rep (i, n) {
	row.push_back(b[i][i]);
    }
    res = check(row);
    if (res) {
	ans = res > 0 ? "O won" : "X won";
	goto solved;
    }

    row = "";
    rep (i, n) {
	row.push_back(b[i][n-1-i]);
    }
    res = check(row);
    if (res) {
	ans = res > 0 ? "O won" : "X won";
	goto solved;
    }


    rep(i, n) rep(j, n) if (b[i][j] == '.') finished = false;

    ans = finished ? "Draw" : "Game has not completed";
    
  solved:
    cout << "Case #" << caseNum << ": " << ans << endl;
    return;
}

int main() {
    int n;
    cin >> n;
    rep(i, n) solve(i + 1);
    return 0;
}
