#include <iostream>
#include <string>

using namespace std;

typedef long long ll;
typedef pair<ll, int> pii;

int main() {
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int R, k, N; cin >> R >> k >> N;
		int g[N];
		for (int i = 0; i < N; i++)
			cin >> g[i];
		pii cache[N]; // first = euros made, second = next starter
		for (int i = 0; i < N; i++) {
			int total = 0, j;
			bool first = true;
			for (j = i; total + g[j] <= k && (j != i || first); j = (j + 1)%N) {
				first = false;
				total += g[j];
			}
			cache[i].first = ll(total);
			cache[i].second = j;
		}
		// get answer
		ll ans = 0LL;
		int curr = 0;
		for (int i = 0; i < R; i++) {
			ans += cache[curr].first;
			curr = cache[curr].second;
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
}

