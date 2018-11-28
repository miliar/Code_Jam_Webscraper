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

string taskname = "b1";

#define MAXN 10001
#define INF (1 << 30)

int a[MAXN];
int l[MAXN];
int r[MAXN];
string s[MAXN];


int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int tests;
	scanf("%d", &tests);
	for (int test = 0; test < tests; test++) {
		printf("Case #%d: ", test + 1);
		int n;
		scanf("%d\n", &n);
		for (int i = 0; i < n; i++) {
			char buf[50];
			scanf("%s %d %d\n", buf, &l[i], &r[i]);
			s[i] = string(buf);
		}
		int ans = INF;
		for (int i = 0; i < (1 << n); i++) {
			memset(a, 0, sizeof(a));
			set <string> used;
			used.clear();
			int cnt = 0;
			for (int j = 0; j < n; j++) {
				if (i & (1 << j)) {
					used.insert(s[j]);
					if (used.size() > 3) {
						break;
					}
					cnt++;
					for (int k = l[j]; k <= r[j]; k++) {
						a[k] = 1;
					}
				}
			}
			bool ok = (used.size() <= 3);
			for (int j = 1; j < MAXN; j++) {
				if (a[j] == 0) {
					ok = false;
					break;
				}
			}
			if (ok) {
				ans = MIN(ans, cnt);
			}
		}
		if (ans == INF) {
			printf("IMPOSSIBLE");
		} else {
			printf("%d", ans);
		}
		printf("\n");
	}

	return 0;
}
