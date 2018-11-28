#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector <int> invoke() {
	int combine[26][26];
	int opposed[26][26];
	for (int i = 0; i < 26; i++) for (int j = 0; j < 26; j++) combine[i][j] = -1;
	for (int i = 0; i < 26; i++) for (int j = 0; j < 26; j++) opposed[i][j] = 0;
	int C;
	cin >> C;
	string x;
	for (int i = 0; i < C; i++) {
		cin >> x;
		combine[x[0] - 'A'][x[1] - 'A'] = x[2] - 'A';
		combine[x[1] - 'A'][x[0] - 'A'] = x[2] - 'A';
	}
	int D;
	cin >> D;
	for (int i = 0; i < D; i++) {
		cin >> x;
		opposed[x[0] - 'A'][x[1] - 'A'] = 1;
		opposed[x[1] - 'A'][x[0] - 'A'] = 1;
	}
	int N;
	cin >> N;
	cin >> x;
	vector <int> res;
	res.clear();
	for (int i = 0; i < x.size(); i++) {
		res.push_back(x[i] - 'A');
		int k = res.size();
		if (k < 2) continue;
		if (combine[res[k - 1]][res[k - 2]] >= 0) {
			res[k - 2] = combine[res[k - 1]][res[k - 2]];
			res.pop_back();
			continue;
		}
		for (int j = 0; j + 1 < k; j++) {
			if (opposed[res[k - 1]][res[j]]) {
				res.clear();
				break;
			}
		}
	}
	return res;
}

int main(int argc, char *argv[]) {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		vector <int> res = invoke();
		cout << "Case #" << i << ": [";
		for (int j = 0; j < res.size(); j++) {
			if (j > 0) cout << ", ";
			cout << (char)(res[j] + 'A');
		}
		cout << "]" << endl;
	}
	return 0;
}

