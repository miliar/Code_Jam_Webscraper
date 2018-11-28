#include <iostream>
#include <string>
#include <set>
using namespace std;

int gao(string &t) {
	multiset<char> s(t.begin(), t.end());
	if (s.count('O') + s.count('T') == 4) {
		return 2;
	} else if (s.count('X') + s.count('T') == 4) {
		return 1;
	} else {
		return 0;
	}
}

int main() {
	int Tc;
	int ans;
	string s[4], t, p;
	cin >> Tc;
	for (int re = 1; re <= Tc; ++re) {
		ans = 0;
		bool incomplete = false;
		for (int i = 0; i < 4; ++i) {
			cin >> s[i];
			ans |= gao(s[i]);
		}
	
		for (int j = 0; j < 4; ++j) {
			t.clear();
			for (int i = 0; i < 4; ++i) {
				t.push_back(s[i][j]);
				incomplete |= s[i][j] == '.';
			}
			ans |= gao(t);
		}
		p.clear();
		t.clear(); 
		for (int k = 0; k < 4; ++k) {
			p.push_back(s[k][k]);
			t.push_back(s[k][3 - k]);
		}
		ans |= gao(p);
		ans |= gao(t);
		string res = (ans & 1) ? "X won" : ((ans & 2) ? "O won" : (!incomplete ? "Draw" : "Game has not completed"));
		cout << "Case #" << re << ": "
			<< res
			<< endl;
	}
	return 0;
}
