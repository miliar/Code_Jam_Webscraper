#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <set>
#include <map>
using namespace std;

#define N 300005
#define K 150000
typedef long long ll;

int d[N];
int mx, i, j, k, n, m, tp;
int x, y;
ll l, z, t, res, r, tr;

struct st {
	int x;
	int c;
	friend int operator < (st a, st b) {
		return a.c > b.c;
	}
};

st s, s1;
priority_queue<st> q;
int T, tt;
int a[N];

int main() {
	freopen("large.in", "r", stdin);	freopen("large.out", "w", stdout);

	scanf("%d", &T);
	for (tt = 1; tt <= T; tt ++) {
		memset(d, -1, sizeof(d));
		scanf("%lld%d", &l, &n);
		mx = 0;
		for (i = 0; i < n; i++) {
			scanf("%d", &a[i]);
			if (a[i] > mx) {
				mx = a[i];
			}
		}
		tr = l / mx;
		tp = l % mx;
		x = l % mx;
		s.x = 0;
		s.c = 0;
		d[s.x + K] = 0;
		while (!q.empty()) q.pop();
		q.push(s);
		while (!q.empty()) {
			s = q.top();
			if (s.x == tp) {
				break;
			}
			q.pop();
			for (i = 0; i < n; i ++) {
				x = s.x + a[i];
				if (x >= mx || x <= -mx) {
					continue;
				}
				if (d[x + K] == -1 || d[x+K] > d[s.x + K] + 1) {
					s1.x = x;
					s1.c = d[s.x + K] + 1;
					d[s1.x + K] = s1.c;
					q.push(s1);
				}
				x = s.x + a[i] - mx;
				if (x >= mx || x <= -mx) {
					continue;
				}
				if (d[x + K] == -1 || d[x+K] > d[s.x + K]) {
					s1.x = x;
					s1.c = d[s.x + K];
					d[s1.x + K] = s1.c;
					q.push(s1);
				}
			}
		}
		printf("Case #%d: ", tt);
		if (d[K+tp] == -1) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%lld\n", d[K+tp] + tr);
		}
	}
	return 0;
}


