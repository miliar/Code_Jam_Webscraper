#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <iomanip>
#include <algorithm>

using namespace std;

std::ostream& outCase(unsigned int tc) {
	std::cout << "Case #" << (tc + 1) << ": ";
	return std::cout;
}

void assert(bool test) {
	if (!test) {
		int a = 0;
	}
}

#define PAIR(c1, c2)	((((unsigned int)(c1)) << 8) | ((unsigned int)(c2)))

void testCase() {
	unsigned int C; cin >> C;
	map<unsigned int, char> comb;
	map<char, set<char> > oppo;
	for (unsigned int i = 0; i < C; ++i) {
		string s; cin >> s;
		comb[PAIR(s[0], s[1])] = s[2];
		comb[PAIR(s[1], s[0])] = s[2];
	}
	unsigned int D; cin >> D;
	for (unsigned int i = 0; i < D; ++i) {
		string s; cin >> s;
		oppo[s[0]].insert(s[1]);
		oppo[s[1]].insert(s[0]);
	}

	unsigned int N; cin >> N;
	string word; cin >> word;
	vector<char> lst;
	lst.push_back(word[0]);
	for (unsigned int i = 1; i < N; ++i) {
		char c = word[i];
		
		if (!lst.empty()) {
			map<unsigned int, char>::iterator it = comb.find(PAIR(*lst.rbegin(), c));
			if (it != comb.end()) {
				*lst.rbegin() = it->second;
				continue;
			}
		}

		set<char>& op = oppo[c];
		for (vector<char>::const_iterator it = lst.begin(); it != lst.end(); ++it) {
			if (op.find(*it) != op.end()) {
				lst.clear();
				goto _continue;
			}
		}

		lst.push_back(c);

_continue:
		;
	}

	cout << "[";
	if (!lst.empty()) {
		cout << lst[0];
	}
	for (unsigned int i = 1; i < lst.size(); ++i) {
		cout << ", " << lst[i];
	}
	cout << "]" << endl;
}

int main() {
	unsigned int T; cin >> T;
	for (unsigned int t = 0; t < T; ++t) {		
		outCase(t);
		testCase();		
	}

	return 0;
}