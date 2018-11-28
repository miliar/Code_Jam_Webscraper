#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

// The Killer Word

int doit(vector <string> dict, int index, string order)
{
	vector <bool> possible(dict.size(), true);
	vector <vector <int> > hist(dict.size(), vector <int> (26, 0));
	for (int i = 0; i < dict.size(); i++) {
		for (int j = 0; j < dict[i].size(); j++) {
			hist[i][dict[i][j] - 'a']++;
		}
		if (dict[i].size() != dict[index].size()) {
			possible[i] = false;
		}
	}
	int ret = 0;
	for (int i = 0; i < order.size(); i++) {
		bool flag = false;
		for (int j = 0; j < dict.size(); j++) {
			if (possible[j] && hist[j][order[i] - 'a'] > 0) {
				flag = true;
			}
		}
		if (!flag) {
			continue;
		}
		if (hist[index][order[i] - 'a'] == 0) {
			ret++;
		}
		for (int j = 0; j < dict.size(); j++) {
			if (possible[j]) {
				for (int k = 0; k < dict[j].size(); k++) {
					if (dict[index][k] == order[i] && dict[j][k] != order[i] ||
					    dict[index][k] != order[i] && dict[j][k] == order[i]) {
						possible[j] = false;
					}
				}
			}
		}
	}
	return ret;
}

string TheKillerWord(vector <string> dict, string order)
{
	int bestpoint = -1;
	int bestindex = 0;
	for (int i = 0; i < dict.size(); i++) {
		int point = doit(dict, i, order);
		if (point > bestpoint) {
			bestindex = i;
			bestpoint = point;
		}
	}
	return dict[bestindex];
}

int main()
{
	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int N, M;
		cin >> N >> M;
		vector <string> dict(N);
		for (int i = 0; i < N; i++) {
			cin >> dict[i];
		}
		cout << "Case #" << caseno << ":";
		for (int i = 0; i < M; i++) {
			string order;
			cin >> order;
			cout << " " << TheKillerWord(dict, order);
		}
		cout << endl;
	}

	return 0;
}
