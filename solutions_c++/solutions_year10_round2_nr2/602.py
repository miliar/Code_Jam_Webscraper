/*
TASK: 
ID: marijon1
LANG: C++
*/

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <complex>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
#define mp make_pair
#define st first
#define nd second
#define FOR(i,n) for(int i=0;i<(n);i++)
#define FORO(i,n) for(int i=1;i<=(n);i++)
#define FORS(i,a,n) for(int i=(a);i<(n);i++)
#define FORB(i,a,n) for(int i=(a);i>=(n);i--)
#define foreach(v, i) for (typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define INRANGE(a,b,c,d) ((a)>=0&&(b)>=0&&(a)<(c)&&(b)<(d))
#define sz(v) ((int)(v).size())
#define pf printf

using namespace std;
typedef long long ll;

int go() {
	int n, k, b, t, pos[50], sp[50], ncr[50];
	bool reaches[50], cr[50];
	cin >> n >> k >> b >> t;
	FOR(i, n) cin >> pos[i];
	FOR(i, n) cin >> sp[i];
	bool sr = true;
	int nr = 0;
	int swp = 0;
	FORB(i, n-1, 0) {
		cr[i] = (pos[i] + sp[i] * t) >= b;
		sr = sr && cr[i];
		//pf("prer[%d] = %d\n", i, sr);
		reaches[i] = sr;
		ncr[i] = 0;
		if (sr) nr++;
	}
	bool impos = false;
	while (nr < k) {
		int dw = -1;
		FORB(j, n-1, 0)
			if (!reaches[j] && cr[j]) {
				dw = j;
				break;
			}
		//pf("dw=%d\n", dw);
		if (dw == -1) { impos = true; break; }
		reaches[dw] = true;
		nr++;
		for (int j = dw+1; j < n; j++)
			if (!reaches[j])
				ncr[dw]++;
			else {
				ncr[dw] += ncr[j];
				break;
			}
		swp += ncr[dw];
	}
	if (impos) {
		int maxr = 0;
		FOR(i, n)
			if ((pos[i] + sp[i] * t) >= b)
				maxr++;
		//pf("maxr=%d k=%d\n", maxr, k);
		assert(maxr < k);
		return -1;
	}
	return swp;
}

int main() {
	//freopen("xxxxx.in", "r", stdin);
	//freopen("xxxxx.out", "w", stdout);
	int t;
	cin >> t;
	FOR(i, t) {
		int x = go();
		if (x >= 0)
			pf("Case #%d: %d\n", i+1, x);
		else
			pf("Case #%d: IMPOSSIBLE\n", i+1);
	}
	return 0;
}
