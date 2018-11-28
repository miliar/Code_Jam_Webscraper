#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>
#include <cstring>
#include <string>
#include <functional>
#include <numeric>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()

const int INF = ((1 << 31) - 1);
const long long LLINF = (((1LL << 63) - 1LL));
const double eps = 1e-9;
const double PI = 3.14159265358979323846;

typedef long long ll;

void explode(vector<char> & list, const vector<string> & explode_rules) {
	vector<bool> was(26, false);
	for (int i = 0; i < list.size(); ++i)
		was[list[i] - 'A'] = true;
	for (int i = 0; i < explode_rules.size(); ++i)
		if (was[explode_rules[i][0] - 'A'] &&
			was[explode_rules[i][1] - 'A']) {
				list.clear();
				return;
		}
}

void append(vector<char> & list, char ch, const vector<string> & adding_rules, const vector<string> & explode_rules) {
	list.push_back(ch);
	if (list.size() < 2)
		return;
	for (int i = 0; i < adding_rules.size(); ++i) {
		if (list[list.size() - 2] == adding_rules[i][0] &&
			list[list.size() - 1] == adding_rules[i][1] ||
			list[list.size() - 2] == adding_rules[i][1] &&
			list[list.size() - 1] == adding_rules[i][0]) {
				list.pop_back();
				list.pop_back();
				append(list, adding_rules[i][2], adding_rules, explode_rules);
				return;
		}
	}
}

void outList(vector<char> v) {
	cout << "[";
	for (int i = 0; i < v.size(); ++i) {
		cout << v[i];
		if (i + 1 < v.size())
			cout << ", ";
	}
	cout << "]";
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	cin >> tests;
	for (int test = 0; test < tests; ++test) {
		cerr << test << " from " << tests << " completed!\n";
		vector<char> list;
		int amount_of_adding_rules;
		cin >> amount_of_adding_rules;
		vector<string> adding_rules(amount_of_adding_rules);
		for (int i = 0; i < amount_of_adding_rules; ++i)
			cin >> adding_rules[i];
		int amount_of_explode_rules;
		cin >> amount_of_explode_rules;
		vector<string> explode_rules(amount_of_explode_rules);
		for (int i = 0; i < amount_of_explode_rules; ++i) {
			cin >> explode_rules[i];
			assert(explode_rules[i][0] != explode_rules[i][1]);
		}
		int len;
		cin >> len;
		string s;
		cin >> s;
		for (int i = 0; i < len; ++i) {
			append(list, s[i], adding_rules, explode_rules);
			explode(list, explode_rules);
		}
		cout << "Case #" << test + 1 << ": ";
		outList(list);
		cout << "\n";
	}
	return 0;
}