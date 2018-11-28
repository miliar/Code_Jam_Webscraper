#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cassert>

#define all(x) (x).begin(), (x).end()
#define sz(v) int((v).size())
#define fori(i,b,n) for (int i = (b); i < (n); i++)
#define forn(i,n) fori(i,0,n)
#define forall(i,v) forn(i,sz(v))
#define var(x,y) typeof(y) x = y
#define foreach(it,v) for (var(it,(v).begin()); it != (v).end(); it++)
#define forreach(it,v) for (var(it,(v).rbegin()); it != (v).rend(); it++)

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

typedef set<int> iset;
typedef set<string> sset;

typedef map<int,int> iimap;

typedef vector<int> ivec;
typedef vector<vector<int> > iivec;

int X, S, R, N;

struct ss {
	int b, e, w;
	ss(int b_ = 0, int e_ = 0, int w_ = 0) : b(b_), e(e_), w(w_) {};
	bool operator < (const ss &a) const {
		return (w+R)*(w+S) < (a.w+R)*(a.w+S);
	}
};

int main() {
	int T;
	cin >> T;
	for (int CASE = 1; CASE <= T; CASE++) {
		double t;
		cin >> X >> S >> R >> t >> N;
		vector<ss> seg(N);
		forn (i, N)
			cin >> seg[i].b >> seg[i].e >> seg[i].w;
		int b = 0;
		forn (i, N) {
			if (seg[i].b > b)
				seg.push_back(ss(b, seg[i].b, 0));
			b = seg[i].e;
		}
		if (b < X)
			seg.push_back(ss(b, X, 0));
		sort(all(seg));
/* 		forall(i, seg) {
			cout << seg[i].b << ',' << seg[i].e << endl;
		} */
		double res = 0;
		forall (i,seg) {
			double d = (seg[i].e - seg[i].b);
			if (t > 0) {
				double rt = d / (R + seg[i].w);
				if (rt <= t) {
					t -= rt;
					res += rt;
				} else {
					res += t;
					d -= (R + seg[i].w) * t;
					t = 0;
					res += d / (S + seg[i].w);
				}
			} else {
				res += d / (S + seg[i].w);
			}
		}
		printf("Case #%d: %.9f\n", CASE, res);
	}
	return 0;
}
