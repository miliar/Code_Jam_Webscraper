#include <iostream>
#include <vector>
#include <map>
using namespace std;

bool findinvector(const vector<char> & v, char c) {
	for (int i = 0; i < v.size(); ++i) {
		if (v[i] == c) return true;
	}
	return false;
}

int main() {
	int t;
	cin >> t;
	for (int k = 0; k < t; ++k) {
		int na, nb, nc;
		string temp;
		vector<char> res;
		map<string, char> cb;
		map<char, char> op;
		cin >> na;
		for (int i = 0; i < na; ++i) {
			cin >> temp;
			cb[temp.substr(0, 2)] = temp[2];
			string str = "  ";
			str[0] = temp[1];
			str[1] = temp[0];
			cb[str] = temp[2];
		}
		cin >> nb;
		for (int i = 0; i < nb; ++i) {
			cin >> temp;
			op[temp[0]] = temp[1];
			op[temp[1]] = temp[0];
		}
		char c;
		string line = "";
		cin >> nc >> line;
		for (int j = 0; j < nc; ++j) {
			c = line[j];
			int i = res.size();
			if (res.size() > 0) {
				string term = "  ";
				term[0] = res[i - 1];
				term[1] = c;
				if (cb.find(term) != cb.end()) {
					res.pop_back();
					res.push_back(cb[term]);
				} else if (op.find(c) != op.end() && findinvector(res, op[c])) {
					res.clear();
				} else {
					res.push_back(c);
				}
			} else {
				res.push_back(c);
			}
		}
		printf("Case #%d: [", k + 1);
		for (int i = 0; i < res.size(); ++i)
			printf("%s%c", i == 0 ? "" : ", ", res[i]);
		printf("]\n");
	}
	return 0;
}

