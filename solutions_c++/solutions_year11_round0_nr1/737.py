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

string wrd[5050];
char mp[256][15];

int main() {
	int tt;
	cin >> tt;
	forn(t, tt) {
		int res;
		int n; cin >> n;
		res = 0;
		int p[2], tm[2];
		p[0] = p[1] = 1; tm[0]=tm[1] = 0;
		forn(i, n) {
			char ch; int v, c; cin >> ch >> v;
			c = ch == 'O';
			tm[c] += abs(v-p[c]);
			p[c] = v;
			if (tm[c] < tm[!c]) tm[c] = tm[!c];
			tm[c]++; // push
		}
		res = max(tm[0],tm[1]);
		cout << "Case #" << t+1 << ": " << res << endl;
	}
	return 0;
}

