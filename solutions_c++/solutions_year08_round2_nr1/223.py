#pragma comment(linker,"/STACK:256000000")

#ifdef __GNUC__
#define int64 long long
#else /* MSVC, say */
#define int64 __int64
#endif 

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <memory.h>
#include <ctype.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))

#define MAXN (1 << 7)

pair <int64, int64> a[MAXN];

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int tests;
	scanf("%d", &tests);
	for (int test = 0; test < tests; test++) {
		int64 n, A, B, C, D, x, y, M;
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x, &y, &M);
		for (int i = 0; i < n; i++) {
			a[i] = make_pair(x, y);
//			cout << x << " " << y << endl;
			x = (A * x + B) % M;
			y = (C * y + D) % M;
		}
		int ans = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < i; j++) {
				for (int k = 0; k < j; k++) {
					int64 cx = a[i].first + a[j].first + a[k].first;
					int64 cy = a[i].second + a[j].second + a[k].second;
					if ((cx % 3 == 0) && (cy % 3 == 0)) {
						ans++;
					}
				}
			}
		}
		printf("Case #%d: %d", test + 1, ans);
		printf("\n");
	}

	return 0;
}
