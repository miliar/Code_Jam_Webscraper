#include <stdio.h>
#include <string.h>
#include <math.h>
#include <memory.h>
#include <ctype.h>
#include <stdlib.h>
#include <assert.h>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <iostream>
#include <sstream>

#define int64 long long

using namespace std;

string taskname = "aa";

#define MAXN 128

int a[MAXN];

int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int tests;
	scanf("%d\n", &tests);
	for (int test = 0; test < tests; test++) {
		int n;
		scanf("%d\n", &n);
		char s[100];
		memset(a, 0, sizeof(a));
		for (int i = 0; i < n; i++) {
			gets(s);
			for (int j = 0; j < n; j++) {
				if (s[j] == '1') {
					a[i] = j;
				}
			}
		}
		int ans = 0;
		for (int i = 0; i < n; i++) {
			for (int j = i; j < n; j++) {
				int cur = a[j];
				if (a[j] <= i) {
					for (int l = j - 1; l >= i; l--) {
						a[l + 1] = a[l];
					}
					a[i] = cur;
					ans += j - i;
					break;
				}
			}
		}

		cout << "Case #" << test + 1 << ": ";
		cout << ans;
		cout << endl;
	}

	return 0;
}
