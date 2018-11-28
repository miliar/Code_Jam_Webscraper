#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define Nul(a) memset(a, 0, sizeof(a))
#define Fil(a, b) memset(a, b, sizeof(a))
#define Size(a) ((int)a.size())

string name[200];
int l[200], r[200], u = 0;
bool leaf[200];
char _s[100000];
double v[200];
void SkipTo(string &s, int &i, char c1, char c2) {
	while (i < Size(s)) {
		if (s[i] >= c1 && s[i] <= c2) break;
		i++;
	}
}
void SkipTo2(string &s, int &i, char c1, char c2) {
	while (i < Size(s)) {
		if (s[i] >= c1 && s[i] <= c2 || s[i] >= 'a' && s[i] <= 'z') break;
		i++;
	}
}
double ScanD(string &s, int &i) {
	SkipTo(s, i, '0', '9');
	double val = 0, st = 1;
	bool dot = false;
	while (i < Size(s)) {
		if (s[i] >= '0' && s[i] <='9') {
			if (dot) st *= 1e-1;
			val = val * 10 + s[i] - '0';
		} else if (s[i] == '.') {
			dot = true;
		} else {
			break;
		}
		i++;
	}
	return val * st;
}
string ScanS(string &s, int &i) {
	string val;
	while (i < Size(s)) {
		if (s[i] >= 'a' && s[i] <='z') {
			val += s[i];
		} else break;
		i++;
	}
	return val;
}
double dfs(int i, set<string> &cs) {
	if (leaf[i]) {
		return v[i];
	} else {
		if (cs.find(name[i]) == cs.end()) {
			return v[i] * dfs(r[i], cs);
		} else {
			return v[i] * dfs(l[i], cs);
		}
	}
}
int scan(string &s, int &i) {
	SkipTo(s, i, '(', '(');
	int id = u++;
	v[id] = ScanD(s, i);
	SkipTo2(s, i, '(', ')');
	if (s[i] >= 'a' && s[i] <= 'z') {
		name[id] = ScanS(s, i);
		l[id] = scan(s, i);
		r[id] = scan(s, i);
		leaf[id] = false;
	} else {
		leaf[id] = true;
		i++;
	}
	return id;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		printf("Case #%d:\n", ti);
		u = 0;
		int ns;
		scanf("\n");
		gets(_s);
		sscanf(_s, "%d", &ns);
		string s = "";
		for (int i = 0; i < ns; i++) {
			gets(_s);
			s += _s;
		}
		int p = 0;
		scan(s, p);
		int m;
		scanf("%d", &m);
		for (int i = 0; i < m; i++) {
			scanf("%s", _s);
			int k;
			scanf("%d", &k);
			set<string> cs;
			while (k--) {
				scanf("%s", _s);
				cs.insert(_s);
			}
			printf("%.7lf\n", dfs(0, cs));
		}
	}
	return 0;
}