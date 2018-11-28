#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; ++test) {
		int n, m;
		cin >> n >> m;
		vector< vector<int> > u_um(m, vector<int>());
		vector<int> u_m(m, 0);
		for (int i = 0; i < m; ++i) {
			int t;
			cin >> t;
			for (int j = 0; j < t; ++j) {
				int x, y;
				cin >> x >> y;
				if (y == 0) u_um[i].push_back(x);
				else u_m[i] = x;
			}
		}

		int min = n + 1, mini = -1;
		for (int i = 0; i < (1 << n); ++i) {
			bool sat_all = true;
			for (int j = 0; j < m; ++j) {
				bool sat = false;
				for (int k = 0; k < (int)u_um[j].size(); ++k) {
					if ((i & (1 << (u_um[j][k] - 1))) == 0) sat = true;
				}
				if ((i & (1 << (u_m[j] - 1))) != 0) sat = true;
				sat_all &= sat;
			}
			if (sat_all) {
				int nbits = 0;
				for (int j = 0; j < n; ++j) if ((i & (1 << j)) != 0) ++nbits;
				if (nbits < min) {
					min = nbits;
					mini = i;
				}
			}
		}

		cout << "Case #" << (test + 1) << ": ";
		if (mini == -1) cout << "IMPOSSIBLE" << endl;
		else {
			for (int i = 0; i < n; ++i) {
				cout << ((mini & (1 << i)) ? 1 : 0) << ((i < n-1) ? " " : "");
			}
			cout << endl;
		}
	}
	return 0;
}