#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <functional>
#include <string>
#include <map>
#define MAX 10005

using namespace std;

//	Pairs
#define MP make_pair
#define F first
#define S second
typedef pair<int, int> ii;

// Vectors
#define PB push_back
typedef vector<int> vi;
typedef vector<vi> vvi;

map< pair<int, int>, bool > dp;

int n, d, p[MAX], l[MAX];
bool debug = false;

bool dp_mem(int x, int y) {
	if (debug) printf("in %d %d\n", x, y);

	int k;
	if ( y < 0 ) return false;
	if (y > l[x]) return false;

	if (dp.find( MP(x, y) ) != dp.end() ) return dp[ MP(x, y) ];

	if (x == 1) {
		dp[ MP(1, y) ] = p[1] >= y;
	} else {
		bool tmp = false;

		for (k=1; k<x; k++) {
			int m = p[x] - p[x-k];
			tmp |= (m >= y) && dp_mem(x-k, m);
		}
		dp[ MP(x, y) ] = tmp;
	}

	if (debug) printf("returning %d\n", dp[ MP(x,y ) ]);
	return dp[ MP(x, y) ];

}

int main() {
	//freopen("a.in", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempto.out2", "w", stdout);
	int tst, i, t;
	scanf("%d", &tst);
	for (t=1; t<=tst; t++) {
		//if (t == 6) debug = true;
		dp.clear();

		scanf("%d", &n);
		for (i=1; i<=n; i++) scanf("%d%d", &p[i], &l[i]);
		scanf("%d\n", &d);

		bool sol = false;
		for (int j = 1; j <= n; j++) sol |= dp_mem(j, d - p[j]);

		printf("Case #%d: %s\n", t, sol ? "YES" : "NO");
		debug = false;
	}
	return 0;
}

