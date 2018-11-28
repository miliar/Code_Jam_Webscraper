#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

#define REP(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define sz(v) (int)(v).size()

int a[26] = {24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25, 19, 13, 22, 9, 15, 5, 12, 0, 16};

int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	/*
	memset(a, -1, sizeof(a));
	int tst;
	cin >> tst;
	string s, t;
	getline(cin, s);
	REP(_, tst) {
		getline(cin, s);
		getline(cin, t);
		REP(i, sz(s)) {
			if (s[i] != ' ') {
				int x = s[i] - 'a';
				int y = t[i] - 'a';
				if (a[x] != -1) {
					assert(a[x] == y);
				} else {
					a[x] = y;
				}
			}
		}
	}
	REP(i, 26) cout << a[i] << ", ";//cout << (char)('a' + i) << "->" << (char)('a' + a[i]) << " " << a[i] << endl;
	*/
	int tst;
	cin >> tst;
	string s;
	getline(cin, s);
	for (int test = 1; test <= tst; test++) {
		getline(cin, s);
		REP(i, sz(s)) s[i] = (s[i] == ' '? ' ': (char)('a' + a[s[i] - 'a']));
		printf("Case #%d: %s\n", test, s.c_str());
	}
	return 0;
}