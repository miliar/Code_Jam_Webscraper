#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>
using namespace std;

int main() {
	ifstream cin("B-large.in");
	ofstream cout("B-large.out");
	int T;
	cin >> T;
	for (int cc = 1; cc <= T; cc++) {
		cout << "Case #" << cc << ": ";
		string list;
		map<pair<char, char>, char> merge;
		set<pair<char, char> > conf;
		int C;
		cin >> C;
		while (C--) {
			char a, b, c;
			cin >> a >> b >> c;
			merge[make_pair(a, b)] = c;
			merge[make_pair(b, a)] = c;
		}

		int D;
		cin >> D;
		while (D--) {
			char a, b;
			cin >> a >> b;
			conf.insert(make_pair(a,b));
			conf.insert(make_pair(b,a));
		}

		int N;
		cin >> N;
		while(N--) {
			char t;
			cin >> t;
			if (list.size() == 0)
				list += t;
			else {
				if (merge.count(make_pair(t, list[list.size()-1]))) {
					char nn = merge[make_pair(t, list[list.size()-1])];
					list.pop_back();
					list += nn;
				} else {
					bool co = false;
					for (int i = 0; i < list.size(); i++) {
						if (conf.count(make_pair(t, list[i])))
							co = true;
					}

					if (co)
						list.clear();
					else
						list += t;
				}
			}
		}

		cout << "[";
		if (list.size()) {
			cout << list[0];
			for (int i = 1; i < list.size(); i++)
				cout << ", " << list[i];
		}
		cout << "]" << endl;
	}
	return 0;
}