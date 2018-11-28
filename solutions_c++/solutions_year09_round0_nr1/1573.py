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
	int l, d, n;
	cin >> l >> d >> n;
	forn(i, d) cin >> wrd[i];
	forn(t, n) {
		string s; cin >> s;
//		DBG(s);
		memset(mp, 0, sizeof(mp));
		const char *p = s.c_str();
		forn(i, l) {
			if (*p == '(') { p++;
				while (*p != ')') mp[(int)*(p++)][i] = 1;
				p++;
			} else mp[(int)*(p++)][i] = 1;
		}
		int res = 0;
		forn(i, d) {
			bool ok = 1;
			forn(j, l) ok = ok && mp[(int)wrd[i][j]][j];
			res += ok;
		}
		cout << "Case #" << t+1 << ": " << res << endl;
	}
	return 0;
}
