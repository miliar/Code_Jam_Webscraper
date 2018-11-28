#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <set>
#include <sstream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, M; cin >> N >> M;
		set<string> built;
		for (int j = 0; j < N; j++) {
			string dir; cin >> dir;
			built.insert(dir);
		}
		int total = 0;
		for (int j = 0; j < M; j++) {
			string need; cin >> need;
			//cout << "need: " << need << "\n";
			if (built.count(need) != 0) continue;
			vector<string> paths;
			for (int k = 0; k < need.size(); k++) if (need[k] == '/') need[k] = ' ';
			istringstream iss(need);
			//cout << "need: " << need << "\n";
			string str;
			while (iss >> str) paths.push_back(str);
			str = "/";
			for (int k = 0; k < paths.size(); k++) {
				str += paths[k];
				if (built.count(str) == 0) {
					//cout << "add: " << str << "\n";
					built.insert(str);
					total++;
					for (int m = k+1; m < paths.size(); m++) {
						str = str + "/" + paths[m];
						//cout << "add: "  << str << "\n";
						built.insert(str);
						total++;
					}
					break;
				}
				if (k != paths.size()-1) str += "/";
			}
		}
		cout << "Case #" << (i+1) << ": " << total << "\n";
	}
	return 0;
}