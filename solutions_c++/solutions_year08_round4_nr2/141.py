#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>

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

int ok[10002*10002+100];

int n, m, A;
int X1, Y1, X2, Y2;
int ln = -1;
bool calc() {
	forsn(a, ln+1, n+1) {
		forn(d, 10001) { //m
			int v = a*d;
			if (ok[v] == -1 || ok[v] > d) ok[v] = d;
		}
	}
	ln = n;
	cerr << "ok " << n << endl;
	forn(b, m+1) forn(c, n+1) {
		int w = A+b*c;
		if (w > n*m) break;
		if (ok[w] == -1 || ok[w] > m) continue;
		if (w == 0) {
			X1 = 0; Y1 = b; X2 = c; Y2 = 0;
			return true;
		}
		int d = ok[w];
		int a = w/d;
		X1 = a; Y1 = b; X2 = c; Y2 = d;
		return true;
	}
	return false;
}

struct tcase {
	int tt, n, m, A;
	int X1, Y1, X2, Y2;
	bool res;
};

bool cmpn(const tcase& a, const tcase& b) {
	if (a.n != b.n) return a.n < b.n;
	return a.m < b.m;
}
bool cmptt(const tcase& a, const tcase& b) {
	return a.tt < b.tt;
}


tcase tc[1024];

int main() {
	memset(ok, 0xFF, sizeof(ok));
	ln = -1;

	int T;
	cin >> T;
	forn(tt, T) {
		cin >> tc[tt].n >> tc[tt].m >> tc[tt].A; tc[tt].tt = tt;
	}
	sort(tc, tc+T, cmpn);
	forn(tt, T) {
		A = tc[tt].A;
		n = tc[tt].n;
		m = tc[tt].m;
		tc[tt].res = calc();
		tc[tt].X1 = X1;
		tc[tt].Y1 = Y1;
		tc[tt].X2 = X2;
		tc[tt].Y2 = Y2;
	}
	sort(tc, tc+T, cmptt);
	forn(tt, T) {
		if (tc[tt].res) {
			cout << "Case #" <<  tt+1 << ": 0 0 " << tc[tt].X1 << " " << tc[tt].Y1 << " " << tc[tt].X2 << " " << tc[tt].Y2 << endl;
			if (tc[tt].X1*tc[tt].Y2 - tc[tt].X2*tc[tt].Y1 != tc[tt].A) { cerr << "WRONG " << tc[tt].X1*tc[tt].Y2 - tc[tt].X2*tc[tt].Y1 - tc[tt].A << endl; return 0;}
		} else {
			cout << "Case #" <<  tt+1 << ": " << "IMPOSSIBLE" << endl;
		}
//		printf("Case #%d: %ld\n", tt+1, res);
	}

	return 0;
}
