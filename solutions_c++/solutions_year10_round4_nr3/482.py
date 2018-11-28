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

char B1[200][200], B2[200][200];

int xcase() {
	int r;
	cin >> r;
	fill(B1[0], B1[200], 0);
	FOR(i, r) {
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		x1--; y1--; x2--; y2--;
		FORS(r, y1, y2+1)
			FORS(c, x1, x2+1)
				B1[r][c] = 1;
	}
	char (*b1)[200] = B1, (*b2)[200] = B2;
	int tt = 0;
	while (true) {
		/*FOR(r, 20) {
			FOR(c, 20) pf("%2d", b1[r][c]);
			pf("\n");
		}
		pf("\n");*/
		copy(b1[0], b1[100], b2[0]);
		int still = false;
		FOR(r, 100) FOR(c, 100) {
			if (r > 0 && c > 0 && b1[r-1][c] && b1[r][c-1])
				b2[r][c] = 1;
			else if ((r == 0 || b1[r-1][c]==0) && (c == 0 || b1[r][c-1]==0))
				b2[r][c] = 0;
			if (b2[r][c]) still=true;
		}
		swap(b1, b2);
		tt++;
		if (!still) break;
	}
	return tt;
}

int main() {
	//freopen("xxxxx.in", "r", stdin);
	//freopen("xxxxx.out", "w", stdout);
	int c;
	cin >> c;
	FOR(i, c) {
		pf("Case #%d: %d\n", i+1, xcase());
	}
	return 0;
}
