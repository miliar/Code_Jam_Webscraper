#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int t,n,m;
	cin >> t;
	vector<string> dir;
	string line;
	for (int caseno = 1; caseno <= t; caseno++) {
		dir.clear();
		cin >> n >> m;
// 		cout << "part 1" << endl;
		for (int i = 0; i < n; i++) {
			cin >> line;
			for (int k = 1; k <= line.size(); k++) {
				if (line[k] == '/' || k == line.size()) {
					bool found = false;
					string temp(line,0,k);
					for (int l = 0; l < dir.size() && !found; l++) {
						if (dir[l] == temp)
							found = true;
					}
					if (!found) {
						dir.push_back(temp);
// 						cout << temp << endl;
					}
				}
			}
		}
		int ans = 0;
// 		cout << "part 2" << endl;
		for (int i = 0; i < m; i++) {
			cin >> line;
			for (int k = 1; k <= line.size(); k++) {
				if (line[k] == '/' || k == line.size()) {
					bool found = false;
					string temp(line,0,k);
					for (int l = 0; l < dir.size() && !found; l++) {
						if (dir[l] == temp)
							found = true;
					}
					if (!found) {
						dir.push_back(temp);
						ans++;
// 						cout << temp << endl;
					}
				}
			}
		}
		
		cout << "Case #" << caseno << ": " << ans << endl;
	}
}