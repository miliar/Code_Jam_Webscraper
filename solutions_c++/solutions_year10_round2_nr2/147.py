#include <iostream>

using namespace std;

long long n, k, b, t, res;
long long v[55], x[55];

void process() {
	int cnt1 = 0;
	int cnt2 = 0;
	res = 0;
	for (int i = n; i >= 1; i--) {
		if (x[i] + v[i] * t < b) cnt1++;
		else {
			cnt2++;
			res += cnt1;
		}
		if (cnt2 >= k) {
			cout << res << endl;
			return;
		}
	}
	cout << "IMPOSSIBLE" << endl;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	int test;
	cin >> test;
	
	for (int i = 1; i <= test; i++) {
		cin >> n >> k >> b >> t;
		for (int j = 1; j <= n; j++) cin >> x[j];
		for (int j = 1; j <= n; j++) cin >> v[j];
		cout << "Case #" << i << ": ";
		process();
	}
	
	return 0;
}
