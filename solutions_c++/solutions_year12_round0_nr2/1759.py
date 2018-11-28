#include <iostream>

using namespace std;

int main() {
	int Tc;
	int n, s, p;
	int t[110];
	cin >> Tc;
	for (int re = 1; re <= Tc; ++re) {
		cin >> n >> s >> p;
		for (int i = 0; i < n; ++i) {
			cin >> t[i];
		}

		int ans = 0;
		for (int i = 0; i < n; ++i) {
			if (max(0, p - 1) * 2 + p <= t[i]) {
				ans++;
			} else if (max(0, p - 2) * 2 + p <= t[i] && s > 0) {
				ans++;
				s--;
			}
		}
		cout << "Case #" << re << ": " << ans << endl;
	}
	return 0;
}
