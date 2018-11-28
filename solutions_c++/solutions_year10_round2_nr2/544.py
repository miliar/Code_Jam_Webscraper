#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

#define PROBLEM_NAME "b"
#define MAXN 50

int n, k, b, t;
int x[MAXN], v[MAXN];
int tim[MAXN];
bool can[MAXN];

int main () {
	freopen (PROBLEM_NAME ".in", "rt" ,stdin);
	freopen (PROBLEM_NAME ".out", "wt" ,stdout);
	int CC; scanf ("%d", &CC);
	for (int tt = 1; tt <= CC; tt++) {
		printf ("Case #%d: ", tt);
		scanf ("%d%d%d%d", &n, &k, &b, &t);
		for (int i = 0; i < n; i++) {
			scanf ("%d", x+i);
		}
		for (int i = 0; i < n; i++) {
			scanf ("%d", v+i);
		}
		int kol = 0;
		for (int i = 0; i < n; i++) {
			tim[i] = (b + v[i] - 1 - x[i]) / v[i];
			if (tim[i] <= t) {
				kol++;
				can[i] = true;
			} else {
				can[i] = false;
			}
		}
		if (kol < k) {
			printf ("IMPOSSIBLE\n");
			continue;
		}
		kol = 0;
		int add = 0;
		for (int i = n-1; i >= 0 && k > 0; i--) {
			if (can[i]) {
				k--;
				kol += add;
			} else {
				add++;
			}
		}
		printf ("%d\n", kol);
	}
	return 0;
}
