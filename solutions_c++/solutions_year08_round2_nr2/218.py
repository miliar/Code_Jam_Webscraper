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

#define MAXN (1 << 10)

int a[MAXN];
int v[MAXN];

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int tests;
	scanf("%d", &tests);
	for (int test = 0; test < tests; test++) {
		int x1, x2, p;
		scanf("%d %d %d", &x1, &x2, &p);
		int ans = 0;
		memset(a, 0, sizeof(a));
		for (int i = 2; i < MAXN; i++) {
			if (!a[i]) {
				a[i] = 2;
				for (int j = 2 * i; j < MAXN; j += i) {
					a[j] = 1;
				}
			}
		}
		memset(v, 0, sizeof(v));
		for (int i = p; i < MAXN; i++) {
			if (a[i] != 2) {
				continue;
			}
			int found = 0;
			bool merged = false;
			for (int j = x1; j <= x2; j++) {
				if (!(j % i == 0)) {
					continue;
				}
				if (!v[j]) {
					v[j] = 1;
					found = 1;
				} else {
					merged = true;
				}
			}
			if (!merged) {
				ans += found;
			}
		}
		for (int j = x1; j <= x2; j++) {
			if (!v[j]) {
				ans++;
			}
		}
		printf("Case #%d: %d", test + 1, ans);
		printf("\n");
	}

	return 0;
}
