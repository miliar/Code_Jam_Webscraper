#include <iostream>
#include <string>

using namespace std;

int T;
int main() {
	cin >> T;
	for (int t = 1; t <= T; t ++) {
		int combine[256][256];
		memset(combine, -1, sizeof(combine));
		int C;
		cin >> C;
		for (int i = 0; i < C; i ++) {
			string s;
			cin >> s;
			combine[s[0]][s[1]] = combine[s[1]][s[0]] = s[2];
		}
		bool oppose[256][256];
		memset(oppose, 0, sizeof(oppose));
		int D;
		cin >> D;
		for (int i = 0; i < D; i ++) {
			string s;
			cin >> s;
			oppose[s[0]][s[1]] = oppose[s[1]][s[0]] = true;
		}
		int N;
		cin >> N;
		string s;
		cin >> s;
		string res;
		for (int i = 0; i < N; i ++) {
			if (res.size() != 0 && combine[res.back()][s[i]] != -1) {
				res.back() = combine[res.back()][s[i]];
			} else {
				bool opposed = false;
				for (int j = 0; j < res.size(); j ++) {
					if (oppose[res[j]][s[i]]) {
						res = "";
						opposed = true;
						break;
					}
				}
				if (!opposed) {
					res += s[i];
				}
			}
		}
		cout << "Case #" << t << ": [";
		for (int i = 0; i < res.size(); i ++) {
			cout << res[i];
			if (i + 1 != res.size()) {
				cout << ", ";
			}
		}
		cout << "]\n";
	}
}