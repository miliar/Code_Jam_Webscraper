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

const int INF = 1<<28;
#define MAXM 10004

int m,v;
int g[MAXM],c[MAXM],l[MAXM];

int op(int x, int op, int y) {
	return op == 1 ? x && y : x || y;
}

int memo[MAXM][2];
int go(int node, int val) {
	int& res = memo[node][val];
	if (res != -1) return res;

	if (node > (m-1)/2) {
		if(l[node] == val) return res = 0;
		else return res = INF;
	}

	res = INF;
	forn(x1,2) forn(x2,2) if (op(x1,g[node],x2) == val) res <?= go(2*node,x1) + go(2*node+1,x2);

	if (c[node]) {
		forn(x1,2) forn(x2,2) if (op(x1,1-g[node],x2) == val) res <?= 1 + go(2*node,x1) + go(2*node+1,x2);
	}

	return res;
}



void init() {
	ids.clear();
	memset(memo,-1,sizeof memo);
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int _t; cin >> _t;
	forsn(cas,1,_t+1) {
		init();
		cin >> m >> v;
		forsn(i,1,m+1)
			if (i <= (m-1) / 2) {
				cin >> g[i] >> c[i];
			}
			else {
				cin >> l[i];
			}

		cout << "Case #" << cas << ": ";
		int res = go(1,v);
		if (res == INF) cout << "IMPOSSIBLE\n";
		else cout << res << endl;

	}
	return 0;
}

