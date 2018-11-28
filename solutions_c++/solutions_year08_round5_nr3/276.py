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

#define MAXN 10

int mem[MAXN + 1][1 << MAXN];
int used[MAXN + 1];
int n, m;

int bitcnt(int k) {
	int ret = 0;
	while (k) {
		k &= k - 1;
		ret++;
	}
	return ret;
}

bool valid(int mask) {
	int last = -2;
	for (int i = 0; i < m; i++) {
		if (mask & (1 << i)) {
			if (i - last < 2) {
				return false;
			}
			last = i;
		}
	}
	return true;
}

bool fit(int mask, int k) {
	return ((used[k] & mask) == 0);
}

int get(int k, int mask) {
	int & ret = mem[k][mask];
	if (ret != -1) {
		return ret;
	}
	if (k == 0 && fit(mask, k)) {
		ret = bitcnt(mask);
		return ret;
	}
	ret = 0;
	for (int i = 0; i < (1 << m); i++) {
		if (!valid(i)) {
			continue;
		}
		if (!fit(i, k - 1)) {
			continue;
		}
		if (i & ((mask << 1 ) | (mask >> 1))) {
			continue;
		}
		ret = max(ret, bitcnt(mask) + get(k - 1, i));
	}
	return ret;
}

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		memset(mem, -1, sizeof(mem));
		scanf("%d %d\n", &n, &m);
		memset(used, 0, sizeof(used));
		for (int i = 0; i < n; i++) {
			int curmask = 0;
			for (int j = 0; j < m; j++) {
				curmask <<= 1;
				char ch;
				scanf("%c", &ch);
				if (ch == 'x') {
					curmask++;
				}
			}
			used[i] = curmask;
			scanf("\n");
		}
		int ans = 0;
		for (int i = 0; i < (1 << m); i++) {
			if (valid(i) && fit(i, n - 1)) {
				ans = max(ans, get(n - 1, i));
			}
		}
		printf("Case #%d: ", test);
		printf("%d", ans);
		printf("\n");
	}

	return 0;
}
