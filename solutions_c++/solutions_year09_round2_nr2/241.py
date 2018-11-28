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

typedef long double tdbl;

int main() {
//	freopen("tree.in", "r", stdin);

	int tt;
	cin >> tt;

	forn(t, tt) {
		string res, s; cin >> s;
		vint v;
		v.push_back(0);
		forn(i, s.size()) v.push_back(s[i]-'0');

//		forn(i, v.size()) cerr << v[i] << " "; cerr << endl;

		bool b = next_permutation(all(v));
		if (!b) cerr << "ERROR " << s << endl;

//		forn(i, v.size()) cerr << v[i] << " "; cerr << endl;

		int st = 0;
		while (st < (int)v.size() && !v[st]) st++;
		res = "";
		forsn(i, st, v.size()) res += '0' + v[i];
		printf("Case #%d: %s\n", t+1, res.c_str());
	}
	return 0;
}
