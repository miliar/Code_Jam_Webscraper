#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <string>

using namespace std;

typedef long long ll;

const int M = 1000000000;

int ys[2010];
int h[2010];

bool check(int n) {
	for(int i = 0; i < n; ++i) if(h[i] < 0 || h[i] > M) return false;
	for(int i = 0; i < n - 1; ++i) {
		for(int j = i + 1; j < ys[i]; ++j) {
			if((h[j] - h[i]) * (ll)(ys[i] - i) >= (h[ys[i]] - h[i]) * (ll)(j - i)) return false;
		}
		for(int j = ys[i] + 1; j < n; ++j) {
			if((h[j] - h[i]) * (ll)(ys[i] - i) > (h[ys[i]] - h[i]) * (ll)(j - i)) return false;
		}
	}
	return true;
}

bool go(int s, int t, int d) {
	if(s == t) return true;
	int pos = -1;
	for(int i = s; i < t && pos == -1; ++i) if(ys[i] == t) pos = i;
	if(pos == -1) return false;
	h[pos] = h[t] - d * (t - pos);
	if(!go(pos + 1, t, d + 1) || !go(s, pos, d)) return false;
	return true;
}

int main() {
	int T;
	cin >> T;
	for(int c = 1; c <= T; ++c) {
		int n;
		cin >> n;
		for(int i = 0; i < n - 1; ++i) cin >> ys[i];
		for(int i = 0; i < n - 1; ++i) --ys[i];
		h[n - 1] = M;
		bool ok = go(0, n - 1, 0);
		printf("Case #%d:", c);
		if(!ok) puts(" Impossible");
		else {
			for(int i = 0; i < n; ++i) printf(" %d", h[i]);
			puts("");
			if(!check(n)) {
				cerr << "err" << endl;
				break;
			}
		}
	}
	return 0;
}
