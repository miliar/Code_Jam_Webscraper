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
#include <cmath>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a):(-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))

#define pii pair < int, int >
#define MP make_pair
#define X first
#define Y second 

#define N 5011

int ind[N];
int a[N];
vector < int > b;

//int ans[N][N], used[N];

int main () {
	int i, j, T, n, k;

	scanf("%d", &T);
//	mset(used, 0);
	
	for (int cas = 1; cas <= T; cas++) {

		scanf("%d%d", &k, &n);

		for (i = 0; i < n; i++) scanf("%d", &ind[i]);

		//if (!used[k]) {

		mset(a, 0);
		b.clear();

		int cnt = 1, c = 0;

		for (i = 1; i <= k; i++) b.PB( i );

		i = 0, c = 1;
		while (cnt <= k) {
			//if (cnt == c) {
				a[ b[i] ] = cnt;
				b.erase( b.begin() + i );
				cnt++;
				//c = 1;
				if (!b.SZ) break;
				i = (i + cnt - 1) % ((int)b.SZ);

			//}
			//if (!b.SZ) break;
			//i = (i+1) % ( (int)b.SZ );
			//c++;
		}

		//memcpy(ans[k], a, sizeof(a));
		//used[k] = true;

		//}

		printf("Case #%d:", cas);

		for (i = 0; i < n; i++) printf(" %d", a[ ind[i] ]);
		printf("\n");
	}

	return 0;
}
