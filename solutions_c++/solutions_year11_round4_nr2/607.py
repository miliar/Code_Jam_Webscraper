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


bool check(int K, const int R, const int C, const vector<vector<int> > &w) {
	for (int y = 0; y+K <= R; y++) for (int x = 0; x+K <= C; x++) {
		int xcm = 0, ycm = 0, d = K-1;
		for (int j = 0; j < K; j++) for (int i = 0; i < K; i++) {
			if ((!j || j+1 == K) && (!i || i+1 == K)) continue;
			ycm += w[y+j][x+i]*(j*2-d);
			xcm += w[y+j][x+i]*(i*2-d);
		}
		if (!ycm && !xcm) return true;
	}
	return false;
}

int solveIt(int R, int C, int /*D*/) {
	vector<vector<int> > w(R, vector<int>(C));
	char sz[512];
	for (int i = 0; i < R; i++) {
		fgets(sz, 512, stdin);
		for (int j = 0; j < C; j++) w[i][j] = sz[j]-'0';
	}
	int i = R>C?C:R;
	for (; i >= 3; i--) if (check(i, R, C, w)) return i;
	return -1;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int R, C, D;
		scanf("%d %d %d ", &R, &C, &D);

		long long res = solveIt(R, C, D);
		if (res < 0)
			printf("Case #%d: IMPOSSIBLE\n", cn);
		else
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

