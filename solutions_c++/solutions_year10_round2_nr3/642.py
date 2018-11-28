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

#define MODU 100003

tint res[30];

int id[30];

void init() {
	
	forn(x, 1 << 24) {
		int msk = 0;
		int li = -1;
		int cnt = 0;
		bool bl = false;
		forn(i, 24) if ((x >> i) & 1) { cnt++;
			li = i+2;
			if (cnt == 1) {
				msk |= 1 << i;
				li = i+2;
				id[li] = cnt;
			} else {
				li = i+2;
				int j = cnt-2;
				if ((msk >> j) & 1) msk |= 1 << i;
			}
		}
		if (li >=0 && ((msk >> (li-2))&1)) res[li] = (res[li]+1)%MODU;
	}
	return;
}


int main() {
	
	init();
	
	int tt;
	cin >> tt;
	forn(t, tt) {
		int n;
		cin >> n;
		
		cout << "Case #" << (t+1) << ": " << res[n] << endl;
	}
	return 0;
}

