#include <cstdio>
using namespace std;
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <iostream>

struct TT {
	string name;
	map<string, TT> sub;
};

TT root;

string get(string &s) {
	string ans = "";
	string t = s;
	reverse(t.begin(), t.end());
	do {
		ans.push_back(t[t.size() - 1]);
		t.resize(t.size() - 1);
	} while ((t.size() != 0) && (t[t.size() - 1] != '/'));
	reverse(t.begin(), t.end());
	s = t;
	return ans;
}

int parse(string s) {
	TT *tmp = &root;
	int ans = 0;
	while (s != "") {
		string w = get(s);
		if (tmp->sub.count(w) == 0) {
			tmp->sub[w] = TT();
			++ans;
		}
		tmp = &(tmp->sub[w]);
//		cout << w << endl;
	}
//	cout << endl;
	return ans;	
}

int solve() {
	int n, m;
	scanf("%d%d", &n, &m);
	root = TT();
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		string s;
		cin >> s;
		parse(s);
	}
	for (int i = 0; i < m; ++i) {
		string s;
		cin >> s;
		ans += parse(s);
	}
	return ans;
}


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: ", i + 1);
		printf("%d\n", solve());
	}
	return 0;
}

