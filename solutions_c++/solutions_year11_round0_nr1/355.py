/*
 TASK:
 LANG: C++
 */
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iterator>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <bitset>
#include <cstring>
#include <climits>
#include <deque>
#include <utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>
#include <ctime>
#include <valarray>
//#include "vc.h"
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#if __GNUC__ > 2
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#else
#include <hash_set>
#include <hash_map>
#endif
#endif

template<class key>
struct hashtemp {

	enum {
		bucket_size = 4, min_buckets = 8
	};
	virtual size_t operator()(const key &p) const=0;

};

using namespace std;
#ifndef M_PI
const long double M_PI=acos((long double)-1);
#endif
#define rep(i,n) for(int  i=0;i<(int)(n);++i)
long double ZERO = 0;
const long double INF = 1 / ZERO, EPSILON = 1e-12;
#define all(c) (c).begin(),(c).end()
#define rep2(i,a,b) for(int i=(a);i<=((int)b);++i)
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define sz(v) ((int)((v).size()))
#define let(x,y) __typeof(y) x(y)

#define rrep(i,n) for(int  i=((int)n)-1;i>=0;--i)
#define rall(c) (c).rbegin(),(c).rend()
#define rrep2(i,a,b) for(int i=(a);i>=((int)b);--i)
#define rforeach(it,c) for(__typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)
#define rep2d(i, j, v) rep(i, sz(v)) rep(j, sz(v[i]))
#define foreach2d(i, j, v) foreach(i,v) foreach(j,*i)
int but[100];
char col[100];
struct state {
	int b, o, i;
};
bool vis[101][101][101];
int main() {
	std::ios_base::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
#endif
	int T;
	cin >> T;
	rep(t,T) {
		int n;
		cin>>n;
		rep(i,n)
			cin >> col[i]>> but[i] ;

		state s = { 1, 1, 0 };
		queue<state> q;
		q.push(s);
		int st = 0;
		memset(vis, 0, sizeof vis);
		vis[1][1][0] = 1;
		while (q.size()) {
			st++;
			int ss = q.size();
			while (ss--) {
				s = q.front();
				q.pop();
				rep2(di,-1,1) {
					rep2(dj,-1,1) {
						state ns = { s.b + di, s.o + dj, s.i };
						if (ns.o >= 1 && ns.o <= 100 && ns.b >= 1 && ns.b <= 100
								&& !vis[ns.o][ns.b][ns.i]) {
							vis[ns.o][ns.b][ns.i] = 1;
							q.push(ns);
						}
					}
					if (s.o == but[s.i] && col[s.i] == 'O') {
						state ns = s;
						ns.i++;
						ns.b += di;
						if (ns.i == n)
							goto bara;
						if (ns.o >= 1 && ns.o <= 100 && ns.b >= 1 && ns.b <= 100
								&& !vis[ns.o][ns.b][ns.i]) {
							vis[ns.o][ns.b][ns.i] = 1;
							q.push(ns);
						}
					}
					if (s.b == but[s.i] && col[s.i] == 'B') {
						state ns = s;
						ns.i++;
						ns.o += di;
						if (ns.i == n)
							goto bara;
						if (ns.o >= 1 && ns.o <= 100 && ns.b >= 1 && ns.b <= 100
								&& !vis[ns.o][ns.b][ns.i]) {
							vis[ns.o][ns.b][ns.i] = 1;
							q.push(ns);
						}
					}
				}
			}
		}
		bara: printf("Case #%d: %d\n", t + 1, st);
	}
	return 0;
}
