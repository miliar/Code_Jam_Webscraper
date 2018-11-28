#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#define out(v) cout << #v << ": " << (v) << endl
using namespace std;
typedef long long LL;

int T;
int X, S, R, t, N;
typedef pair<int, int> pr;
pr seg[1005];
int sgn(double x, double eps = 1.0e-9) {
	return (x > eps) - (x < -eps);
}

int main() {
	cin >> T;
	for (int id = 1; id <= T; ++id) {
		cin >> X >> S >> R >> t >> N;
		int tot = 0;
		for (int i = 0; i < N; ++i) {
			int B, E, w;
			cin >> B >> E >> w;
			seg[i] = pr(w + S, E - B);
			tot += E - B;
		}
		seg[N] = pr(S, X - tot);
		sort(seg, seg + N + 1);
		double remain = t, sum = 0.0;
		for (int i = 0; i <= N; ++i) {
			double sp = seg[i].first - S + R;
			double cost = min(remain, seg[i].second / sp);
			sum += cost + (seg[i].second - sp * cost) / seg[i].first;
			remain -= cost;
		}
		printf("Case #%d: %.9f\n", id, sum);
	}
	return 0;
}
