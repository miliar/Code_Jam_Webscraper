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

vector<string> B;

int solveIt() {
	int t = 0, ct = 1;
	while (ct) {
		ct = 0;
		for (int y = 99; y >= 0; y--) for (int x = 99; x >= 0; x--)
			if (B[y][x] == '1') {
				if ((!y || B[y-1][x] == '0') && (!x || B[y][x-1] == '0')) B[y][x] = '0';
				else ct++;
			} else if (y && x && B[y-1][x] == '1' && B[y][x-1] == '1') {
				B[y][x] = '1';
				ct++;
			}
		t++;
		if (dbg > 1) {
			printf("Time %d\n", t);
			for (int y = 0; y < 10; y++) {
				for (int x = 0; x < 10; x++) printf("%c", B[y][x]);
				printf("\n");
			}
		}
	}
	return t;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int R;
		scanf("%d ", &R);
		B.clear();
		B.resize(100, string(100, '0'));
		for (int i = 0; i < R; i++) {
			vector<int> cd = readVI(4);
			for (int y = cd[1]-1; y < cd[3]; y++) for (int x = cd[0]-1; x < cd[2]; x++)
				B[y][x] = '1';
		}

		long long res = solveIt();
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

