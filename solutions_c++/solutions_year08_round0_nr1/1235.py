#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main() {
	int n;
	int casenum = 1;
	cin >> n;

	while (n--) {
		int S, id = 0;
		cin >> S;

		map<string, int> engines;
		vector<bool> used = vector<bool>(S, false);
		string name;

		getline(cin, name);
		while (S--) {
			getline(cin, name);
			engines[name] = id++;
		}

		int Q;
		string query;
		int answer = 0, canuse = engines.size();
		cin >> Q;
		getline(cin, query);

		while (Q--) {
			getline(cin, query);
			id = engines[query];
			if (!used[id]) {
				used[id] = true;
				canuse--;
			}

			if (canuse == 0) {
				answer++;
				canuse = engines.size()-1;
				used = vector<bool>(engines.size(), false);
				used[id] = true;
			}
		}

		cout << "Case #" << casenum++ << ": " << answer << endl;
	}
}
