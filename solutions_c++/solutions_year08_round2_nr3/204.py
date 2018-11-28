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

#define MAXN 5010

int next[MAXN];
int prev[MAXN];
int a[MAXN];

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	int tests;
	scanf("%d", &tests);
	for (int test = 0; test < tests; test++) {
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			next[i] = (i + 1) % n;
			prev[i] = (i + n - 1) % n;
		}
		int cur = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < i; j++) {
				cur = next[cur];
			}
			a[cur] = i + 1;
			next[prev[cur]] = next[cur];
			prev[next[cur]] = prev[cur];
			cur = next[cur];
		}
		int k;
		scanf("%d", &k);
		printf("Case #%d: ", test + 1);
		for (int i = 0; i < k; i++) {
			int q;
			scanf("%d", &q);
			printf("%d ", a[q - 1]);
		}
		printf("\n");
	}

	return 0;
}
