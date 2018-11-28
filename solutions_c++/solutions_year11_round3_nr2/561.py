#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
using namespace std;

typedef long long ll;

const int MAX_N = 1000 * 1000 + 10;

int N, L, C;
ll T, A[1001], presum[MAX_N + 1];

ll BestSum(int first, int m) {
	vector<ll> rem, base;
	while (first < N && first % C != 0) {
		rem.push_back(A[first % C]);
		++first;
	}
	int last = N;
	while (last > first && last % C != 0) {
		--last;
		rem.push_back(A[last % C]);
	}
	sort(rem.begin(), rem.end());
	for (int i = 0; i < C; ++i)
		base.push_back(A[i]);
	sort(base.begin(), base.end());
	int baseN = (last - first) / C;

	ll ans = 0;
	while ((!base.empty() || !rem.empty()) && m > 0)
		if (!base.empty() && (rem.empty() || base.back() > rem.back())) {
			int delta = min(baseN, m);
			ans += base.back() * delta;
			base.pop_back();
			m -= delta;
		} else {
			ans += rem.back();
			rem.pop_back();
			m -= 1;
		}
	return ans;
}

string solve() {
	cin >> L >> T >> N >> C;
	for (int i = 0; i < C; ++i) cin >> A[i];

	presum[0] = 0;
	for (int i = 0, j = 0; i < N; ++i) {
		presum[i + 1] = presum[i] + A[j];
		if (++j == C) j = 0;
	}
	
	ll ans = 0;
	for (int i = 0; i < N; ++i)
		if (presum[i] * 2 >= T) {
			ll t;

			t = BestSum(i, L);
			if (t > ans) ans = t;

			if (L > 0 && i > 0) {
				t = BestSum(i, L - 1);

				ll len = presum[i] - presum[i - 1];
				ll t0 = T - presum[i - 1] * 2;
				t += len - t0 / 2;
				if (t > ans) ans = t;
			}
			break;
		}
	ostringstream out;
	out << presum[N] * 2 - ans;
	return out.str();
}

int main(int argc, char* argv[]) {
    if (argc > 1) {
        char* file_name = argv[1];
        int len = strlen(file_name);
        if (strcmp(file_name + len - 3, ".in") == 0)
            file_name[len - 3] = 0;
        else if (strcmp(file_name + len - 1, ".") == 0)
            file_name[len - 1] = 0;
        freopen((string(file_name) + ".in").c_str(), "r", stdin);
        freopen((string(file_name) + ".out").c_str(), "w", stdout);
    }
    int cc = 0, ccc = 0;
    for (cin >> ccc; cc < ccc; ++cc)
            cout << "Case #" << cc + 1 << ": " << solve() << endl;
    return 0;
}
