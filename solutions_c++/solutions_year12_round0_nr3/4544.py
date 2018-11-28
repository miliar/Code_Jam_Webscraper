#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <sstream>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t_cnt;
	cin >> t_cnt;
	for (int t = 0; t < t_cnt; ++t) {
		int a, b;
		cin >> a >> b;
		int ans = 0;
		for (int i = a; i <= b; ++i) {
			ostringstream oss;
			oss << i;
			string str = oss.str();
			set<int> valid;
			for (size_t j = 0; j < str.size(); ++j)
				if (str[j] != '0') {
					istringstream iss(str.substr(j, 100) + str.substr(0, j));
					int other;
					iss >> other;
					if (other > i && other <= b)
						valid.insert(other);
				}
			ans += valid.size();
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}
