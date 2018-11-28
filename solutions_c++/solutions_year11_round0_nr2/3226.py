#include <iostream>
#include <set>
#include <map>
#include <vector>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int C, D, N;
		map<pair<char, char>, char> combinations;
		map<char, vector<char> > annihlations;
		map<char, int> current;
		vector<char> ans;
		
		cin >> C;
		for (int i = 0; i < C; i++) {
			char a, b, c;
			cin >> a >> b >> c;
			combinations[pair<char, char>(a, b)] = c;
			combinations[pair<char, char>(b, a)] = c;
		}
		
		cin >> D;
		for (int i = 0; i < D; i++) {
			char a, b;
			cin >> a >> b;
			annihlations[a].push_back(b);
			annihlations[b].push_back(a);
		}
		
		cin >> N;
		for (int i = 0; i < N; i++) {
			char a;
			cin >> a;
			if (ans.size() && combinations[pair<char, char>(ans[ans.size()-1], a)]) {
				current[ans[ans.size()-1]]--;
				ans[ans.size()-1] = combinations[pair<char, char>(ans[ans.size()-1], a)];
				current[ans[ans.size()-1]]++;
			}
			else {
				ans.push_back(a);
				current[a]++;
				vector<char>::iterator e = annihlations[a].end();
				for (vector<char>::iterator i = annihlations[a].begin(); i != e; i++) if (current[*i]) {
					current.clear();
					ans.clear();
					break;
				}
			}
		}
		
		cout << "Case #" << t+1 << ": [";
		for (int i = 0; i < ans.size(); i++) {
			if (i != 0) cout << ", ";
			cout << ans[i];
		}
		cout << "]\n";
	}
	return 0;
}
