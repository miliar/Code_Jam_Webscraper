#include <string>
#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

int n;
long long d;
int p[300], v[300];
long long q[2000000], qx[2000000];

inline bool check(long long t) {
	copy(q, q + n, qx);
	qx[0] = qx[0] - t;
	for (int i = 1; i < n; ++i) {
		long long pos = qx[i-1] + d;
		if (qx[i] < pos && pos - q[i] > t) {
			return false;
		}
		qx[i] = qx[i] - t;
		if (qx[i] < pos) {
			qx[i] = pos;
		}	
	}
	return true;
}

int main() {
	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ++ti) {
		int c;
		cin >> c >> d;
		n = 0;
		for (int i = 0; i < c; ++i) {
			cin >> p[i] >> v[i];
			for (int j = 0; j < v[i]; ++j) {
				q[n++] = p[i] * 2;
			}
		}
		d *= 2;
		long long ans = 0LL;
		if (!check(0)) {
			long long ansMin = 0LL; // can't for sure
			long long ansMax = 2 * n * d; // can for sure
			while (ansMin + 1 < ansMax) {
				long long mid = (ansMin + ansMax) / 2;
				if (!check(mid)) {
					ansMin = mid;
				}
				else {
					ansMax = mid;
				}
			}
			ans = ansMax;
		}
		printf("Case #%d: %Lf\n", ti, ans * 0.5L);
		
	}

}
