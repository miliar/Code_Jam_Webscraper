#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
using namespace std;

typedef long long ll;

void move_robot(int& pos, int next) {
	if (next == -1)
		;
	else if (pos < next)
		++pos;
	else if (pos > next)
		--pos;
}

string solve() {
	int N;
	vector<pair<char, int> > seq;
	cin >> N;
	for (int i = 0; i < N; ++i) {
		char c[10];
		int x;
		cin >> c >> x;
		seq.push_back(make_pair(c[0], x));
	}
	int pO = 1, pB = 1, ans = 0;
	for (int i = 0; i < N; ++i) {
		int nextO = -1, nextB = -1;
		for (int j = i; j < N; ++j) {
			if (nextO == -1 && seq[j].first == 'O') nextO = seq[j].second;
			if (nextB == -1 && seq[j].first == 'B') nextB = seq[j].second;
		}
		while (seq[i].first == 'O' && nextO != pO
				|| seq[i].first == 'B' && nextB != pB) {
			++ans;
			move_robot(pO, nextO);
			move_robot(pB, nextB);
		}
		if (seq[i].first == 'O') {
			++ans;
			// press O
			move_robot(pB, nextB);
		} else {
			++ans;
			move_robot(pO, nextO);
			// press B
		}
	}
	ostringstream ret;
	ret << ans;
	return ret.str();
}

int main(int argc, char* argv[]) {
    if (argc > 1) {
        char* file_name = argv[1];
        int len = strlen(file_name);
        if (strcmp(file_name + len - 3, ".in") == 0)
            file_name[len - 3] = 0;
        else if (strcmp(file_name + len - 1, ".") == 0)
            file_name[len - 1] = 0;
        freopen((string(file_name) + ".in").c_str(), "r", stdin);
        freopen((string(file_name) + ".out").c_str(), "w", stdout);
    }
    int cc = 0, ccc = 0;
    for (cin >> ccc; cc < ccc; ++cc)
            cout << "Case #" << cc + 1 << ": " << solve() << endl;
    return 0;
}
