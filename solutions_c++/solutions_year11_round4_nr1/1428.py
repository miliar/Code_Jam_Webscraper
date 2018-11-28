/*
USER:
TASK:
ALGO:
*/
/*
#pragma warning (disable: 4786)
#pragma comment (linker, "/STACK:0x800000")
*/
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <utility>
using namespace std;

template< class T > T _abs(T n) { return (n < 0 ? -n : n); }
template< class T > T _max(T a, T b) { return (!(a < b) ? a : b); }
template< class T > T _min(T a, T b) { return (a < b ? a : b); }
template< class T > T sq(T x) { return x * x; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > bool inside(T a, T b, T c) { return a<=b && b<=c; }

#define MP(x, y) make_pair(x, y)
#define REV(s, e) reverse(s, e)
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define SZ(c) (int)c.size()
#define PB(x) push_back(x)
#define ff first
#define ss second
#define i64 long long
#define ld long double
#define pii pair< int, int >
#define ppi pair< int, pii >
#define psi pair< string, int >

const double EPS = 1e-10;
const int INF = 0x7f7f7f7f; 

vector< ppi > W;

int main() {
	READ("A-large.in");
	WRITE("A-large.out");
	int test, cs = 1, X, S, R, t, n, a, b, w, i;
	double dt, tn, dx, run, walk, ddx, tp;
	scanf("%d", &test);
	while(test--) {
		scanf("%d %d %d %d %d", &X, &S, &R, &t, &n);
		W.clear();
		for(i = 0; i < n; i++) {
			scanf("%d %d %d", &a, &b, &w);
			W.PB(ppi(w, pii(a, b)));
		}
		if(W[0].ss.ff) W.PB(ppi(0, pii(0, W[0].ss.ff)));
		for(i = 1; i < n; i++) {
			if(W[i].ss.ff != W[i-1].ss.ss) {
				W.PB(ppi(0, pii(W[i-1].ss.ss, W[i].ss.ff)));
			}
		}
		if(W[n-1].ss.ss != X) W.PB(ppi(0, pii(W[n-1].ss.ss, X)));
		
		sort(W.begin(), W.end());
		
		dt = t; tn = 0.0; run = R; walk = S;
		for(i = 0; i < SZ(W); i++) {
			dx = W[i].ss.ss - W[i].ss.ff;
			if(dx / ((double)W[i].ff + run) > dt + EPS) {
				ddx = ((double)W[i].ff + run) * dt;
				tn += dt; dt = 0.0; dx -= ddx;
				tn += dx / ((double)W[i].ff + walk);
			}
			else {
				tp = dx / ((double)W[i].ff + run);
				tn += tp; dt -= tp;
			}
		}
		
		printf("Case #%d: %.9lf\n", cs++, tn + EPS);
	}
	return 0;
}
