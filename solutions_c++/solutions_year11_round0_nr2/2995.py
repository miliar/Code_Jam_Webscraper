#include <vector>
#include <string>
#include <iostream>

#include <hash_map>


using namespace std;
using namespace stdext;


char space;
int main () {
	int cases;
	cin >> cases;

	for (int i = 1; i <= cases; ++i) {
		int com;
		hash_map<char, char> com_map;
		hash_map<char, char> com_value;
		cin >> com;
		for (int j = 0; j < com; ++j) {
			char c1, c2, c3;
			cin >> c1 >> c2 >> c3;
			com_map.insert(make_pair(c1, c2));
			com_map.insert(make_pair(c2, c1));
			com_value.insert(make_pair(c1, c3));
			com_value.insert(make_pair(c2, c3));
		}

		int opp;
		hash_map<char, char> opp_map;
		cin >> opp;
		for (int j = 0; j < opp; ++j) {
			char c1, c2;
			cin >> c1 >> c2;
			opp_map.insert(make_pair(c1, c2));
			opp_map.insert(make_pair(c2, c1));
		}

		int invokes;
		vector<char> invoke_list;
		cin >> invokes;
		for (int j = 0; j < invokes; ++j) {
			char c;
			cin >> c;

			bool inserted = false;
			while (!invoke_list.empty()) {
				// combined
				hash_map<char, char>::const_iterator k1 = com_map.find(c);
				if (k1 == com_map.end() || k1->second != invoke_list.back()) {
					break;
				}
				invoke_list.pop_back();
				c = com_value.find(c)->second;
			}

			// opposed
			hash_map<char, char>::const_iterator k2 = opp_map.find(c);
			if (k2 != opp_map.end()) {
				for (vector<char>::const_iterator m = invoke_list.begin(); m != invoke_list.end(); ++m) {
					if (*m == k2->second) {
						invoke_list.clear();
						inserted = true;
						break;
					}
				}
			}

			// insert
			if (!inserted)
				invoke_list.push_back(c);
		}

		// output
		cout << "Case #" << i << ": [";
		for(vector<char>::const_iterator j = invoke_list.begin(); j != invoke_list.end();) {
			cout << *j;
			if (++j != invoke_list.end())
				cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}