#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
#include <sstream>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 0; t < T; t++) {
		int C; int D; int N;
		cin >> C;
		// combine
		map<string,string> combines;
		for (int i = 0; i < C; i++) {
			string base; cin >> base;
			string sub = base.substr(0,2);
			combines.insert(make_pair(sub, base.substr(2)));
			reverse(sub.begin(),sub.end());
			combines.insert(make_pair(sub, base.substr(2)));
		}
		// destroy
		cin >> D;
		map<char,set<char> > destroy;
		for (int i = 0; i < D; i++) {
			string des; cin >> des;
			char ch = des[0];
			char ch2 = des[1];
			destroy[ch].insert(ch2);
			destroy[ch2].insert(ch);
		}
		cin >> N;
		// input
		string line; cin >> line;
		string output;
		for (int i = 0; i < line.size(); i++) {
			if (i == 0) {
				output += line[i];
				continue;
			}
			output += line[i];
			if (output.size() >= 2) {
				string b = output.substr(output.size()-2, 2);
				if (combines.count(b) != 0) {
					// combines
					output = output.substr(0, output.size()-2) + combines[b];
				}
				// check for destroy
				char lastChar = output[output.size()-1];
				bool gone = false;
				for (int j = 0; j < output.size()-1; j++) {
					if (destroy[lastChar].count(output[j]) != 0) {
						gone = true;
						break;
					}
				}
				if (gone) output = "";
			}
		}
		cout << "Case #" << t+1 << ": [";
		for (int i = 0; i < output.size(); i++) {
			if (i != 0) cout << ", ";
			cout << output[i];
		}
		cout << "]\n";
	}
	return 0;
}