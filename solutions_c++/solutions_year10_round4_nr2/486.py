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
		int p;
		cin >> p;

		vector<int> m(1<<p);
		for (int i = 0; i < (1<<p); ++i) {
			cin >> m[i];
		}

		reverse(m.begin(), m.end());
		vector<int> cost(1 << p);

		for (int i = (1 << p) - 1; i >= 1; --i) {
			cin >> cost[i];
		}

		vector<vector<int> > f(1 + (1 << (p + 1)), vector<int>(p + 1, 1000000000));
		for (int i = (1 << (p + 1)) - 1; i >= 1; --i) {
			for (int miss = 0; miss <= p; ++miss) {
				if (i >= (1 << p)) {
					if (miss <= m[i - (1 << p)]) {
						f[i][miss] = 0;
					}
				} else {
					int l = 2 * i;
					int r = l + 1;
					if (miss + 1 <= p) {
						f[i][miss] = min(f[i][miss], f[l][miss + 1] + f[r][miss + 1]);
					}
					f[i][miss] = min(f[i][miss], f[l][miss] + f[r][miss] + cost[i]);
				}
			}
		}

		int res = f[1][0];
		cout << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}
