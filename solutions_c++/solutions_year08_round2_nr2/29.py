#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
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
#define D(a) cout << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;

#define MAXN 1000010


map<string, map<string, int> > ids;
int id(string cat, string s) {
	map<string,int>& m = ids[cat];
	if (m.count(s) == 0) m[s] = si(m)-1;
	return m[s];
}


tint pre[MAXN];

void init(tint n) {
	forn(i,n) pre[i] = i;
}

tint comp(tint x) {
	return pre[x] = pre[x] == x ? x : comp(pre[x]);
}

void merge(tint a, tint b) {
	pre[b] = a;
}

void init() {
	ids.clear();
}

bool criba[MAXN];
vi primos;

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);


	forn(i,MAXN) criba[i] = true;
	criba[0] = criba[1] = false;
	forn(i,MAXN) if (criba[i]) {
		primos.pb(i);
		for (tint j = 2*i; j < MAXN; j += i) criba[j] = false;
	}

	int _t; cin >> _t;
	forsn(cas,1,_t+1) {
		init();
		tint a,b,P; cin >> a >> b >> P;
		init(b - a + 1);
		forall(it,primos) if (*it >= P) {
			tint p = *it;
			tint i0 = p * ((a + (p-1)) / p);
			for (tint i = i0; i <= b - p; i += p) merge(comp(i-a),comp(i+p-a));
		}

		tint res = 0;
		forn(i,b-a+1) if (pre[i] == i) res++;
		cout << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}

