/* feliz cumpleaños sabi ! =P */
#include <vector>
#include <queue>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>

using namespace std;

/* tipos */
typedef pair<int,int> pint;
typedef long long tint;
typedef unsigned int mint;
typedef unsigned long long mtint;

typedef vector<int> vint;
typedef vector<vint> vvint;

typedef long double tipo;

/* "funciones" */
#define forn(i,n) for(int ___n=n, i=0;i<___n;++i)
#define dforn(i,n) for(int i=(n)-1;i>=0;--i)
#define forsn(i,s,n) for(int ___n=n, i=s;i<___n;++i)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define dforall(it,X) for(typeof((X).rbegin()) it = (X).rbegin(); it != (X).rend(); ++it)
#define all(X) (X).begin(), (X).end()
#define esta(e, c) (c.find(e) != c.end())
#define DBG(a) cerr << #a << " = " << a << endl;

template<class T> string itos(const T&x) { ostringstream o; o<<x; return o.str(); }

int mat[64][64];

typedef long double tdbl;

struct pto {
	tdbl x, y;
};

tdbl dist(pto a, pto b) {
	return hypot(b.x-a.x, b.y-a.y);
}

long double radi2(pto a, tdbl ra, pto b, tdbl rb) {
	return (ra + rb + dist(a, b)) / 2.0;
}

tdbl rs[64];
pto p[64];

tdbl iradi2(int i, int j) { return radi2(p[i], rs[i], p[j], rs[j]); }

tdbl solve(int n) {
	if (n == 1) return rs[0];
	if (n == 2) return max(rs[0], rs[1]);
	
	return min(
		max(iradi2(0, 1), rs[2]),
	min(
		max(iradi2(1, 2), rs[0]),
		max(iradi2(2, 0), rs[1])
	));
}

int main() {
	int tt;
	cin >> tt;

	forn(t, tt) {
		int n;
		cin >> n;
		
		forn(i, n) cin >> p[i].x >> p[i].y >> rs[i];
		tdbl res = solve(n);
		printf("Case #%d: %.6lf\n", t+1, (double)res);
	}
	return 0;
}
