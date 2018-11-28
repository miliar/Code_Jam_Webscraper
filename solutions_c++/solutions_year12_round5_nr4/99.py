#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>

using namespace std;

int dbg;
string readLine();
int readIntLine();
vector<int> readVI(int n);
vector<string> readVS(int n);
vector<int> itokens(string s, string sep);
vector<string> stokens(string s, string sep);

            //abcdefghijklmnopqrstuvwxyz
string alt = "48  3 9 1     0   57      ";

long long solveIt(int K, string &l) {
	long long res = 0;
	set<string> ss;
	for (int i = 0; i+K-1 < l.size(); i++) {
		string s = l.substr(i, K);
		ss.insert(s);
		if (alt[s[0]-'a'] != ' ') {
			string t = s;
			t[0] = alt[s[0]-'a'];
			ss.insert(t);
			if (alt[s[1]-'a'] != ' ') {
				s[1] = alt[s[1]-'a'];
				t[1] = s[1];
				ss.insert(s);
				ss.insert(t);
			}
		} else if (alt[s[1]-'a'] != ' ') {
			s[1] = alt[s[1]-'a'];
			ss.insert(s);
		}
	}
	vector<int> st(128, 0), nd(128, 0);
	for (auto &s : ss) {
//		printf("%s\n", s.c_str());
		st[s[0]]++;
		nd[s[1]]++;
	}
	bool xst = false, xnd = false;
	for (int i = 0; i < 128; i++) {
//		if (st[i] || nd[i]) printf("%c %d %d\n", (char)i, st[i], nd[i]);
		if (st[i] > nd[i]) {
			res += st[i];
			xst = true;
		} else if (nd[i] > st[i]) {
			res += nd[i];
			xnd = true;
		} else {
			res += st[i];
		}
	}
	if (!xst) res++;
	return res;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int N;
		scanf("%d ", &N);
		string l = readLine();

		long long res = solveIt(N, l);
		printf("Case #%d: %lld\n", cn, res);
	}
	return 0;
}








string readLine() {
	char sz[10000];
	fgets(sz, 10000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}
int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}
vector<int> readVI(int n = 0) {
	if (!n) scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}
vector<string> readVS(int n = 0) {
	if (!n) scanf("%d ", &n);
	vector<string> v(n);
	for (int i = 0; i < n; i++) v[i] = readLine();
	return v;
}
vector<string> stokens(string s, string sep = " \n\r\t") {
	vector<string> res;
	int start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(s.substr(start, end-start));
	}
	return res;
}
vector<int> itokens(string s, string sep = " \n\r\t") {
	vector<int> res;
	int start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(atoi(s.substr(start, end-start).c_str()));
	}
	return res;
}

