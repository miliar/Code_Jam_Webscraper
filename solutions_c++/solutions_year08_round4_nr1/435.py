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

#define MAXN (10010)
#define INF (1 << 29)


int g[MAXN];
int c[MAXN];
int v[MAXN];
int n;

int mem[MAXN][2];

int firstleaf;

int left(int k) {
	return 2 * k + 1;
}

int right(int k) {
	return 2 * k + 2;
}

int f(int a, int b, int g) {
	if (g) {
		return a & b;
	} else {
		return a | b;
	}
}

int get(int k, int val) {
	int & ret = mem[k][val];
	if (ret != -1) {
		return ret;
	}
	if (left(k) >= n) {
		if (v[k] == val) {
			ret = 0;
		} else {
			ret = INF;
		}
		return ret;
	}
	ret = INF;
	
	for (int i1 = 0; i1 < 2; i1++) {
		for (int i2 = 0; i2 < 2; i2++) {
			int c1 = get(left(k), i1);
			int c2 = get(right(k), i2);
			if (f(i1, i2, g[k]) == val) {
				ret = MIN(ret, c1 + c2);
			} else if (c[k] && (f(i1, i2, 1 - g[k]) == val)) {
				ret = MIN(ret, c1 + c2 + 1);
			}
		}
	}

	return ret;
}

int main() {
	freopen("aa.in", "r", stdin);
	freopen("aa.out", "w", stdout);

	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		int target;
		scanf("%d %d", &n, &target);
		
		for (int i = 0; i < (n - 1) / 2; i++) {
			scanf("%d %d", &g[i], &c[i]);
		}
	
		firstleaf = (n - 1) / 2;
		memset(v, -1, sizeof(v));
		for (int i = 0; i < (n + 1) / 2; i++) {
			scanf("%d", &v[firstleaf + i]);
		}

		printf("Case #%d: ", test);
		memset(mem, -1, sizeof(mem));
		int ans = get(0, target);
		if (ans >= INF) {
			printf("IMPOSSIBLE");
		} else {
			printf("%d", ans);
		}
		printf("\n");
	}

	return 0;
}
