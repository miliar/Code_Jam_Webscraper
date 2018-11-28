#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;

int T, C, D, N;
map< pair<char,char>, char > combined;
map<char, char> opposed;
vector<char> el;
multiset<char> blacklist;

int main() {
	
	cin >> T;
	string tmp;
	pair<char, char> coppia;
	for (int i = 1; i <= T; i++)
	{
		// RESET
		opposed.clear();
		combined.clear();
		blacklist.clear();
		el.clear();
		// Reading input
		cin >> C;
		for (int j = 0; j < C; j++)
		{
			cin >> tmp;
			combined[ make_pair( min(tmp[0], tmp[1]), max(tmp[0], tmp[1]) ) ] = tmp[2];
		}
		cin >> D;
		for (int j = 0; j < D; j++)
		{
			cin >> tmp;
			opposed[tmp[0]] = tmp[1];
			opposed[tmp[1]] = tmp[0];
		}
		cin >> N >> tmp;

		// Here starts the main algorithm
		el.push_back(tmp[0]);
		if ( opposed.count(el[0]) ) blacklist.insert(opposed[el[0]]);
		for (int j = 1; j < N; j++)
		{
			el.push_back(tmp[j]);
			while (el.size() > 1) {
				coppia = make_pair( min(el[el.size()-1], el[el.size()-2]), max(el[el.size()-1], el[el.size()-2]) );
				if ( combined.count(coppia) ) {
					if ( opposed.count(el.back()) ) {
						int erased = blacklist.erase(opposed[el.back()]);
						for (int k = 1; k < erased; k++) blacklist.insert(opposed[el.back()]);
					}
					el.pop_back();
					if ( opposed.count(el.back()) ) {
						int erased = blacklist.erase(opposed[el.back()]);
						for (int k = 1; k < erased; k++) blacklist.insert(opposed[el.back()]);
					}
					el[el.size()-1] = combined[coppia];
				}
				else break;
			}
			if ( opposed.count(el.back()) ) blacklist.insert(opposed[el.back()]);
			if ( blacklist.count(el.back()) ) {
				el.clear();
				blacklist.clear();
			}
				
		}
		cout << "Case #" << i << ": [";
		for (int f= 0; f < (signed int)el.size()-1; f++)
		{
			cout << el[f] << ", ";
		}
		if (el.size() >= 1) cout << el.back();
		cout << "]" << endl;
	}
	
	return 0;
}
