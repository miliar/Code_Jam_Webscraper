#include <iostream>
#include <string>
#include <vector>
#include <set>
using namespace std;

int n, m;
int c1, c2;
set<string> a;

void make(string s) {
	s = s + "/";
	for (int i = 1; i < s.size(); i++) {
		if (s[i] == '/') {
//			cout << s.substr(0, i) << endl;
			a.insert(s.substr(0, i));
		}
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int test;
	cin >> test;
	for (int i = 1; i <= test; i++) {
		cin >> n >> m;
		a.clear();
		for (int j = 0; j < n; j++) {
			string s;
			cin >> s;
			make(s);
		}
		c1 = a.size();
		
//		cout << "---" << endl;
		
		for (int j = 0; j < m; j++) {
			string s;
			cin >> s;
			make(s);
		}
		c2 = a.size();
		cout << "Case #" << i << ": " << c2 - c1 << endl;
	}
	return 0;
}
