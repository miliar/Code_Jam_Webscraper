#include <iostream>
#include <algorithm>
#include <limits>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <numeric>
#include <iterator>
using namespace std;

#define forloop(i, s, t) for(__typeof(s) i = s; i < t; i++)
#define rforloop(i, s, t) for(__typeof(s) i = s; i > t; i--)
#define foreach(itr, c) for(__typeof((c).begin()) itr = (c).begin(); itr != (c).end(); itr++)
#define rforeach(itr, c) for(__typeof((c).begin()) itr = (c).rbegin(); itr != (c).rend(); itr++)

#define rep(n) forloop(rep_c, 0, n)
#define fill2d_nn(g, s, z, v) forloop(i, 0, s) fill_n(g[i], z, v)
#define fill2d_n(g, s, v) fill2d_nn(g, s, s, v)
//#define read(s, t) forloop(read_c, s, t) cin >> *read_c
//inline void read(ForwardIterator s, ForwardIterator e) { forloop(i, s, e) cin >> *i; }
#define read_n(x, n) forloop(read_n_c, 0, n) cin >> x[read_n_c]
#define rread_n(x, n) rforloop(rread_n_c, n-1, -1) cin >> x[rread_n_c]

#define tpop(x) (x).top(); (x).pop()
#define fpop(x) (x).front(); (x).pop()
#define all(x) (x).begin(), (x).end()
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

#define varcontent(v) #v << '=' << v
#define debug(v) cerr << varcontent(v) << endl
#define pdebug(v, w) cerr << '(' << varcontent(v) << ',' << varcontent(w) << ')' << endl

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

#define gcase int T; cin >> T; for(int gtest = 1; gtest <= T; gtest++)
#define gstate() cerr << "Case: " << gtest << '/' << T << endl
#define gout cout << "Case #" << gtest << ": "

const int INF = numeric_limits<int>::max()/2;
const double EPS = INF*numeric_limits<double>::epsilon();

int main() {
	gcase {
		gstate();
		int N;
		cin >> N;
		int m = INF, cur = 0, sum = 0;
		forloop(n, 0, N) {
			int C;
			cin >> C;
			sum += C;
			chmin(m, C);
			cur ^= C;
		}
		if(cur) gout << "NO" << endl;
		else gout << sum-m << endl;
	}
}
