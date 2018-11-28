#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int main() {
	ifstream in("B.in");
	ofstream out("B.out");

	int tests;
	in >> tests;
	for (int test = 1; test <= tests; ++test) {
		out << "Case #" << test << ": ";

		map<pair<char, char>, char> combos;

		int combinations;
		in >> combinations;
		while (combinations--) {
			string combo;
			in >> combo;
			combos[make_pair(combo[0], combo[1])] = combo[2];
			combos[make_pair(combo[1], combo[0])] = combo[2];
		}

		map<char, vector<char> > opposes;

		int opposers;
		in >> opposers;
		while (opposers--) {
			string oppose;
			in >> oppose;
			opposes[oppose[0]].push_back(oppose[1]);
			opposes[oppose[1]].push_back(oppose[0]);
		}

		int length;
		string spell;
		in >> length >> spell;

		map<char, int> elements;
		vector<char> magic;
		for (int i = 0; i < length; i++) {
			if (magic.size() > 0 && combos.find(make_pair(*magic.rbegin(), spell[i])) != combos.end()) {
				elements[*magic.rbegin()]--;
				*magic.rbegin() = combos[make_pair(*magic.rbegin(), spell[i])];
				elements[*magic.rbegin()]++;
			} else {
				bool clear = false;
				for (int j = 0; j < opposes[spell[i]].size(); ++j) {
					if (elements[opposes[spell[i]][j]] > 0) {
						elements.clear();
						magic.clear();
						clear = true;
						break;
					}
				}
				if (!clear) {
					magic.push_back(spell[i]);
					elements[*magic.rbegin()]++;
				}
			}
		}

		out << "[";
		for (int i = 0; i < (int)magic.size() - 1; ++i) {
			out << magic[i] << ", ";
		}
		if (magic.size() > 0) {
			out << *magic.rbegin();
		}
		out << "]" << endl;
	}
}