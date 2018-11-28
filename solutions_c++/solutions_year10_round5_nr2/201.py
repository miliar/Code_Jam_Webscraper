#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

typedef unsigned long long big;

struct board {
	big length;
	big cost;
	board(big l, big c) : length(l), cost(c) { }
};

bool operator<(board a, board b) {
	return make_pair(a.length, a.cost) < make_pair(b.length, b.cost);
}
bool operator>(board a, board b) {
	return b < a;
}


big tgt;
int nboards;

vector<board> boards;

void add_boards(big len) {
	big k = 1;
	while (len < tgt) {
		boards.push_back(board(len, k));
		len *= 2;
		k *= 2;
	}
}

	


int main() {
	int ncases;
	cin >> ncases;
	for (int caseno = 1; caseno <= ncases; caseno++) {
		boards.clear();
		cin >> tgt >> nboards;
		for (int i = 0; i < nboards; i++) {
			big len;
			cin >> len;
			add_boards(len);
		}
		sort(boards.begin(), boards.end(), greater<board>());

		vector<big> low(boards.size() + 1);
		low[boards.size()] = tgt;
		for (int i = boards.size() - 1; i >= 0; --i)
			low[i] = low[i + 1] < boards[i].length ? 0 : low[i + 1] - boards[i].length;


		vector<pair<big, big> > dp;
		dp.push_back(make_pair(0, 0));
		for (int i = 0; i < boards.size(); i++) {
			vector<pair<big, big> > k;
			for (vector<pair<big, big> >::iterator it = lower_bound(dp.begin(), dp.end(), pair<big, big>(low[i], 0)); it != dp.end(); ++it) {
				if (it->first + boards[i].length > tgt) break;
				k.push_back(make_pair(it->first + boards[i].length, it->second + boards[i].cost));
			}
			vector<pair<big, big> > k2;
			k2.reserve(dp.size() + k.size());
			k2.swap(dp);

			vector<pair<big, big> >::iterator it1 = k.begin(), it2 = k2.begin();

			while (it1 != k.end() && it2 != k2.end()) {
				if (it1->first == it2->first) {
					if (it1->second < it2->second) { ++it2; continue; }
					++it1; continue;
				}
				if (it1->first < it2->first) dp.push_back(*it1++);
				else dp.push_back(*it2++);
			}
			while (it1 != k.end()) dp.push_back(*it1++);
			while (it2 != k2.end()) dp.push_back(*it2++);
		}

		cout << "Case #" << caseno << ": ";
		if (dp.back().first == tgt) cout << dp.back().second;
		else cout << "IMPOSSIBLE";
		cout << endl;

	}
	return 0;
}
