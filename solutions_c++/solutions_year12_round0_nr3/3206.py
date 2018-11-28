#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <map>

using namespace std;

string d2s(int x) {
	stringstream ss; ss << x;
	string ret; ss >> ret;
	return ret;
}

int s2d(const string& x) {
	stringstream ss; ss << x;
	int ret; ss >> ret;
	return ret;
}

map<int, int> f;

int main() {
	int cases; cin >> cases;

	for (int T = 1; T <= cases; ++T) {
		printf("Case #%d: ", T); int ans = 0;
		int a, b; cin >> a >> b;

		for (int i = a; i <= b; ++i) {
			string str = d2s(i); f.clear();

			for (int j = 1; j < str.length(); ++j) {
				string to = "";
				for (int k = j; k < str.length(); ++k) to += str[k];
				for (int k = 0; k < j; ++k) to += str[k];
				int x = s2d(to);
				if (f[x] > 0) continue; f[x]++;
				if (x > i && x <= b) ans++;
			}
		}

		cout << ans << endl;
	}

	return 0;
}
