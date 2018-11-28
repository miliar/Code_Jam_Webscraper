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

bool solveIt(vector<int> &li, vector<int> &di, int D) {
	int N = li.size();
	vector<int> fr(N, -1);
	fr[0] = di[0]*2;
	if (fr[0] >= D) return true;
	int e = 0;
	for (int v = 1; v < N; v++) {
		if (di[v] < di[v-1]) fprintf(stderr, "Unsorted\n");
		while (e < v && fr[e] < di[v]) e++;
		for (int i = e; i < v; i++) {
			if (fr[i] >= di[v]) {
				int d = min(di[v]-di[i], li[v]);
				int r = di[v] + d;
				if (r > fr[v]) {
					fr[v] = r;
					if (r >= D) return true;
				}
			}
		}
	}
	return false;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int N, D;
		scanf("%d ", &N);
		vector<int> li(N), di(N);
		for (int i = 0 ; i < N; i++) scanf("%d %d", &di[i], &li[i]);
		scanf("%d", &D);

		bool res = solveIt(li, di, D);
		printf("Case #%d: %s\n", cn, res?"YES":"NO");
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
	unsigned int start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(s.substr(start, end-start));
	}
	return res;
}
vector<int> itokens(string s, string sep = " \n\r\t") {
	vector<int> res;
	unsigned int start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(atoi(s.substr(start, end-start).c_str()));
	}
	return res;
}

