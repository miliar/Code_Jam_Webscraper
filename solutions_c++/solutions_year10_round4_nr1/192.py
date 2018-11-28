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

int solveIt(int k, vector<string> &d) {
	if (dbg > 2) for (int i = 0; i < d.size(); i++) printf("%s\n", d[i].c_str());
	int res = 0;
	int baxk = k-1, bayk = k-1;
	int j = k-1;
	for (int i = 0; i < k; i++) {
		bool ok = true;
		int c = j-i;
		for (int y = 0; ok && y < d.size(); y++) {
			for (int x = 0; x < c; x++) if (d[y].size() > c*2-x && d[y][c*2-x] != d[y][x] && d[y][c*2-x] >= '0' && d[y][x] >= '0') { ok = false; break; }
		}
		if (ok) { baxk = i; break; }
		ok = true;
		c = j+i;
		for (int y = 0; ok && y < d.size(); y++) {
			for (int x = d[y].size()-1; x > c; x--) if (d[y][c*2-x] != d[y][x] && d[y][c*2-x] >= '0' && d[y][x] >= '0') { ok = false; break; }
		}
		if (ok) { baxk = i; break; }
	}
	for (int i = 0; i < k; i++) {
		bool ok = true;
		int c = j-i;
		for (int x = 0; ok && x < d.size(); x++) {
			for (int y = 0; y < c; y++) if (x < d[y].size() && d.size() > c*2-y && d[c*2-y][x] != d[y][x] && d[c*2-y][x] >= '0' && d[y][x] >= '0') { ok = false; break; }
		}
		if (ok) { bayk = i; break; }
		ok = true;
		c = j+i;
		for (int x = 0; ok && x < d.size(); x++) {
			for (int y = d.size()-1; y > c; y--) if (x < d[y].size() && d[c*2-y][x] != d[y][x] && d[c*2-y][x] >= '0' && d[y][x] >= '0') { ok = false; break; }
		}
		if (ok) { bayk = i; break; }
	}
	if (dbg > 1) printf("baxk %d, bayk %d\n", baxk, bayk);
	int nk = k + baxk + bayk;
	return nk*nk - k*k;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int k = readIntLine();
		vector<string> vs = readVS(k*2-1);

		long long res = solveIt(k, vs);
		printf("Case #%d: %lld\n", cn, res);
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

