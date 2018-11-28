#include <iostream>
#include <algorithm>
#include <limits>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <numeric>
#include <iomanip>
using namespace std;

#define forl(i, s, t) for(__typeof(s) i = s; i < t; i++)
#define rforl(i, s, t) for(__typeof(s) i = s; i > t; i--)
#define foreach(itr, c) forl(itr, (c).begin(), (c).end())
#define rforeach(itr, c) forl(itr, (c).rbegin(), (c).rend())

#define rep(n) forl(rep_c, 0, n)
#define fill2d_nn(g, s, z, v) forl(i, 0, s) fill_n(g[i], z, v)
#define fill2d_n(g, s, v) fill2d_nn(g, s, s, v)
//#define read(s, t) forloop(read_c, s, t) cin >> *read_c
//inline void read(ForwardIterator s, ForwardIterator e) { forloop(i, s, e) cin >> *i; }
//#define read_n(x, n) forl(read_n_c, 0, n) cin >> x[read_n_c]
//#define rread_n(x, n) rforl(rread_n_c, n-1, -1) cin >> x[rread_n_c]

#define tpop(x) (x).top(); (x).pop()
#define fpop(x) (x).front(); (x).pop()
//#define all(x) (x).begin(), (x).end()
#define pb(a) push_back(a)
#define mp(a, b) make_pair(a, b)

//#define chmin(a, b) a = min(a, b)
//#define chmax(a, b) a = max(a, b)
template<typename T> inline void chmin(T& a, const T& b) { a = min(a, b); }
template<typename T> inline void chmax(T& a, const T& b) { a = max(a, b); }

int gcd(int a, int b) { if(b == 0) return a; return gcd(b, a % b); }
#define gcd_n(a, n) accumulate(a+1, a+n, a[0], gcd);
template <class ForwardIterator>
inline int gcd_r(ForwardIterator s, ForwardIterator e) { return accumulate(s+1, e, s[0], gcd); }

#ifdef DEBUG
#define varcontent(v) #v << '=' << v
#define debug(v) cerr << varcontent(v) << endl
#define pdebug(v, w) cerr << '(' << varcontent(v) << ',' << varcontent(w) << ')' << endl
#define dmsg(a) cerr << a << endl
#else
#define varcontent(v) 0
#define debug(v) 0
#define pdebug(v, w) 0
#define dmsg(a) 0
#endif

#define printarr(a, n) cerr << #a << " = ["; forloop(i, 0, n) cerr << a[i] << ' '; cerr.seekp(cerr.tellp()-1L); cerr << ']' << endl
#define printgrid(g, y, x) cerr << endl << #g << ':' << endl; forloop(i, 0, y) { forloop(j, 0, x) cerr << g[i][j] << ' '; cerr << endl; } cerr << endl
#define rprintgrid(g, x, y) cerr << endl << #g << ':' << endl; forloop(i, 0, x) { forloop(j, 0, y) cerr << g[j][i] << ' '; cerr << endl; } cerr << endl
/*inline void printgrid(RandomAccessIterator g, int y, int x) {
	cerr << endl << #g << ':' << endl;
	forloop(i, 0, y) {
		forloop(j, 0, x) cout<< g[i][j] << ' ';
		cout << endl;
	}
	cerr << endl;
}*/
/*inline void rprintgrid(RandomAccessIterator g, int x, int y) {
	cerr << endl << #g << ':' << endl;
	forloop(i, 0, x) {
		forloop(j, 0, y) cout<< g[j][i] << ' ';
		cout << endl;
	}
	cerr << endl;
}*/

const int INF = numeric_limits<int>::max()/2;
const double EPS = INF*numeric_limits<double>::epsilon();

void gcjmain() {
	vector< vector<char> > grid(4, vector<char>(4));
	bool complete = true;
	bool xwin = false, owin = false;
	forl(r, 0, 4) {
		char cur = 'T';
		int count = 0;
		forl(c, 0, 4) {
			cin >> grid[r][c];
			if(grid[r][c] == '.') complete = false;
			if(cur == 'T') {
				cur = grid[r][c];
				count++;
			}
			else if(cur == '.') {}
			else if(grid[r][c] == 'T' || grid[r][c] == cur) {
				count++;
			}
		}
		if(count == 4) {
			if(cur == 'X') xwin = true;
			else if(cur == 'O') owin = true;
		}
	}
	forl(c, 0, 4) {
		char cur = 'T';
		int count = 0;
		forl(r, 0, 4) {
			if(cur == 'T') {
				cur = grid[r][c];
				count++;
			}
			else if(cur == '.') {}
			else if(grid[r][c] == 'T' || grid[r][c] == cur) {
				count++;
			}
		}
		if(count == 4) {
			if(cur == 'X') xwin = true;
			else if(cur == 'O') owin = true;
		}
	}
	{
	char cur = 'T';
	int count = 0;
	forl(r, 0, 4) {
		int c = r;
		if(cur == 'T') {
			cur = grid[r][c];
			count++;
		}
		else if(cur == '.') {}
		else if(grid[r][c] == 'T' || grid[r][c] == cur) {
			count++;
		}
	}
	if(count == 4) {
		if(cur == 'X') xwin = true;
		else if(cur == 'O') owin = true;
	}
	}
	{
	char cur = 'T';
	int count = 0;
	forl(r, 0, 4) {
		int c = 3-r;
		if(cur == 'T') {
			cur = grid[r][c];
			count++;
		}
		else if(cur == '.') {}
		else if(grid[r][c] == 'T' || grid[r][c] == cur) {
			count++;
		}
	}
	if(count == 4) {
		if(cur == 'X') xwin = true;
		else if(cur == 'O') owin = true;
	}
	}
	if(xwin) cout << "X won" << endl;
	else if(owin) cout << "O won" << endl;
	else if(!complete) cout << "Game has not completed" << endl;
	else cout << "Draw" << endl;
}

int main() {
	int T;
	cin >> T;
	forl(t, 1, T+1) {
		cerr << "Case: " << t << '/' << T << endl;
		cout << "Case #" << t << ": ";
		gcjmain();
	}
}
