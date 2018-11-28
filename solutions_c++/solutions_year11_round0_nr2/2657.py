#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cassert>

#define vv vector
#define pb push_back
#define mp make_pair
#define px first
#define py second
#define in cin
#define out cout
#pragma warning(disable: 4996)

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int cases;
	in >> cases;

	for (int tcase = 0; tcase < cases; ++tcase) {
		int c; in >> c;
		vv< vv<char> > comb(255, vv<char>(255, 0));
		for (int i = 0; i < c; ++i) {
			string combination;
			in >> combination;
			comb[combination[0]][combination[1]] = combination[2];
			comb[combination[1]][combination[0]] = combination[2];
		}
		int d; in >> d;
		vv< vv<bool> > opp(255, vv<bool>(255, false));
		for (int i = 0; i < d; ++i) {
			string opposed;
			in >> opposed;
			opp[opposed[0]][opposed[1]] = opp[opposed[1]][opposed[0]] = true;
		}
		int n; string s;
		in >> n >> s;
		
		vv<char> e;
		for (int i = 0; i < n; ++i) {
			e.push_back(s[i]);
			while (e.size() >= 2) {
				char ex = e[e.size() - 1];
				char ey = e[e.size() - 2];
				if (comb[ex][ey] != 0) {
					e.pop_back();
					e.pop_back();
					e.push_back(comb[ex][ey]);
				} else {
					break;
				}
			}
			for (int j = 0; j < e.size(); ++j) {
				if (opp[e[j]][e.back()]) {
					e.clear();
					break;
				}
			}
		}

		out << "Case #" << tcase + 1 << ": [";
		for (int i = 0; i < e.size(); ++i) {
			if (i > 0) {
				out << ", ";
			}
			out << e[i];
		}
		out << "]" << endl;
	}

	return 0;
}