#include <iomanip>
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
#include <cstring>
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
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
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
typedef vector<pii> vpii;

int  n,m,t, ans;
vector<vector<string> > w, z;

void read(int cond) {
	string s, tmp;
	vector<string> v;
	cin >> s;
	int i=0;
	while(i<si(s)) {
		if (s[i] == '/') {
			i++;
			continue;
		} else {
			tmp+= s[i];
		}
		if ((i == si(s)-1) || (s[i+1] == '/')) {
			v.pb(tmp);
			tmp = "";
		}
		i++;
	}
	if (cond == 0) w.pb(v);
	else z.pb(v);
}

int comparten(vector<string> a, vector<string> b) {
	int i = 0;
	while(i<min(si(a),si(b)) && (a[i] == b[i])) i++;
	return i;
}

void init() {
	w.clear(), z.clear();
	ans = 0;
}

int main () {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	cin >> t;
	forn(rep,t) {
		init();
		cin >> n >> m;
		forn(i,n) read(0);
		forn(i,m) read(1);

		forn(i,si(z)) {
			int mx = 0;
			forn(j,si(w)) mx = max(mx,comparten(z[i],w[j]));
			vector<string> newv;
			forn(k,mx) newv.pb(z[i][k]);
			forsn(k,mx,si(z[i])) {
				newv.pb(z[i][k]);
				w.pb(newv);
				ans++;
			}
		}
		cout << "Case #" << rep+1 << ": " << ans << endl;
	}
	return 0;
}
