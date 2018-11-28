#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

typedef double db;
const db pinf = 100000;
const int steps = 100;
const int maxn = 1000100;
const db eps = 1e-9;

int T;
int C;
db D;
int P, V;
int N;
db v[maxn];
db d[maxn]; 

db l, r, res;

inline bool check(db t) {
	d[1] = v[1] - t;
	for (int i = 2; i <= N; i++) {
		if (v[i] + t - d[i - 1] < D - eps) {
			return false;
		} else {
			db tmp = v[i] - d[i - 1];
			if (tmp > D) {
				d[i] = max(d[i - 1] + D, v[i] - t);
			} else {
				d[i] = d[i - 1] + D;
			}
		}
	}	
	return true;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	for (int t = 1; t <= T; t++) {
		N = 0;
		cin >> C;
		cin >> D;		
		for (int i = 0; i < C; i++) {
			cin >> P >> V;
			N += V;
			for (int j = 0; j < V; j++) {
				v[N - j] = P;
			}
		}

		l = 0, r = pinf;
		for (int st = 0; st < steps; st++) {
			res = (l + r) / 2;
			if (check(res)) {
				r = res;
			} else {
				l = res;
			}
		}

	   printf("Case #%d: %.9lf\n", t, r);
	}
}