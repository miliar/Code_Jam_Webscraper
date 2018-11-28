#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <map>

using namespace std;

int t, n, a[10], s, p;
int cnt_bit(int i) {
	int res = 0;
	if ((1 << 2) & i) res++;
	if ((1 << 1) & i) res++;
	if ((1 << 0) & i) res++;
	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for (int q = 1; q <= t; q++) {
		int ans = 0;
		cin >> n >> s >> p;
		for (int i = 0; i < n; i++) cin >> a[i];
		for (int i = 0; i < n; i++)
			if (a[i] % 3 == 0) {
				if (a[i] / 3 >= p) ans++;
				else if (s > 0 && a[i] > 0 && a[i] / 3 + 1 >= p) {
					ans++;
					s--;
				}
			} else if (a[i] % 3 == 1) {
				if (a[i] / 3 + 1 >= p) ans++;
			} else {
				if (a[i] / 3 + 1 >= p) ans++;
				else if (a[i] / 3 + 2 >= p && a[i] > 1 && s > 0) {
					ans++;
					s--;
				}
			}
		cout << "Case #" << q << ": " << ans << endl;
	}
}