#include <numeric>
#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <iomanip>
#include <string>
#include <cctype>
#include <stdio.h>
#include <cstdlib>
#include <memory.h>

using namespace std;

//#define in cin
//#define out cout

ifstream in("input.txt");
ofstream out("output.txt");

int t, n;
string s;
char c, a[120];
map<string, char> M1;
map<char, set<char> > M2;
multiset<char> cur;
stack<char> S;

int main() {
	in >> t;
	for (int tt = 0; tt < t; tt++) {

		M1.clear();
		M2.clear();
		while (!S.empty()) S.pop();
		cur.clear();

		in >> n;
		for (int i = 0; i < n; ++i) {
			in >> s;
			string t = "aa";
			t[0] = s[0]; t[1] = s[1];
			M1[t] = s[2];
			t[1] = s[0]; t[0] = s[1];
			M1[t] = s[2];
		}

		in >> n;
		for (int i = 0; i < n; ++i) {
			in >> s;
			M2[s[0]].insert(s[1]);
			M2[s[1]].insert(s[0]);
		}

		in >> n;
		for (int i = 0; i < n; ++i) {
			in >> a[i];
		}

		for (int i = 0; i < n; ++i) {
			if (S.empty()) {
				S.push(a[i]);
				cur.insert(a[i]);
				continue;
			}

			s = "aa";
			s[0] = S.top(); s[1] = a[i];

			if (M1.find(s) != M1.end()) {
				cur.erase(cur.find(S.top()));
				S.pop();

				S.push(M1[s]);
				cur.insert(M1[s]);
			}
			else if (M2.find(a[i]) != M2.end() && !cur.empty()) {

				vector<char> v;
				set_intersection(M2[a[i]].begin(), M2[a[i]].end(), cur.begin(), cur.end(), inserter(v, v.begin()));

				if (!v.empty()) {
					while (!S.empty()) S.pop();
					cur.clear();
				}
				else {
					S.push(a[i]);
					cur.insert(a[i]);
				}
			} else {
				S.push(a[i]);
				cur.insert(a[i]);
			}
		}

		out << "Case #" << tt + 1 << ": [";

		if (!S.empty()) {
			vector<char> v;
			while (!S.empty()) {
				v.push_back(S.top());
				S.pop();
			}
			reverse(v.begin(), v.end());
			for (int i = 0; i < v.size() - 1; ++i) out << v[i] << ", ";
			if (!v.empty()) out << v[v.size() - 1];
		}
		out << "]\n";
	}

	return 0;
}
