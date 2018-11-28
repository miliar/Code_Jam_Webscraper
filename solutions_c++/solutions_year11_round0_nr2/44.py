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

string solveIt() {
	int N;
	char sz[128];
	vector<char> combo(26*26, 0);
	scanf("%d ", &N);
	for (int i = 0; i < N; i++) {
		scanf("%127s ", sz);
		combo[(sz[0]-'A')*26+(sz[1]-'A')] = sz[2];
		combo[(sz[1]-'A')*26+(sz[0]-'A')] = sz[2];
	}
	scanf("%d ", &N);
	vector<int> opp(N);
	for (int i = 0; i < N; i++) {
		scanf("%127s ", sz);
		opp[i] = (1<<(sz[0]-'A'))|(1<<(sz[1]-'A'));
	}
	string s;
	scanf("%d %127s", &N, sz);
	int bs = 0;
	vector<int> cct(26, 0);
	for (int i = 0; i < N; i++) {
		s += sz[i];
		cct[sz[i]-'A']++;
		bs |= 1<<(sz[i]-'A');
		while (s.size() > 1) {
			int s1 = s[s.size()-1]-'A', s2 = s[s.size()-2]-'A';
			int b = s2*26 + s1;
			if (combo[b]) {
				if (!--cct[s1]) bs &= ~(1<<s1);
				if (!--cct[s2]) bs &= ~(1<<s2);
				s.resize(s.size()-1);
				s[s.size()-1] = combo[b];
				cct[combo[b]-'A']++;
				bs |= 1<<(combo[b]-'A');
			} else
				break;
		}
		if (s.size() > 1) for (int j = 0; j < opp.size(); j++) if ((bs&opp[j]) == opp[j]) {
			s.clear();
			cct.clear();
			cct.resize(26, 0);
			bs = 0;
			break;
		}
	}
	string res = "[";
	for (int i = 0; i < s.size(); i++) {
		if (i) res += ", ";
		res += s[i];
	}
	res += ']';
	return res;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		string res = solveIt();
		printf("Case #%d: %s\n", cn, res.c_str());
	}
	return 0;
}








string readLine() {
	char sz[1000];
	fgets(sz, 1000, stdin);
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

