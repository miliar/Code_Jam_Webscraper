#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int C;
		cin >> C;
		
		vector<string> combine;
		for (int i = 0; i < C; i++) {
			string str;
			cin >> str;
			combine.push_back(str);
		}

		int D;
		cin >> D;

		vector<string> destroy;
		for (int i = 0; i < D; i++) {
			string str;
			cin >> str;
			destroy.push_back(str);
		}

		int N;
		cin >> N;
		vector<char> ret;
		for (int i = 0; i < N; i++) {
			char ch;
			cin >> ch;
				
			ret.push_back(ch);
			// cout << "ret: " << ret << endl;
			
			int sz = ret.size();
			if (sz == 1) continue;
			
			int found = 0;
			int cycle = 1;
			while (cycle) {
				cycle = 0;

				for (int j = 0; j < (int)combine.size(); j++) {
					if (combine[j][0] == ret[sz - 2] && combine[j][1] == ret[sz - 1] ||
						combine[j][0] == ret[sz - 1] && combine[j][1] == ret[sz - 2]) {
						found = 1;
						
						ret.pop_back();
						ret.pop_back();
						ret.push_back(combine[j][2]);
						sz--;

						if (sz > 1) cycle = 1;
						break;
					}
				}
			}
			if (!found) {
				int done = 0;
				for (int j = 0; j < (int)destroy.size(); j++) {
					for (int p = 0; p < sz - 1; p++) {
						if (destroy[j][0] == ret[p] && destroy[j][1] == ret[sz - 1] ||
						    destroy[j][0] == ret[sz - 1] && destroy[j][1] == ret[p]) {
							ret.clear();
							done = 1;
							break;
						}
					}
					if (done) break;
				}
			}

			// cout << "ret: " << ret << endl;
		}

		cout << "Case #" << t << ": [";
		for (int i = 0; i < (int)ret.size(); i++) {
			if (i > 0) cout << ", ";
			cout << ret[i];
		}
		cout << "]" << endl;
	}

	return 0;
}

