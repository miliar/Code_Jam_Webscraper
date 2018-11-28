#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#define MOD 10007
using namespace std;

int N, H, W, R;

int gcd(int a, int b) {
	return b ? gcd(b, a % b) : a;
}

long long cmb(int a, int b) {
	b = min(a - b, b);
	vector<int> v(b);
	for (int i = 0; i < b; i++)
	 v[i] = a - i;
/*	for (int i = b; 1 < i; i--) {
		int p = a % i;
		while (v[p] % i) p += i;
		if (b <= p) printf("%dC%d %d %d\n", a, b, i, p);
		v[p] /= i;
	}*/
	for (int i = b; 1 < i; i--) {
		int t = i;
		for (int j = 0; j < b && t != 1; j++) {
			int g = gcd(v[j], t);
			if (g != 1) {
				v[j] /= g; t /= g;
			}
		}
		if (t != 1) {
			fprintf(stderr, "%dC%d Error\n", a, b);
		}
	}
	long long r = 1;
	for (int i = 0; i < b; i++) {
		r = (r * v[i]) % MOD;
	}
	return r;
}

int main() {
	cin >> N;
	for (int case_x = 1; case_x <= N; case_x++) {
		cin >> H >> W >> R;
		vector< pair<int, int> > rc; rc.clear();
		int h = H - 1, w = W - 1;
		int x = (2 * w - h) / 3, y = (2 * h - w) / 3;
		for (int i = 0; i < R; i++) {
			int HH, WW;
			cin >> HH >> WW; WW--; HH--;
			if ((2 * WW - HH) % 3 || (2 * HH - WW) % 3)
			 continue;
			int xx = (2 * WW - HH) / 3, yy = (2 * HH - WW) / 3;
			if (xx < 0 || yy < 0) continue;
			if (x < xx || y < yy) continue;
			rc.push_back(make_pair(xx, yy));
		}
		sort(rc.begin(), rc.end());
		if ((2 * w - h) % 3 || (2 * h - w) % 3 || x < 0 || y < 0) {
			printf("Case #%d: 0\n", case_x);
			continue;
		}
		long long cnt = cmb(x + y, x);
		//fprintf(stderr, "Cnt: %lld\n", cnt);
		vector<int> rr(rc.size(), 1);
		for (int i = 0; i < rc.size(); i++) {
			rr[i] = cmb(rc[i].first + rc[i].second, rc[i].first);
			for (int j = 0; j < i; j++) {
				int dx = rc[i].first - rc[j].first,
				 dy = rc[i].second - rc[j].second;
				if (dx < 0 || dy < 0) continue;
				rr[i] -= rr[j] * cmb(dx + dy, dx);
				rr[i] = (rr[i] + MOD) % MOD;
			}
			rr[i] %= MOD;
			int dx = x - rc[i].first, dy = y - rc[i].second;
			cnt = (cnt + MOD - (rr[i] * cmb(dx + dy, dx)) % MOD) % MOD;
		}
		printf("Case #%d: %lld\n", case_x, cnt);
	}
	return 0;
}