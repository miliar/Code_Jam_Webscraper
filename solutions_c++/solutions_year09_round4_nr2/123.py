#include <cstdio>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>

using namespace std;

map <pair <pair <int, int>, string>, int> dp;

int move(int x, int y, string current, vector <string> &cave, int F);

int fall(int x, int y, int f, string current, vector <string> &cave, int F)
{
	if (f > F) {
		return 1 << 29;
	}
	if (y >= (int)cave.size() - 1 || cave[y + 1][x] == '#') {
		return move(x, y, current, cave, F);
	}
	return fall(x, y + 1, f + 1, cave[y + 1], cave, F);
}

int move(int x, int y, string current, vector <string> &cave, int F)
{
	if (y >= (int)cave.size() - 1) {
		return 0;
	}
	pair <pair <int, int>, string> key(make_pair(x, y), current);
	if (dp.find(key) != dp.end()) {
		return dp[key];
	}
	int ret = 1 << 29;
	int left = x;
	for (int i = x; i >= 0; i--) {
		if (current[i] == '#' || cave[y + 1][i] == '.') {
			break;
		}
		left = i;
	}
	int right = x;
	for (int i = x; i < current.size(); i++) {
		if (current[i] == '#' || cave[y + 1][i] == '.') {
			break;
		}
		right = i;
	}
	for (int l = left + 1; l <= right; l++) {
		for (int r = l; r <= right; r++) {
			string next = cave[y + 1];
			for (int i = l; i <= r; i++) {
				next[i] = '.';
			}
			ret = min(ret, (r - l + 1) + fall(l, y + 1, 1, next, cave, F));
		}
	}
	for (int r = left; r <= right - 1; r++) {
		for (int l = left; l <= r; l++) {
			string next = cave[y + 1];
			for (int i = l; i <= r; i++) {
				next[i] = '.';
			}
			ret = min(ret, (r - l + 1) + fall(r, y + 1, 1, next, cave, F));
		}
	}
	if (left > 0 &&
	    current[left - 1] == '.' && cave[y + 1][left - 1] == '.') {
		ret = min(ret, fall(left - 1, y + 1, 1, cave[y + 1], cave, F));
	}
	if (right < (int)current.size() - 1 &&
	    current[right + 1] == '.' && cave[y + 1][right + 1] == '.') {
		ret = min(ret, fall(right + 1, y + 1, 1, cave[y + 1], cave, F));
	}

	return dp[key] = ret;
}


string ADiggingProblem(vector <string> cave, int F)
{
	dp.clear();
	int dig = move(0, 0, cave[0], cave, F);
	if (dig >= 1 << 29) {
		return "No";
	}
	stringstream ss;
	ss << "Yes " << dig;
	return ss.str();
}

int main()
{
	string line;

	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int R, C, F;
		cin >> R >> C >> F;
		vector <string> cave(R);
		for (int i = 0; i < R; i++) {
			cin >> cave[i];
		}

		string ret = ADiggingProblem(cave, F);

		cout << "Case #" << caseno << ": " << ret << endl;
	}

	return 0;
}
