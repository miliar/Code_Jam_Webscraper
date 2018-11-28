#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
#include <cstring>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;

const int MAXN = 500 + 10;

struct cell {
	tint d, i, j;
	cell operator+(const cell& o) const { return (cell){d+o.d, i+o.i, j+o.j}; }
	cell operator-(const cell& o) const { return (cell){d-o.d, i-o.i, j-o.j}; }
};
ostream& operator<<(ostream& out, const cell& o) { out << '(' <<o.d << ',' << o.i << ',' << o.j << ')'; return out; }

tint m,n;
cell t[MAXN][MAXN], cum[MAXN][MAXN];

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int ncas; cin >> ncas;
    forn(cas,ncas) {    	
    	cout << "Case #" << cas+1 << ": ";
    	int _; cin >> m >> n >> _;
    	forn(i,m) forn(j,n) {
    		char c; cin >> c; int w = c-'0';
    		t[i][j] = (cell){w,i*w,j*w};
    	}

    	forn(i,m+2) cum[i][0] = (cell){0,0,0};
    	forn(j,n+2) cum[0][j] = (cell){0,0,0};
    	forn(i,m) forn(j,n)
    		cum[i+1][j+1] = t[i][j] + cum[i][j+1] + cum[i+1][j] - cum[i][j];

    	int res;
    	for (res = min(m,n); res >= 3; res--) {
    		forsn(c,res,m+1) forsn(d,res,n+1) {
    			cell s = cum[c][d] - cum[c-res][d] - cum[c][d-res] + cum[c-res][d-res];
    			s = s - t[c-1][d-1] - t[c-res][d-1] - t[c-1][d-res] - t[c-res][d-res];
    			tint ci = 2*c - res - 1, cj = 2*d - res - 1;
    			if (ci * s.d == 2*s.i && cj * s.d == 2*s.j) goto hell;
    		}
    	}
    	hell:;
    	if (res < 3) cout << "IMPOSSIBLE" << endl;
    	else cout << res << endl;



    }
}
