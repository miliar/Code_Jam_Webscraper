#include <iostream>
#include <string>
#include <set>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, M;
		cin >> N >> M;
		set<string> dirs;
		for (int i = 0; i < N; i++) {
			string d;
			cin >> d;
			dirs.insert(d);
		}
		int ans = 0;
		for (int i = 0; i < M; i++) {
			string d;
			cin >> d;
			for (int j = 1; j < d.size(); j++)
				if (d[j] == '/') {
					string d2(d, 0, j);
					if (!dirs.count(d2)) {
						ans++;
						dirs.insert(d2);
					}
				}
			if (!dirs.count(d)) {
				ans++;
				dirs.insert(d);
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
