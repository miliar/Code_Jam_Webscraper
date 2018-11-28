#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream fin("input");
ofstream fout("output");

void solve() {
	int c;
	fin >> c;
	vector< vector<char> > combination(26, vector<char>(26, 30));
	for (int i = 0; i < c; i++) {
		string buf;
		fin >> buf;
		combination[buf[0] - 'A'][buf[1] - 'A'] = buf[2] - 'A';
		combination[buf[1] - 'A'][buf[0] - 'A'] = buf[2] - 'A';
	}
	
	int d;
	fin >> d;
	vector< pair<char, char> > oposite(d);
	for (int i = 0; i < d; i++) {
		string buf;
		fin >> buf;
		oposite[i] = make_pair(buf[0] - 'A', buf[1] - 'A');
	}
	
	int n;
	fin >> n;
	string s;
	fin >> s;
	vector<int> list;
	vector<int> qnt(26, 0);
	for (int i = 0; i < n; i++) {
		s[i] -= 'A';
		if (!list.empty() && (combination[list[list.size() - 1]][s[i]] != 30)) {
			char res = combination[list[list.size() - 1]][s[i]];
			qnt[list[list.size() - 1]]--;
			list.pop_back();
			list.push_back(res);
			qnt[res]++;
		}
		else {
			list.push_back(s[i]);
			qnt[s[i]]++;
		}
		for (vector< pair<char, char> >::iterator it = oposite.begin(); it != oposite.end(); it++) {
			if (qnt[it->first] && qnt[it->second]) {
				qnt.assign(26, 0);
				list.clear();
				break;
			}
		}
	}
	
	fout << "[";
	for (int i = 0; i < list.size(); i++) {
		fout << char(list[i] + 'A');
		if (i < list.size() - 1) {
			fout << ", ";
		}
	}
	fout << "]" << endl;
}

int main() {
	int t;
	fin >> t;
	for (int i = 0; i < t; i++) {
		fout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}
