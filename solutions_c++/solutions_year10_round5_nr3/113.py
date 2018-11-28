#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <utility>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define _foreach(it, b, e) for (typeof(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)
#define rep(i, n) foreach(i, 0, n)

#define MSET(c, v) memset(c, v, sizeof(c))

const int INF = 0x3f3f3f3f; const int NEGINF = 0xC0C0C0C0;
const int NULO = -1;
double EPS = 1.e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
map<int, int> num;
int main() {
	TRACE(setbuf(stdout, NULL));
	int _42;
	scanf("%d", &_42);
	rep(_41, _42) {
		printf("Case #%d:", _41+1);
		num.clear();
		int C;
		scanf("%d", &C);
		int numa = 0;
		int ans = 0;
		int posa = -1000000000;
		rep(c, C) {
			int P, V;
			scanf("%d %d", &P, &V);
			num[P] = V;
		}
		while (1) {
			int qual = -1000000000;
			foreach(it, all(num)) {
				if (it->second > 1) {
					qual = it->first;
					break;
				}
			}
			if (qual == -1000000000) break;
			ans++;
			num[qual] -= 2;
			if (num.count(qual-1) == 0) num[qual-1] = 0;
			num[qual-1]++;
			if (num.count(qual+1) == 0) num[qual+1] = 0;
			num[qual+1]++;
		}
		printf(" %d\n", ans);
	}
	return 0;
}
