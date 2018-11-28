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

int _cl[128*128]; //empieza con todos en -1
tint cl(tint i) { return (_cl[i] == -1 ? i : _cl[i] = cl(_cl[i])); }
void join(tint i, tint j) { if(cl(i)!=cl(j)) _cl[cl(i)] = cl(j); }

int mp[128][128];
#define enrango(i, j) ((i) < f && (i) >= 0 && (j) < c && (j) >= 0)
#define ptocord(i, j) ((i)*128+(j))

int ddi[5] = {0, -1,  0, 0, 1};
int ddj[5] = {0,  0, -1, 1, 0};

int main() {
	int tt;
	cin >> tt;

	forn(t, tt) {
		memset(_cl, 0xff, sizeof(_cl));
		int f, c; cin >> f >> c;
		forn(i, f) forn(j, c) cin >> mp[i][j];
		forn(i, f) forn(j, c) {
			int md = 0;
			forn(d, 5) {
				int ii = i+ddi[d]; int jj = j+ddj[d];
				if (enrango(ii, jj) && mp[ii][jj] < mp[i+ddi[md]][j+ddj[md]]) md = d;
			}
			if (md) join(ptocord(i, j), ptocord(i+ddi[md], j+ddj[md]));
		}
		cout << "Case #" << t+1 << ":" << endl;
		map<int, char> mcl;
		char cur = 'a';
		forn(i, f) forn(j, c) {
			if (!mcl[cl(ptocord(i, j))]) mcl[cl(ptocord(i, j))] = cur++;
			cout << mcl[cl(ptocord(i, j))] << (j==c-1?"\n":" ");
		}
	}
	return 0;
}
