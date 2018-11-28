#include <iostream>
#include <string>
#include <algorithm>
#include <assert.h>
using namespace std;

int dp[2][128];
string name[128];

int main() {
	int tc;
	cin >> tc;
	for (int x=1; x<=tc; ++x) {
		int s;
		cin >> s;
		assert(s > 0 && s <= 100);
		getline(cin, name[0]);
		for (int i=0; i<s; ++i)
			getline(cin, name[i]);
		sort(name, name + s);
		int q;
		string query;
		cin >> q;
		getline(cin, query);
		for (int i=0; i<s; ++i)
			dp[0][i] = 0;
		int cur = 0;
		while(q--) {
			int next = !cur;
			getline(cin, query);
			int id = distance(name, lower_bound(name, name + s, query));
			assert(id >= 0 && id < s);
			dp[next][id] = 1000000;
			for (int i=0; i<s; ++i) {
				if (i != id)
					dp[next][i] = min(dp[cur][i], dp[cur][id] + 1);
			}
			cur = next;
		}
		int best = 1000000;
		for (int i=0; i<s; ++i)
			best = min(best, dp[cur][i]);
		cout << "Case #" << x << ": " << best << endl;
	}
	return 0;
}
