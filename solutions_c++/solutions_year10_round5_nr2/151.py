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

int gcd(int a, int b) { return b ? gcd(b, a%b) : a; }

int best[10000];
void buildIt(vector<int> &b) {
	sort(b.begin(), b.end());
	int bb = b.back(), N = bb*bb;
	memset(best, -1, sizeof(best));
	best[0] = 0;
	for (int i = b.size()-1; i >= 0; i--) {
		for (int j = 0; j+b[i] < N; j++) if (best[j] >= 0 && (best[j+b[i]] < 0 || best[j+b[i]] > best[j]+1))
			best[j+b[i]] = best[j]+1;
	}
}

long long solveIt(long long L, vector<int> &b) {
	long long res = -1; int g = b[0];
	for (int i = 1; i < b.size(); i++) g = gcd(g, b[i]);
	if (L%g) return -1;
	buildIt(b);
	int bb = b.back();
	int r = L%bb;
	if (best[r] >= 0) res = best[r] + (L-r)/bb;
	r += bb;
	while (r < bb*bb) {
		if (best[r] >= 0) {
			long long r2 = best[r] + (L-r)/bb;
			if (res < 0 || r2 < res) res = r2;
		}
		r += bb;
	}
	return res;
//	while (r > bb*bb) r -= bb;
//	if (best[r] < 0) return -1;
//	return best[r] + (L-r)/bb;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		long long L; int N;
		scanf("%Ld %d ", &L, &N);
		vector<int> b = readVI(N);

		long long res = solveIt(L, b);
		if (res < 0) printf("Case #%d: IMPOSSIBLE\n", cn);
		else printf("Case #%d: %lld\n", cn, res);
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

