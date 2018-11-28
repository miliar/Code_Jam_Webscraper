#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

#pragma comment(linker, "/STACK:160000000")

const int N = 11;

vector <int> a[N];
int u[N];
int v[N];
int ans[N];
int n, k;
int mn;
bool color[N];

bool solve(int pos) {
//	cerr << pos << endl;
	if (pos == n)
		return 1;
	for (ans[pos] = 0; ans[pos] < mn; ans[pos]++) {
		bool ok = 1;
		for (int i = 0; i < k; ++i) {
			memset(color, 0, sizeof(color));
			int cnt = 0;
			for (int j = 0; j < a[i].size(); ++j) {
				if (a[i][j] > pos) {
					++cnt;
				} else {
					if (!color[ans[a[i][j]]]) {
						++cnt;
						color[ans[a[i][j]]] = 1;
					}
				}
			}
			if (cnt < mn) {
				ok = 0;
				break;
			}
		}	
	    if (ok) {
	    	if (solve(pos + 1))
	    		return 1;
	    }
	}
	return 0;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif

	int t;
	scanf("%d", &t);

	for (int tt = 0; tt < t; ++tt) {
		int m;
		k = 1;
		scanf("%d%d", &n, &m);

		for (int i = 0; i < n; ++i) {
			a[i].clear();
		}
		for (int i = 0; i < n; ++i) {
			a[0].push_back(i);
		}

		for (int i = 0; i < m; ++i) {
			scanf("%d", &u[i]);
			--u[i];
		}
		for (int i = 0; i < m; ++i) {
			scanf("%d", &v[i]);
			--v[i];
		}

		for (int i = 0; i < m; ++i) {
			for (int j = 0; j < k; ++j) {
				if (u[i] > v[i]) {
					swap(u[i], v[i]);
				}
				int p1 = -1;
				int p2 = -1;
				for (int y = 0; y < a[j].size(); ++y) {
					if (a[j][y] == u[i]) {
						p1 = y;
					}
					if (a[j][y] == v[i]) {
						p2 = y;
					}
				}
				if (p1 != -1 && p2 != -1) {
					for (int y = p1; y <= p2; ++y) {
						a[k].push_back(a[j][y]);
					}
					for (int y = p2; y < a[j].size(); ++y) {
						a[j][p1 + y - p2 + 1] = a[j][y];
					}
					for (int y = 0; y < p2 - p1 - 1; ++y) {
						a[j].pop_back();
					}
					++k;
					break;
				}
			}
		}

		mn = a[0].size();
		for (int i = 1; i < k; ++i) {
			mn = min(mn, (int)a[i].size());
		}

		while (!solve(0)) {
			--mn;
			solve(0);
		}

		printf("Case #%d: %d\n", tt + 1, mn);

		for (int i = 0; i < n; ++i) {
			printf("%d ", ans[i] + 1);
		}

		printf("\n");
/*		for (int i = 0; i < k; ++i) {
			for (int j = 0; j < a[i].size(); ++j) {
				printf("%d ", a[i][j]);
			}
			printf("\n");
		}
*/			
	}

	return 0;
}
