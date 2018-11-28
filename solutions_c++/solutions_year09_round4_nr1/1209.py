#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <cmath>
#include <set>

using namespace std;

#define mp make_pair

set<vector<long long> > seen;

int main() {
	int T; cin >> T;
	for (int i = 0; i < T; i++) {
		int N; cin >> N;
		char ch;
		seen.clear();
		vector<long long> vec;
		for (int j = 0; j < N; j++) {
			long long r = 0;
			int seen = 0;
			for (int k = 0; k < N; k++) {
				cin >> ch;
				if (ch == '1') {
					seen = k+1;
				}
			}
			//cout << "cost: " << seen << "\n";
			vec.push_back(seen);
		}
		queue<pair<int,vector<long long> > > q;
		q.push(mp(0,vec));
		while (!q.empty()) {
			//cout << "cost: " << q.front().first << "\n";
			//cout << "vec: "; for (int j = 0; j < q.front().second.size(); j++) cout << q.front().second[j] << " ";
			//cout << "\n";
			pair<int,vector<long long> > pp = q.front(); q.pop();
			vector<long long> vv = pp.second;
			if (seen.count(vv) != 0) continue;
			seen.insert(vv);
			bool ok = true;
			for (int j = 0; j < vv.size(); j++) {
				if (vv[j] > j+1) {
					ok = false;
					break;
				}
			}
			if (ok) {
				cout << "Case #" << i+1 << ": " << pp.first << "\n";
				break;
			}
			for (int j = 0; j+1 < vv.size(); j++) {
				//if (vv[j] >= (j+2) && vv[j+1] >= (j+1)) {
				//	continue;
				//}
				swap(vv[j],vv[j+1]);
				if (seen.count(vv) == 0) {
					q.push(mp(pp.first+1, vv));
				}
				swap(vv[j],vv[j+1]);
			}
		}
	}
	return 0;
}