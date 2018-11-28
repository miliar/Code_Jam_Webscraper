//#pragma comment(linker, "/STACK:100000000)

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <time.h>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a):(-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))
#define UNIQUE(p) sort(ALL(p)), p.resize( (int)(unique(ALL(p)) - p.begin()) )

#define pii pair < int, int >
#define MP make_pair
#define X first
#define Y second

//////////////////////////////// STUFF ////////////////////////////////

#define INF 1000000000

#define N 10111
#define M 11

char name[M][100];
pii a[M];
int ind[M], n;

int used[N];

map < string, int > dict;

inline int cntbits(int x)  {
	int res = 0;
	while (x) {
		x -= (x & -x);
		res++;
	}
	return res;
}

int main () {
	int i, j, CAS;

	scanf("%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {

		scanf("%d", &n);
		dict.clear();

		for (i = 0; i < n; i++) {
			scanf("%s%d%d", name[i], &a[i].X, &a[i].Y);
			if (dict.find( name[i] ) == dict.end()) {
				int t = dict.SZ;
				dict[ name[i] ] = t;
			}
			ind[ i ] = dict[ name[i] ];
		}

		int res = INF;

		for (int m = 1; m < (1<<n); m++) {
			mset(used,-1);
			int c = 0;
			for (i = 0; i < n; i++) if ( m & (1<<i) ) {
				for (j = a[i].X; j <= a[i].Y; j++) used[j] = ind[i];
			}
			int tm = 0;
			for (i = 1; i <= 10000; i++) {
				if (used[i] == -1) break;
				tm |= (1<<used[i]);
			}
			if (i <= 10000) continue;
			if (cntbits(tm) <= 3) res = min(res, cntbits(m));
		}

		if (res == INF) printf("Case #%d: IMPOSSIBLE\n", cas);
		else printf("Case #%d: %d\n", cas, res);
		cerr << cas << "\n";
	}

	cerr << "clock(): " << clock() << "\n";

	return 0;
}


