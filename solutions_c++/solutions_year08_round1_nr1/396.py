#include <vector>
#include <map>
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
#define forsn(i,s,n) for(int ___n=n, i=s;i<___n;++i)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define all(X) (X).begin(), (X).end()

template<class T> string itos(const T&x) { ostringstream o; o<<x; return o.str(); }


int main() {
//	freopen("a.in", "r", stdin);
	int T;
	cin >> T;
	forn(tt, T) {
		int n; cin >> n;
		vint a(n), b(n);
		forn(i, n) cin >> a[i];
		forn(i, n) cin >> b[i];
		tint res = 0;
		sort(all(a));
		sort(all(b));
		forn(i, n) res += (tint)a[i] * b[n-i-1];

		cout << "Case #" <<  tt+1 << ": " << res << endl;
//		printf("Case #%d: %ld\n", tt+1, res);
	}

	return 0;
}
