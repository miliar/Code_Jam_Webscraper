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
#include <cstring>

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

string wrd[5050];
char mp[256][15];

struct trie;
struct trie {
	map<string, trie> v;
};

void insert(trie& t, char* p) {
	p++;
	int n = strlen(p); p[n-1] = 0;
//	DBG(p);
	trie* tt = &t;
	for(char*q = p; *q; ) {
		char* r = q;
		for(; *q && *q != '/'; q++);
		if (*q=='/') { *q = 0; q++; }
//		DBG(r);
		tt = &(tt->v[r]);
	}
}

int count(const trie& t) {
	int res = 1;
	forall(it, t.v) { res += count(it->second); }
	return res;
}

#define MAXS 101000
char s[MAXS];

int main() {
	int tt;
	cin >> tt;
	forn(t, tt) {
		int n, m; cin >> n >> m;
		fgets(s, MAXS, stdin);
		trie tr;
		forn(i, n) {
			fgets(s, MAXS, stdin);
			insert(tr, s);
		}
		int a = count(tr);
//		DBG(a)

		forn(i, m) {
			fgets(s, MAXS, stdin);
			insert(tr, s);
		}
		int b = count(tr);
//		DBG(b)

		int res = b-a;
		
		cout << "Case #" << (t+1) << ": " << res << endl;
	}
	return 0;
}

