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

#define INF 10000000

#define blk 0x3f3f3f3f

struct brd {
	int m[128][128];
	int sts, rem, mi, mj, mpf;
	int mej, cur;

	void go(int i, int j) {
//		cerr << i << " " << j << endl;
		if (j > mj) { go(i+1, 1); return; }
		if (i > mi) {
//			cerr << mej << " " << cur << endl;
			mej = max(cur, mej);
			return;
		} else {
			int rem = (mi-i)*((mj+1)/2) + ((mj-j+1)+1)/2;
			if (rem + cur  <= mej) return;
			if (m[i][j] == 0) { // Libre
				cur++;
				m[i+1][j-1]++;
				m[i+1][j+1]++;
				m[i+0][j+1]++;
				go(i, j+2);
				m[i+1][j-1]--;
				m[i+1][j+1]--;
				m[i+0][j+1]--;
				cur--;
			}
			go(i, j+1);
		}
	}

	brd() {
		memset(m, 0x3f, sizeof(m));
		sts = mej = cur = 0;
	}
};

int main() {
	int T;
	cin >> T;
	forn(tt, T) {
		brd b;
		cin >> b.mi >> b.mj;
		forn(i, b.mi) {
			string s; cin >> s;
			forn(j, b.mj) {
				b.m[i+1][j+1] = (s[j]=='x')?blk:(b.sts++,0);
			}
		}
		b.rem = b.sts;
		b.mpf = (b.mj+1)/2;
		b.go(1, 1);
		int res = b.mej;
		cout << "Case #" <<  tt+1 << ": " << res << endl;
//		printf("Case #%d: %ld\n", tt+1, res);
	}

	return 0;
}
