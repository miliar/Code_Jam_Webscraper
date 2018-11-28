#include <iostream>
using namespace std;

int main() {
	int C;
	cin >> C;
	for (int c = 1; c <= C; c++) {
		long long N, K, B, T;
		cin >> N >> K >> B >> T;
		long long X[N], V[N];
		for (int i = 0; i < N; i++) cin >> X[i];
		for (int i = 0; i < N; i++) cin >> V[i];
		int bad = 0, ans = 0;
		cout << "Case #" << c << ": ";
		if (K == 0) {
			cout << 0 << endl;
			continue;
		}
		for (int i = N-1; i >= 0; i--) {
			if (X[i]+T*V[i] < B) {
				bad++;
				continue;
			}
			ans += bad;
			if (N-i-bad == K) {
				cout << ans << endl;
				break;
			}
		}
		if (N-bad < K) cout << "IMPOSSIBLE" << endl;
	}
}
