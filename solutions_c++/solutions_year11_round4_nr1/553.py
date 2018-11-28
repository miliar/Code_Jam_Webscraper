#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <utility>
#include <vector>
#include <set>
#include <cmath>
#include <cstring>

using namespace std;

#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))

typedef long long i64;

const int MAXN = 10000;

int u[MAXN];
struct Q {
	int b, e, w;
	bool operator<(const Q &x) const {
		return b < x.b;
	}
} q[MAXN];

int main() {
	int T; scanf("%d", &T);
	memset(u, ~0, sizeof(u));
	for (int tt = 0; tt < T; ++tt) {
		int x, s, r, n;
		double t;
		cin >> x >> s >> r >> t >> n;
		for (int i = 0; i < n; ++i) {
			cin >> q[i].b >> q[i].e >> q[i].w;
		}
		sort(q, q + n);
		int m = n;
		for (int i = 0; i < n; ++i) {
			if (!i && q[i].b) {
				q[m].b = 0;
				q[m].e = q[i].b;
				q[m].w = 0;
				++m;
			} else if (i && (q[i].b > q[i - 1].e)) {
				q[m].b = q[i - 1].e;
				q[m].e = q[i].b;
				q[m].w = 0;
				++m;
			}
			if (i == n - 1 && q[i].e < x) {
				q[m].b = q[i].e;
				q[m].e = x;
				q[m].w = 0;
				++m;
			}
		}
		n = m;
		sort(q, q + n);
/*		for (int i = 0; i < n; ++i) {
			cout << q[i].b <<  " " << q[i].e << endl;;
		}*/
		double result = 0;
		for (int i = 0; i < n; ++i) {
			double dt = -1;
			int k = -1;
			for (int j = 0; j < n; ++j) if (u[j] != tt) {
				double p = (q[j].e - q[j].b) / (double)(q[j].w + r);
				if (p > t) p = t;
				double t1 = (q[j].e - q[j].b) / (double)(q[j].w + s);
				double t2 = p + (q[j].e - q[j].b - p * (q[j].w + r)) / (double)(q[j].w + s);
//				cout << t1 - t2 << " " << q[j].w << " " << p << endl;
				if (k == -1 || q[j].w < q[k].w) {
					k = j;
				}
				/*if (t1 - t2 > dt) {
					dt = t1 - t2;
					k = j;
				}*/
			}
			if (k == -1) break;
			u[k] = tt;
			double p = (q[k].e - q[k].b) / (double)(q[k].w + r);
			if (p > t) p = t;
			result += p + (q[k].e - q[k].b - p * (q[k].w + r)) / (double)(q[k].w + s);
			t -= p;
		}
/*		cout << result << endl; 
		cout << x << " " << t << endl;*/
		for (int i = 0; i < n; ++i) if (u[i] != tt) {
// 			cout << i << endl;
			result += (q[i].e - q[i].b) / (double)(q[i].w + s);
		}
/*		for (int i = 0; i < n; ++i) {
			x -= q[i].e - q[i].b;
		}
		double p = x / (double)r;
		if (p > t) p = t;
		result += p;
		x -= r * p;
		result += x / (double)s;*/
		printf("Case #%d: %.8lf\n", tt + 1, result);
	}
	return 0;
}
