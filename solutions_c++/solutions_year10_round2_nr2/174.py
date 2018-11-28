#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <string>
#include <map>
#include <set>
#include <numeric>
#include <algorithm>

#include <cmath>
#include <ctime>
#include <cstring>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int cas = 1; cas <= T; ++cas) {
		int n, k, b, time;
		cin >> n >> k >> b >> time;

		vector<int> x(n);
		for (int i = 0; i < n; ++i) {
			cin >> x[i];
		}

		vector<int> v(n);
		for (int i = 0; i < n; ++i) {
			cin >> v[i];
		}

		vector<int> pos(n);
		int res = 0;
		int bad = 0;

		for (int i = n - 1; i >= 0; --i) {
			pos[i] = x[i] + time * v[i];
			if (pos[i] >= b && k > 0) {
				res += bad;
				--k;
			}
			if (pos[i] < b) {
				++bad;
			}
		}

		if (k == 0) {
			cout << "Case #" << cas << ": " << res << endl;
		} else {
			cout << "Case #" << cas << ": " << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
