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

struct tree {
	tdbl w;
	string ft;
	vector<tree> ch;
};

tdbl cutes(tree& t, set<string> an) {
	tree* p = &t;
	tdbl res = p->w;
	while(p->ch.size() != 0) {
		p = &(p->ch[!esta(p->ft, an)]);
		res *= p->w;
	}
	return res;
}

void leearbol(tree& res) {
	char c; cin >> c; // (
	assert(c == '(');
	cin >> res.w;
	res.ch.clear();
	cin >> c;
	res.ft = c;
	if (c == ')') {
		return;
	}
	c = cin.peek();
	if ('a' <= c && c <= 'z') { string s; cin >> s; res.ft += s; }
	res.ch.push_back(tree());
	res.ch.push_back(tree());
	leearbol(res.ch[0]);
	leearbol(res.ch[1]);
	cin >> c; // )
	assert(c == ')');
}

int main() {
//	freopen("tree.in", "r", stdin);

	int tt;
	cin >> tt;

	forn(t, tt) {
		printf("Case #%d:\n", t+1);
		int l; cin >> l; /* dato al pedo si los hay */
		tree tr; leearbol(tr);
		int m; cin >> m;
		forn(i, m) {
			string fruta; cin >> fruta;
			int n; cin >> n;
			set<string> an;
			forn(j, n) {
				cin >> fruta; an.insert(fruta);
			}
			tdbl cuteness = cutes(tr, an);
			printf("%.8lf\n", (double)cuteness);
		}
	}
	return 0;
}
