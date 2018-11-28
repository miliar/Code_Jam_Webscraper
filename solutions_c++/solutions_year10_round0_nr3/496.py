#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <functional>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
#include <queue>
#include <stack>
#include <cstdarg>

using namespace std;

#define TASKNAME "a"
#define pb push_back
#define mp make_pair
#define first fi
#define second se
#define forn(i, n) for (int i=0; i<(int)n; i++)
#define all(a) a.begin(), a.end()

typedef long double ldb;
typedef long long lld;
typedef unsigned long long uld;
typedef vector<int> vi;
typedef complex<double> cd;

double const eps=1e-9;
ldb const epsl=1e-9;
int const inf=0x3fffffff;
int const infu=0x7fffffff;
lld const infl=0x3fffffffffffffffLL;
uld const inful=0x7fffffffffffffffLL;
template <class T>
inline T sqr(const T &a) {
	return a*a;
}

int const N=1010;

lld g[N], t[N], sm[N], rs[N];


int main () {
	freopen (TASKNAME".in", "r", stdin);
	freopen (TASKNAME".out", "w", stdout);

	int nt;
	cin >> nt;

	for (int it=1; it<=nt; it++) {
		memset(t, 0, sizeof t);
		memset(g, 0, sizeof g);
		memset(sm, 0, sizeof sm);
		memset(rs, 0, sizeof rs);
		lld r, k, n;
		cin >> r >> k >> n;
		for (int i=1; i<=n; i++) {
			cin >> g[i];
			sm[i]=sm[i-1]+g[i];
		}
		k=min(k, sm[n]);
		lld res=0;
		int cr=1, T=0;
		for (int i=0; i<r;) {
			T++;
			if (t[cr] && (r-i)>(T-t[cr])) {
				int q=(r-i)/(T-t[cr]);
				res+=q*(res-rs[cr]);
				i+=q*(T-t[cr]);
			} 
			else {
				t[cr]=T;
				rs[cr]=res;

				int ne=cr;
				lld s=0;
				for (ne=cr; s+g[ne]<=k; s+=g[ne], ne=(ne+1 <= n ? ne+1 : 1));
				res+=s;
				cr=ne;
				i++;
			}
		}
		cout << "Case #" << it << ": " << res << endl;
	}

	return 0;
}