#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

typedef long long ll;

const ll inf = 99999999999999999ll;

int C, D;

ll pos[256];
int cnt[256];

bool run(ll t2) {
	// t2 is twice the actual time
	ll x = -2 * inf;
	for (int i = 0; i < C; ++i) {
		for (int v = 0; v < cnt[i]; ++v) {
			// find lefmost
			ll leftmost = pos[i] - t2;
			ll next = x + D;
			ll loc = max(leftmost, next);
			//cout << " l=" << leftmost << " next=" << next << " loc=" << loc << endl;
			if (abs(loc - pos[i]) > t2) {
				return false;
			}
			x = loc;
		}
	}
	return true;
}

int main() {
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt) {
		cin >> C >> D;
		D *= 2;
		for (int i = 0; i < C; ++i) {
			cin >> pos[i] >> cnt[i];
			pos[i] *= 2;
		}
		ll mi = 0, ma = inf;
		while (mi < ma) {
			ll mx = (mi + ma) / 2;
			if (run(mx)) {
				ma = mx;
			} else {
				mi = mx + 1;
			}
		}
		cout << "Case #" << tt << ": " << (mi/2);
		if (mi % 2) {
			cout << ".5";
		}
		cout << endl;
	}
	return 0;
}

