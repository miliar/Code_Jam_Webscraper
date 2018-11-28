#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

/* tipos */
typedef pair<int,int> pint;
typedef long long tint;
typedef unsigned int mint;
typedef unsigned long long mtint;

typedef vector<int> vint;
typedef vector<vint> vvint;

/* "funciones" */
#define forn(i,n) for(int ___n=n, i=0;i<___n;++i)
#define forsn(i,s,n) for(int ___n=n, i=s;i<___n;++i)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)

template<class T> string itos(const T&x) { ostringstream o; o<<x; return o.str(); }
template<class T> inline int size(const T&c) { return c.size(); }

inline int bneed(unsigned long long x) { return x?64-__builtin_clzll(x):0; }
inline int lg2(unsigned long long x) { return x?63-__builtin_clzll(x):-1; }

#define strtostr(S, s) {istringstream s; s.str(S);}

#define strm(X) ""; forall(it, X) cerr << " " << (*it); cerr << endl

#define INF 10000

int main() {
	int n; cin >> n;
	string ss[128];
	string ln;

	forn(t, n) {
		int s, q;
		int cost[2][128];
		cin >> s; getline(cin, ln);
		forn(i, s) getline(cin, ss[i]);

		forn(i, s) cost[0][i] = cost[1][i] = 0;
		cin >> q; getline(cin, ln);
		while (q--) {
			getline(cin, ln);
			forn(i, s) {
				cost[q&1][i] = INF;
				if (ln!=ss[i]) {
					forn(j, s) cost[q&1][i] = min(cost[q&1][i], cost[!(q&1)][j]+ (i!=j));
				}
			}
//			forn(i, s) cerr << cost[q&1][i] << " "; cerr << endl;
		}

		int res = INF;
		forn(i, s) res = min(res, cost[0][i]);
		cout << "Case #" << t+1 << ": " << res << endl;
	}
	return 0;
}
