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

string taskname = "c";

#define MAXN 128

int cur[MAXN][MAXN];
int next[MAXN][MAXN];

int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 0; test < tests; test++) {
		cout << "Case #" << test + 1 << ": ";
		
		int k;
		cin >> k;

		for (int i = 0; i < k; i++) {
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for (int ii = x1; ii <= x2; ii++) {
				for (int jj = y1; jj <= y2; jj++) {
					cur[ii][jj] = 1;
				}
			}
		}

		int ans = 0;
		while (1) {
			bool dead = true;
			for (int i = 0; i < MAXN; i++) {
				for (int j = 0; j < MAXN; j++) {
					if (cur[i][j]) {
						dead = false;
						break;
					}
				}
			}
			if (dead) {
				break;
			}
			memset(next, 0, sizeof(next));
			for (int i = 1; i < MAXN; i++) {
				for (int j = 1; j < MAXN; j++) {
					int live = cur[i][j - 1] + cur[i - 1][j];
					if (cur[i][j]) {
						if (!live) {
							next[i][j] = 0;
						} else {
							next[i][j] = 1;
						}
					} else {
						if (live == 2) {
							next[i][j] = 1;
						} else {
							next[i][j] = 0;
						}
					}
				}
			}
			memcpy(cur, next, sizeof(cur));
			ans++;
		}
		cout << ans;
		cout << endl;
	}

	return 0;
}
