#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(void) {
	int T;
	cin >> T;
	for (int testNo = 1; testNo <= T; testNo++) {
		int n, m;;
		cin >> n >> m;
		vector<string> v(n);
		for (int i = 0; i < n; i++) {
			cin >> v[i];
		}
		bool failed = false;
		while (true) {
			bool found = false;
			for (int i = 0; i < n && !found; i++) {
				for (int j = 0; j < m && !found; j++) {
					if (v[i][j] != '#')
						continue;
					found = true;
					if (i == n - 1 || j == m - 1) {
						failed = true;
					} else if (v[i+1][j] != '#' || v[i][j+1] != '#' || v[i+1][j+1] != '#') {
						failed = true;
					} else {
						v[i+1][j] = v[i][j+1] = '\\';
						v[i][j] = v[i+1][j+1] = '/';
					}
				}
			}
			if (!found || failed)
				break;
		}
		cout << "Case #" << testNo << ":" << endl;
		if (failed) {
			cout << "Impossible" << endl;
		} else {
			for (int i = 0; i < n; i++) {
				cout << v[i] << endl;
			}
		}
	}
	return 0;
}
