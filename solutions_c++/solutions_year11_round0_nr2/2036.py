#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void add_opposed(char c, bool * opposed, vector<char> * opposing) {
	vector<char> & oppvec = opposing[c - 'A'];
	for (vector<char>::iterator it = oppvec.begin();
		it != oppvec.end();
		++it) {
		opposed[*it - 'A'] = true;
	}
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		char forms[26][26];
		vector<char> opposing[26];

		for (int i = 0; i < 26; ++i) {
			for (int j = 0; j < 26; ++j)
				forms[i][j] = 0;
		}

		int c;
		cin >> c;
		while (c--) {
			string form;
			cin >> form;
			forms[form[0] - 'A'][form[1] - 'A'] = form[2];
			forms[form[1] - 'A'][form[0] - 'A'] = form[2];
		}
		int d;
		cin >> d;
		while (d--) {
			string opposing_str;
			cin >> opposing_str;
			opposing[opposing_str[0] - 'A'].push_back(opposing_str[1]);
			opposing[opposing_str[1] - 'A'].push_back(opposing_str[0]);
		}
		int n;
		string action;
		cin >> n;
		bool opposed[26];
		for (int i = 0; i < 26; ++i)
			opposed[i] = false;
		cin >> action;
		vector<char> elements;
		for (int i = 0; i < n; ++i) {
			char new_elem;
			if (!elements.empty() && (new_elem = forms[action[i] - 'A'][elements.back() - 'A'])) {
				elements.pop_back();
				for (int i = 0; i < 26; ++i) {
					opposed[i] = false;
				}
				for (int i = 0; i < elements.size(); ++i) {
					add_opposed(elements[i], opposed, opposing);
				}
				elements.push_back(new_elem);
			} else {
				elements.push_back(action[i]);
			}
			if (opposed[elements.back() - 'A']) {
				elements.clear();
				for (int i = 0; i < 26; ++i) {
					opposed[i] = false;
				}
				continue;
			}
			add_opposed(elements.back(), opposed, opposing);
		}
		cout << "Case #" << t << ": [";
		if (!elements.empty())
			cout << elements[0];
		for (int i = 1; i < elements.size(); ++i) {
			cout << ", " << elements[i];
		}
		cout << "]" << endl;
	}
}
