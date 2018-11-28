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

vector<string> readDict(int N) {
	vector<string> d(N);
	for (int i = 0; i < N; i++) d[i] = readLine();
	return d;
}

int count(vector<string> &d, string &lst, string &w) {
	int n = w.size();
	string g(n, '.');
	vector<int> vg(26, 0), guessed(26, 0);
	for (size_t i = 0; i < d.size(); i++) for (int j = 0; j < n; j++) vg[d[i][j]-'a'] = 1;
	int ct = 0;
//printf("w %s, lst %s\n", w.c_str(), lst.c_str());
	for (int i = 0; i < 26; i++) if (vg[lst[i]-'a']) {
		guessed[lst[i]-'a']++;
//printf("guess %c when g %s\n", lst[i], g.c_str());
		int h = 0;
		for (int j = 0; j < n; j++) if (w[j] == lst[i]) {
			g[j] = lst[i];
			h++;
		}
		if (!h) ct++;
//printf(" h %d -> ct %d\n", h, ct);
		vg.clear();
		vg.resize(26, 0);
		int u = 0;
		for (size_t j = 0; j < d.size(); j++) {
			int ok = 1;
			for (int k = 0; k < n; k++)
				if ((g[k] > '.' && g[k] != d[j][k]) ||
						(g[k] == '.' && guessed[d[j][k]-'a'])) {
					ok = false;
					break;
				}
			if (ok) {
//printf("  %s matches %s\n", g.c_str(), d[j].c_str());
				u++;
				for (int k = 0; k < n; k++) if (g[k] == '.') vg[d[j][k]-'a'] = 1;
			}
		}
//printf(" u %d\n", u);
		if (u < 1) break;
	}
	return ct;
}

string solveIt(vector<vector<string> > &d, vector<string> &ad, string &lst) {
	int mxc = -1; string fw = "";
	for (size_t i = 0; i < ad.size(); i++) {
		int c = count(d[ad[i].size()], lst, ad[i]);
//printf(" %s -> %d\n", ad[i].c_str(), c);
		if (c > mxc) {
			mxc = c;
			fw = ad[i];
		}
	}
	return fw;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int N, M;
		scanf("%d %d ", &N, &M);

		vector<string> d = readDict(N);
		vector<vector<string> > nd(11);
		for (int i = 0; i < N; i++) nd[d[i].size()].push_back(d[i]);

		printf("Case #%d:", cn);
		for (int i = 0; i < M; i++) {
			string lst = readLine();
			string res = solveIt(nd, d, lst);
			printf(" %s", res.c_str());
		}
		printf("\n");
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

