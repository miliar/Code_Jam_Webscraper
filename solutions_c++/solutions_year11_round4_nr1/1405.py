#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;

typedef long double lld;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_N;
	cin >> test_N;
	for (int test_i = 1; test_i <= test_N; ++test_i) {
		lld X, S, R, T;
		int N;
		cin >> X >> S >> R >> T >> N;
		vector<pair<lld, lld> > wx(N);
		lld L = X;
		for (int i = 0; i < N; ++i) {
			int b, e, w;
			cin >> b >> e >> w;
			wx[i].first = w;
			wx[i].second = e - b;
			L -= wx[i].second;
		}
		wx.push_back(pair<lld, lld> (0, L));
		lld answ = 0.0;
		sort(wx.begin(), wx.end());
		for (int i = 0; i < wx.size(); ++i) {
			lld t = wx[i].second / (R + wx[i].first);
			if (t < T) {
				answ += t;
				T -= t;
			} else {
				answ += T +  (wx[i].second - T * (R + wx[i].first)) / (S + wx[i].first);
				T = 0.0;
			}
		}
		cout.precision(6);
		cout << "Case #" << test_i << ": " << fixed << answ << endl;
	}
	return 0;
}
