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
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cout << #a << "=" << a << endl;
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

map<string, map<string, int> > ids;
int id(string cat, string s) {
	map<string,int>& m = ids[cat];
	if (m.count(s) == 0) m[s] = si(m)-1;
	return m[s];
}

tint a,n,m;

bool sol(tint x1, tint x2, tint y1, tint y2) {
	if (abs(x1*y2 - x2 * y1) != a) return false;

	tint x = min(0LL,min(x1,x2)), y = min(0LL,min(y1,y2)), x0 = 0, y0 = 0;
	x0 -= x; x1 -= x; x2 -= x;
	y0 -= y; y1 -= y; y2 -= y;

	bool res = true;
	if (max(x0,max(x1,x2)) > n || max(y0,max(y1,y2)) > m) res = false;
	if (res) cout << x0 << ' ' << y0 << ' ' << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << endl;
	return res;

}


void init() {
	ids.clear();
}


int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int _t; cin >> _t;
	forsn(cas,1,_t+1) {
		init();
		cout << "Case #" << cas << ": ";

		cin >> n >> m >> a;
		forsn(x2,-n,n+1) forsn(x1,-n,n+1)
		forsn(y2,-m,m+1) forsn(y1,-m,m+1)
			if (sol(x1,x2,y1,y2)) goto next;


		cout << "IMPOSSIBLE\n";
		next:;
	}



	return 0;
}

