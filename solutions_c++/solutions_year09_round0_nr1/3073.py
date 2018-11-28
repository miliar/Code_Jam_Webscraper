#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
	ifstream in("A-large.in");
	ofstream out("A.out");

	vector<string> dic;

	int L, D, N;

	in >> L >> D >> N;

	for (int i = 0; i < D; i++) {
		string word;
		in >> word;
		dic.push_back(word);
	}

	for (int i = 0; i < N; i++) {
		string tmp;
		in >> tmp;
		vector<vector<int> > pattern;
		int j = 0;
		while (j != tmp.size()) {
			vector<int> lets(26, 0);
			if (tmp[j] == '(') {
				j++;
				while (tmp[j] != ')') {
					lets[tmp[j] - 'a'] = 1;
					j++;
				}
			} else {
				lets[tmp[j] - 'a'] = 1;
			}
			pattern.push_back(lets);
			j++;
		}

		int res = 0;

		for (int j = 0 ; j < D; j++) {
			bool is = 1;
			for (int k = 0; k < dic[j].size(); k++) {
				if (pattern[k][dic[j][k] - 'a'] != 1) { is = 0; break; }
			}
			if (is) res++;
		}

		out << "Case #" << i + 1 << ": " << res << endl;
	}

	return 0;
}
