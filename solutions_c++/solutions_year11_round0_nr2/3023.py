#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <string>
#include <stack>
#include <queue>

using namespace std;


int main() {

	//ifstream in("B.in");
	//ofstream out("B.out");
	//ifstream in("B-small.in");
	//ofstream out("B-small.out");
	ifstream in("B-large.in");
	ofstream out("B-large.out");

	int T; in >> T;

	for (int x = 0; x < T; x++) {
		int C; in >> C; vector<string> c;
		for (int i = 0; i < C; i++) { string t; in >> t; c.push_back(t); }
		int D; in >> D; vector<string> d;
		for (int i = 0; i < D; i++) { string t; in >> t; d.push_back(t); }
		int N; in >> N; string s; in >> s;
		string l;
		for (int i = 0; i < N; i++) {
			l += s[i];
			if (l.size() > 1) {
				int n = l.size() - 1;
				char a = l[n], b = l[n - 1];
				for (int j = 0; j < C; j++) {
					if ((c[j][0] == a && c[j][1] == b) || (c[j][0] == b && c[j][1] == a)) {
						l = l.substr(0, l.size() - 2) + c[j][2];
						break;
					}
				}
				for (int j = 0; j < D; j++) {
					char p = d[j][0], q = d[j][1];
					bool is_p = 0, is_q = 0;
					for (int k = 0; k < l.size(); k++) {
						if (l[k] == p) is_p = 1;
						if (l[k] == q) is_q = 1;
					}
					if (is_p && is_q) { l = ""; break; }
				}
			}
		}
		out << "Case #" << x + 1 << ": [";
		for (int i = 0; i < l.size(); i++) {
			out << ((i == 0) ? "" : ", ") << l[i];
		}
		out << "]" << endl;
	}

	return 0;
}
