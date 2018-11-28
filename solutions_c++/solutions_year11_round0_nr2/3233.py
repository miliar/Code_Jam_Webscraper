#include <string>
#include <vector>
#include <iostream>
using namespace std;

struct combine {
	combine() { rep = rev = res = ""; }
	string rep, rev, res;
};

inline void doreplace(string &cur, vector<combine> combines) {
	bool replace = false;
	do {
		replace = false;
		if (cur.length() < 2) return;
		for (int i = 0; i < combines.size(); i++) {
			//cout << cur.substr(cur.length() - 2) << ", looking for " << combines[i].rep << "\n";
			if (cur.substr(cur.length() - 2) == combines[i].rep || cur.substr(cur.length() - 2) == combines[i].rev) {
				//cout << "Found " << combines[i].rep << " in " << cur << "\n";
				cur.replace(cur.length() - 2, 2, combines[i].res);
				replace = true;
				break;
			}
		}		
	} while(replace);
}

inline bool find(string x, char f) {
	for (int i = 0; i < x.length(); i++) if (x[i] == f) return true;
	return false;
}

inline bool checkclear(string cur, vector<pair<char, char> > opposed) {
	for (int i = 0; i < opposed.size(); i++) if (find(cur, opposed[i].first) && find(cur, opposed[i].second)) return true;
	return false;
}


int T, C, D, N;

int main() {
	string str;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> C;
		vector<pair<char, char> > opposed;
		vector<combine> combines;
		for (int c = 0; c < C; c++) {
			combine x;
			cin >> str;
			//cout << "Combine " << c << "/" << C << ": " << str << "\n";
			x.rep += str[0]; x.rep += str[1]; x.res += str[2];
			x.rev += str[1]; x.rev += str[0];
			//cout << "Combine: " << x.rep << " -> " << x.res << "\n";
			combines.push_back(x);
		}

		cin >> D;
		for (int d = 0; d < D; d++) {
			cin >> str;
			opposed.push_back(make_pair(str[0], str[1]));
			//cout << "Opposed: " << opposed[opposed.size() - 1].first << " - " << opposed[opposed.size() - 1].second << "\n";
		}

		cin >> N >> str;
		string cur = "";
		for (int i = 0; i < str.length(); i++) {
			cur += str[i];
			doreplace(cur, combines);
			if (checkclear(cur, opposed)) cur = "";
		}
		cout << "Case #" << t << ": [";
		for (int i = 0; i < cur.length(); i++) {
			cout << cur[i];
			if (i != cur.length() - 1) cout << ", ";
		}
		cout << "]\n";
	}
}