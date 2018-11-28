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

string taskname = "cc";

#define MAXN (1 << 16)
#define MMAX 128

int mem[MAXN];
int ind[MAXN];
int v[MMAX][MMAX];
int a[MMAX][MMAX];
int n, k;

bool inter(int y11, int y12, int y21, int y22) {
	if (y11 > y21) {
		swap(y11, y21);
		swap(y12, y22);
	}
	return (y11 == y21 || (y12 >= y22));
}

int intersect(int a[MAXN], int b[MAXN]) {
	for (int i = 1; i < k; i++) {
		if (inter(a[i - 1], a[i], b[i - 1], b[i])) {
			return 1;
		}
	}
	return 0;
}

#define INF (1 << 30)

int get(int mask) {
	if (mask == 0) {
		return 0;
	}
	int & ret = mem[mask];
	if (ret != -1) {
		return ret;
	}
	ret = INF;
	for (int next = mask; next; next = (next - 1) & mask) {
		if (!ind[next]) {
			continue;
		}
		ret = min(ret, get(mask ^ next) + 1);
	}
	return ret;
}

int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int tests;
	scanf("%d\n", &tests);
	for (int test = 0; test < tests; test++) {
		memset(mem, -1, sizeof(mem));
		
		cin >> n >> k;
		memset(a, 0, sizeof(a));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < k; j++) {
				cin >> v[i][j];
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				a[i][j] = intersect(v[i], v[j]);
				cerr << a[i][j] << " ";
			}
			cerr << endl;
		}

		for (int i = 0; i < (1 << n); i++) {
			ind[i] = 1;
			for (int i1 = 0; i1 < n; i1++) {
				for (int i2 = i1 + 1; i2 < n; i2++) {
					if (!(i & (1 << i1))) {
						continue;
					}
					if (!(i & (1 << i2))) {
						continue;
					}
					if (a[i1][i2]) {
						ind[i] = 0;
						break;
					}
				}
			}
		}

		int ans = get((1 << n) - 1);

		cout << "Case #" << test + 1 << ": ";
		cout << ans;
		cout << endl;
	}

	return 0;
}
