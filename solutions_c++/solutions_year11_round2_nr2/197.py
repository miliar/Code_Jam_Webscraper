#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

typedef pair<int, int> P;
typedef long long ll;

P ps[210];

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		int n, d;
		cin >> n >> d;
		for(int i = 0; i < n; ++i) {
			cin >> ps[i].first >> ps[i].second;
		}
		sort(ps, ps + n);
		long double left = 0, right = 1E20;
		for(int L = 0; L < 200; ++L) {
			long double half = (left + right) / 2;
			long double pos = -1E30;
			bool ok = true;
			for(int i = 0; i < n && ok; ++i) {
				pos = max(pos + d, ps[i].first - half);
				if(abs(pos - ps[i].first) > half + (half + 1) * 1E-10) ok = false;
				pos = pos + (ps[i].second - 1.0) * d;
				if(abs(pos - ps[i].first) > half + (half + 1) * 1E-10) ok = false;
			}
			if(ok) right = half;
			else left = half;
		}
		printf("Case #%d: ", t);
		if(abs(left - right) > 1E-4) cerr << "hoge" << endl;
		printf("%.10f\n", (double)(left + right) / 2);
	}
	return 0;
}
