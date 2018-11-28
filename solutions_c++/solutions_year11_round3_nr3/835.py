#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int N; cin >> N;
		int L, H; cin >> L >> H;
		vector<int> data;
		for (int i = 0; i < N; i++) {
			int v; cin >> v;
			data.push_back(v);
		}
		bool ok = false;
		int ans = 0;
		for (int i = L; i <= H; i++) {
			bool done = true;
			for (int j = 0; j < data.size(); j++) {
				int a = max(data[j],i);
				int b = min(data[j],i);
				if (a % b != 0) {
					done = false;
					break;
				}
			}
			if (done) {
				ok = true;
				ans = i;
				break;
			}
		}
		cout << "Case #" << t << ": ";
		if (!ok) cout << "NO\n";
		else cout << ans << "\n";
	}
	return 0;
}