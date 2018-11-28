/*
USER: zobayer
TASK:
ALGO:
*/

//#pragma warning (disable: 4786)
//#pragma comment (linker, "/STACK:0x800000")
#define _CRT_SECURE_NO_WARNINGS 1

#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <utility>
using namespace std;

template< class T > T _abs(T n) { return (n < 0 ? -n : n); }
template< class T > T _max(T a, T b) { return (!(a < b) ? a : b); }
template< class T > T _min(T a, T b) { return (a < b ? a : b); }
template< class T > T sq(T x) { return x * x; }

#define MP(x, y) make_pair(x, y)
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define SZ(c) (int)c.size()
#define PB(x) push_back(x)
#define ff first
#define ss second
#define i64 long long
#define ld long double
#define pii pair< int, int >
#define psi pair< string, int >

const double EPS = 1e-9;
const int INF = 0x7f7f7f7f;

const int MAX = 10009;

int D[MAX], H[MAX];

int n;

map< pair< int, int >, bool > DP;
map< pair< int, int >, bool > :: iterator it;

bool solve(int p, int x) {
	if(p >= n) return true;
	it = DP.find(MP(p, x));
	if(it != DP.end()) return it->second;
	bool ret = false;
	for(int i = p + 1; i <= n; i++) {
		if(D[i] <= (x + D[p])) {
			ret |= solve(i, _min(H[i], D[i] - D[p]));
			if(ret == 1) break;
		}
		else break;
	}
	DP.insert(MP(MP(p,x), ret));
	return ret;
}

int main() {
	READ("A-small-attempt1.in");
	WRITE("A-small-attempt1.out");
	//READ("in.txt");
	int test, cs, i; bool ret;
	scanf("%d", &test);
	for(cs = 1; cs <= test; cs++) {
		scanf("%d", &n);
		for(i = 0; i < n; i++) {
			scanf("%d %d", &D[i], &H[i]);
		}
		scanf("%d", &D[i]);
		H[i] = INF;
		DP.clear();
		ret = solve(0, _min(D[0], H[0]));
		if(ret) printf("Case #%d: YES\n", cs);
		else printf("Case #%d: NO\n", cs);
	}
	return 0;
}