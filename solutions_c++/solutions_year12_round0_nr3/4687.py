#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <cstdio>

using namespace std;

int Size(int i) {

	string x;
	stringstream s;
	s << i;
	s >> x;

	return x.size();
}

int toInt(string s) {

	int i;
	stringstream ss;
	ss << s;
	ss >> i;

	return i;
}

bool isNSymm(string s) {

	char x = s[0];
	for(unsigned int i = 0; i < s.size(); i++) {
		if(s[i] != x) {
			return true;
		}
	}
	return false;
}

bool fun(string s) {
	if(s[0] == '0' || s[s.size() - 1] == '0') {
		return false;
	}
	return true;
}

int main() {

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int T, a, b;
	string temp1, temp2;
	cin >> T;
	set<pair<string, string> > sm;

	for(int i = 0; i < T; i++) {

		cin >> a >> b;

		for(int k = a; k <= b; k++) {

			stringstream s;
			s << k;
			s >> temp1;
			temp2 = temp1;

			if(!isNSymm(temp1)) {
				continue;
			}

			if(temp1.size() > 1) {
				for(unsigned int v = 0; v < temp1.size(); v++) {
					temp2 += temp2[0];
					temp2.erase(0, 1);

					if(toInt(temp2) >= a && toInt(temp2) <= b && Size(toInt(temp2)) == Size(toInt(temp1)) && temp1 != temp2) {
						sm.insert(make_pair(temp1, temp2));
					}
				}
			}

		}
		cout << "Case #" << i + 1 << ": " << sm.size() / 2 << endl;
		sm.clear();
	}



	return 0;
}
