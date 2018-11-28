#include <iostream>
#include <cassert>
#include <string>
#include <cstdio>
#include <sstream>
#include <set>

using namespace std;

void solve(int test) {
	int a;
	int b;
	cin >> a >> b;
	stringstream ss;
	string s;
	int ans = 0;
	for (int n = a; n <= b; ++n) {
		ss.clear();
		ss << n;
		ss >> s;
		set<int> var;
		for (int j = 0; j < (int) s.size(); ++j) {
			if (s[0] != '0') {
				ss.clear();
				ss << s;
				int x;
				ss >> x;
				if (n < x && x <= b) {
					var.insert(x);
				}
			}
			s = s.substr(1) + s[0];
		}
		ans += var.size();
	}
	cout << "Case #" << test << ": " << ans << endl;
}

void pre() {
}

int main() {
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	pre();
	int n;
	cin >> n;
	string tmp;
	getline(cin, tmp);
	for (int i = 1; i <= n; ++i) {
		solve(i);
	}
	return 0;
}
