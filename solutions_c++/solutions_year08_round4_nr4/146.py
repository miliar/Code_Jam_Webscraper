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
#define dforn(i,n) for(int i=(n)-1;i>=0;--i)
#define forsn(i,s,n) for(int ___n=n, i=s;i<___n;++i)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define dforall(it,X) for(typeof((X).rbegin()) it = (X).rbegin(); it != (X).rend(); ++it)
#define all(X) (X).begin(), (X).end()
#define esta(e, c) (c.find(e) != c.end())
#define DBG(a) cerr << #a << " = " << a << endl;

template<class T> string itos(const T&x) { ostringstream o; o<<x; return o.str(); }

int kp[20];

int main() {
	int T;
	cin >> T;
	forn(tt, T) {
		int k; cin >> k;
		string s; cin >> s;
		int m = s.length(); int x = m / k;
		char r[50002];
		forn(i, k) kp[i] = i;
		int mej = m+1;
		do {
			char lc = 0, ch; int cur = 0;
			forn(i, x) {
				forn(j, k) {
					ch = r[j+i*k] = s[kp[j]+i*k];
					if (ch != lc) {cur++; lc = ch;}
				}
			}
			mej = min(mej, cur);
		} while (next_permutation(kp, kp+k));
		cout << "Case #" <<  tt+1 << ": " << mej << endl;
		//		printf("Case #%d: %ld\n", tt+1, res);
	}

	return 0;
}
