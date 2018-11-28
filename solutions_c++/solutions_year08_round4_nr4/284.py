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

#define N 50111

char a[N], b[N];
int k;

int main () {
	int i, j, n, T;

	scanf("%d", &T);
	
	for (int cas = 1; cas <= T; cas++) {

		scanf("%d%s", &k, &a);

		n = strlen(a);

		int p[] = {0,1,2,3,4};
		int res = N;

		do {
			for (i = 0, j = 0; i < n; i++, j += k) b[ i ] = a[ (i/k)*k + p[i%k] ];
			int cnt = 1;
			for (i = 1; i < n; i++) if (b[i] != b[i-1]) cnt++;
			res = min(res, cnt);
		} while (next_permutation(p, p+k));

		printf("Case #%d: %d\n", cas, res);

		cerr << cas << "\n";
	}

	return 0;
}

