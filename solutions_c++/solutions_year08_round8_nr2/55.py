#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <string>
#include <algorithm>

using namespace std;

int _id = 0;
map<string, int> colors;

int datac[400];
vector<pair<int, int> > data[400];

int id(const string& c) {
	if (colors.find(c) != colors.end())
		return colors[c];
	colors[c] = _id;
	return _id++;
}

int main() {
	int _tc; cin >> _tc;
	for (int _t = 1; _t <= _tc; _t++) {
		for (int i = 0; i < 400; i++) data[i].clear();
		colors.clear(); _id = 0;

		int res = 10000;
		int n; cin >> n;
		string s;
		for (int i = 0, ta, tb; i < n; i++) {
			cin >> s; datac[i] = id(s);
			cin >> ta >> tb;
			data[datac[i]].push_back(make_pair(ta, tb));
		}

		for (int c1 = 0; c1 <= _id; c1++) for (int c2 = 0; c2 <= _id + 1; c2++) for (int c3 = 0; c3 <= _id + 2; c3++) if (c1 != c2 && c1 != c3 && c2 != c3){
			int tres = 0;
			vector<pair<int, int> > pnts;
			pnts.insert(pnts.begin(), data[c1].begin(), data[c1].end());
			pnts.insert(pnts.begin(), data[c2].begin(), data[c2].end());
			pnts.insert(pnts.begin(), data[c3].begin(), data[c3].end());
			sort(pnts.begin(), pnts.end());
			int cur = 0, pos = 0;
			while (cur < 10000 && pos < pnts.size()) {
				int last = -1;
				while (pos < pnts.size() && pnts[pos].first <= cur + 1) {
					last = max(last, pnts[pos].second);
					pos++;
				}
				if (last == -1) break;
				cur = last; tres++;
			}

			if (cur == 10000) res = min(res, tres);
		}
		

		cout << "Case #" << _t << ": ";
		if (res > 1000) cout << "IMPOSSIBLE";
		else cout << res;
		cout << endl;
	}

	return 0;
}