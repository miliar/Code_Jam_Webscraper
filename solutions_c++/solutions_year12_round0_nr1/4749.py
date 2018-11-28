#include <algorithm>
#include <iostream>
#include <sstream>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>

#define sz(a) (int)a.size()
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()
#define llong long long
#define zero(a) fabs(a) < 1e-9
#define resz(a, n) a.clear(), a.resize(n)
#define same(a, n) memset(a, n, sizeof(a))
#define make(a, b) make_pair(a, b)

using namespace std;

const string M = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.out", "w", stdout);
	/*
	same(m, -1);
	m['q' - 'a'] = 'z' - 'a';
	m['z' - 'a'] = 'q' - 'a';
	for (int i = 0; i < 3; i++) {
		getline(cin, a);
		getline(cin, b);
		for (int i = 0; i < sz(a); i++)
			m[a[i] - 'a'] = b[i] - 'a';
	}
	for (int i = 0; i < 26; i++)
		cout << (char)(m[i] + 'a');
	cout << endl;
	*/
	int t;
	cin >> t;
	getchar();
	for (int i = 0; i < t; i++) {
		string s;
		getline(cin, s);
		cout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < sz(s); j++) {
			if (isalpha(s[j]))
				s[j] = M[s[j] - 'a'];
			cout << s[j];
		}
		cout << endl;
	}
	return 0;
}

