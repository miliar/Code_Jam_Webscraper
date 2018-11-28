#include <vector>
#include <queue>
#include <map>
#include <list>
#include <queue>
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

#define INF 0x3f3f3f3f

struct pto {
	short i,j;
	pto() : i(0), j(0) {}
	pto(int ii, int jj) : i(ii), j(jj) {}
	bool operator<(const pto& o) const { if (i != o.i) return i < o.i; return j < o.j; }
};
	pto operator+(const pto&a, const pto&b) { return pto(a.i+b.i, a.j+b.j); }
	pto& operator+=(pto&a, const pto&b) { a.i += b.i; a.j += b.j; return a; }
	pto operator-(const pto&a, const pto&b) { return pto(a.i-b.i, a.j-b.j); }
	pto& operator-=(pto&a, const pto&b) { a.i -= b.i; a.j -= b.j; return a; }
	pto operator*(const pto&a, int b) { return pto(a.i*b, a.j*b); }
	pto operator*(int b, const pto&a) { return pto(a.i*b, a.j*b); }
	pto& operator*=(pto&a, int b) { a.i*=b; a.j*=b; return a; }
	pto operator/(const pto&a, int b) { return pto(a.i/b, a.j/b); }
	pto& operator/=(pto&a, int b) { a.i/=b; a.j/=b; return a; }
	pto operator!(const pto&a) { return pto(a.j, a.i); }

	int operator*(const pto&a, const pto&b) { return a.i*b.i+a.j*b.j; }
	int operator&(const pto&a, const pto&b) { return a.i*b.j-a.j*b.i; }

int mem[16*16+1][16*16+1][16*16];
int mp[16][16];
int mi, mj;
const int di[4] = {0, 1, 0, -1};
const int dj[4] = {1, 0, -1, 0};
int prt[4][16][16];

pto ivd(-1, -1);
int ptonum(const pto& p) {
	if(p.i==-1 || p.j==-1) return 16*16;
	return p.i*16 + p.j;
}
int ptonum(int i, int j) {
	if(i==-1 || j==-1) return 16*16;
	return i*16 + j;
}

struct state {
	short m, p, q;
	bool operator<(const state& o) { if (m != o.m) return m < o.m; if (p != o.p) return p < o.p; return q < o.q; }
};

#define enrango(i, j) ((0 <= (i)) && ((i) < mi) && (0 <= (j)) && ((j) < mj))

int main() {
	DBG(sizeof(mem)/1024);
	int T;
	cin >> T;
	forn(tt, T) {
		memset(mem, 0x3f, sizeof(mem));
		cin >> mi >> mj;
		pto me = ivd;
		pto ck = ivd;
		forn(i,  mi) {
			string s; cin >> s;
			forn(j, mj) {
				if (s[j] == 'O') { me = pto(i, j); s[j] = '.'; }
				if (s[j] == 'X') { ck = pto(i, j); s[j] = '.'; }
				mp[i][j] = s[j] == '#';
			}
		}
		forn(d, 4) {
			forn(i, mi) forn(j, mj) {
				int ii = i; int jj = j;
				do {
					prt[d][i][j] = ptonum(ii, jj);
					ii += di[d];
					jj += dj[d];
				} while(enrango(ii, jj) && mp[ii][jj] == 0);
			}
		}
		list<state> qu;
		state ini;
		ini.m = ptonum(me);
		ini.p = ini.q = ptonum(ivd);
#define trybk(st, dst) { if (mem[st.p][st.q][st.m] == INF) qu.push_back(st); if (mem[st.p][st.q][st.m] > dst) mem[st.p][st.q][st.m] = dst; }

		trybk(ini, 0);
		while (!qu.empty()) {
			state st = qu.front(); qu.pop_front();
			int mei = st.m/16;
			int mej = st.m%16;
			int dst = mem[st.p][st.q][st.m];
			forn(d, 4) forn(dp, 5) forn(dq, 5) {
				state ot(st);
				if (dp < 4) ot.p = prt[dp][mei][mej];
				if (dq < 4) ot.q = prt[dq][mei][mej];
				if (enrango(mei+di[d],mej+dj[d])&& mp[mei+di[d]][mej+dj[d]] == 0) {
					ot.m = ptonum(mei+di[d],mej+dj[d]);
					trybk(ot, dst+1);
				}
				if (st.m == ot.p && ot.q != 256 && ot.p != 256) {
					ot.m = ot.q;
					trybk(ot, dst+1);
				}
				if (st.m == ot.q && ot.p != 256 && ot.q != 256) {
					ot.m = ot.p;
					trybk(ot, dst+1);
				}
			}
		}
		int res = INF;
		int nck = ptonum(ck);
		forn(p, 257) forn(q, 257) {
			res = min(res, mem[p][q][nck]);
		}
		if (res >= INF) {
			cout << "Case #" <<  tt+1 << ": " << "THE CAKE IS A LIE" << endl;
		} else {
			cout << "Case #" <<  tt+1 << ": " << res << endl;
		}
//		printf("Case #%d: %ld\n", tt+1, res);
	}

	return 0;
}
