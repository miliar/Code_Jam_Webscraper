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

int R, K, N;
int GS[1000];
ll AddPts[1000], EndsIn[1000];

void incmod(int &t) {
	t++;
	if (t >= N) t = 0;
}

ll go() {
	fill(AddPts, AddPts + 1000, -1);
	fill(EndsIn, EndsIn + 1000, -1);
	int i = 0, j = 0, c = 0;
	ll ans = 0;
	FOR(r, R) {
		if (AddPts[i] != -1) {
			ans += AddPts[i], j = i = EndsIn[i];
			continue;
		}
		while (true) {
			if ((c && i==j) || (c + GS[j] > K))
				break;
			c += GS[j];
			incmod(j);
		}
		ans += c;
		AddPts[i] = c;
		EndsIn[i] = j;
		//pf("ans=%d i=%d j=%d r=%d c=%d\n", ans, i, j, r, c);
		i = j;
		c = 0;
	}
	return ans;
}

int main() {
	//freopen("xxxxx.in", "r", stdin);
	//freopen("xxxxx.out", "w", stdout);
	int T;
	scanf(" %d", &T);
	FOR(t, T) {
		scanf(" %d %d %d", &R, &K, &N);
		FOR(i, N)
			scanf(" %d", &GS[i]);
		fprintf(stderr, "Case %d\n", t);
		//pf("R=%d K=%d N=%d\n", R, K, N);
		pf("Case #%d: %lld\n", t+1, go());
	}
	return 0;
}
