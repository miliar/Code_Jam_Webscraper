#include <iostream>
#include <set>
#include <string>

using namespace std;

void alg() {
	set<string> got;
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n; ++i) {
		string s;
		cin >> s;
		got.insert(s);
	}
	got.insert("");
	int res = 0;
	for (int i = 0; i < m; ++i) {
		string s;
		cin >> s;
		while (got.find(s) == got.end()) {
			got.insert(s);
			++res;
			while (s[s.length() - 1] != '/')
				s.erase(s.length() - 1, 1);
			s.erase(s.length() - 1, 1);
		}
	}
	cout << res << "\n";
}

int main() {
	int d;
	cin >> d;
	for (int i = 1; i <= d; ++i) {
		cout << "Case #" << i << ": ";
		alg();
	}
}
