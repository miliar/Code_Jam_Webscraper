
#include <set>
#include <map>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <cassert>
#include <iostream>
#include <algorithm>
using namespace std;

string next() {
	string res;
	cin >> res;
	return res;
}

int parseInt(string s) {
	int res;
	sscanf(s.c_str(), "%d", &res);
	return res;
}

int main() {
	int testsCount = parseInt(next());
	for (int test = 0; test < testsCount; ++test) {
		map<pair<char, char>, char> combinable;
		int combinableCount = parseInt(next());
		for (int i = 0; i < combinableCount; ++i) {
			string s = next();
			assert(s.size() == 3);
			assert(!combinable.count(make_pair(s[0], s[1])));
			assert(!combinable.count(make_pair(s[1], s[0])));
			combinable[make_pair(s[0], s[1])] = s[2];
			combinable[make_pair(s[1], s[0])] = s[2];
		}
		set<pair<char, char> > opposable;
		int opposableCount = parseInt(next());
		for (int i = 0; i < opposableCount; ++i) {
			string s = next();
			assert(s.size() == 2);
			assert(!opposable.count(make_pair(s[0], s[1])));
			assert(!opposable.count(make_pair(s[1], s[0])));
			opposable.insert(make_pair(s[0], s[1]));
			opposable.insert(make_pair(s[1], s[0]));
		}
		int operationsCount = parseInt(next());
		string operations = next();
		vector<char> stk;
		for (int i = 0; i < operationsCount; ++i) {
			stk.push_back(operations[i]);
			if (stk.size() > 1) {
				char last = stk[stk.size() - 1];
				char prelast = stk[stk.size() - 2];
				if (combinable.count(make_pair(last, prelast))) {
					char combined = combinable[make_pair(last, prelast)];
					stk.pop_back();
					stk.pop_back();
					stk.push_back(combined);
				} else {
					for (int j = 0; j < int(stk.size()) - 1; ++j)
						if (opposable.count(make_pair(stk[stk.size() - 1], stk[j]))) {
							stk = vector<char>();
							break;
						}
				}
			}
		}
		printf("Case #%d: [", test + 1);
		for (int i = 0; i < int(stk.size()); ++i) {
			putchar(stk[i]);
			if (i + 1 < int(stk.size()))
				printf(", ");
		}
		puts("]");
	}
	return 0;
}