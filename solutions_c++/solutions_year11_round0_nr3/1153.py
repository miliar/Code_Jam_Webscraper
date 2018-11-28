#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> list;

int ans = 0;

void solve(int i, int p, int px, int s, int sx) {
	
	if (ans > 0) return;
	if (i < 0) {
		if (px == sx && p != 0 && s != 0)
			ans = s;

		return;
	}

	solve(i-1, p, px, s+list[i], sx^list[i]);
	solve(i-1, p+list[i], px^list[i], s, sx);

}

int main () {

	int T;

	cin >> T;

	list.reserve(1024);

	for (int t = 1; t <= T; ++t) {
	
		int N;

		list.clear();

		cin >> N;
		for (int i = 0; i < N; ++i) {
			int c;
			cin >> c;
			list.push_back(c);

		}

		sort(list.begin(), list.end());

		ans = 0;

		solve(N-1, 0, 0, 0, 0);

		if (ans == 0)
			cout << "Case #" << t << ": NO" << endl;
		else 
			cout << "Case #" << t << ": " << ans << endl;
		
	}

	return 0;
}


