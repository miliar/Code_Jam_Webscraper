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

vector<int> solveIt(int W, int L, vector<int> &r) {
	int N = r.size(), sw = L > W;
	if (sw) swap(W, L);
	vector<pair<int, int> > rp(N);
	for (int i = 0; i < N; i++) rp[i] = make_pair(r[i], i);
	sort(rp.rbegin(), rp.rend());

	vector<int> res(N*2, -1);
	int cy = 0, cx = 0, mxy = 0;
	for (int i = 0; i < N; i++) {
		int xp = cx + (cx?rp[i].first:0);
		int yp = cy + (cy?rp[i].first:0);
		if (xp > W) {
			cy += mxy;
			cx = 0;
			i--;
			continue;
		}
		if (yp > L) {
			fprintf(stderr, "Oops\n");
		}
		cx += rp[i].first*(cx?2:1);
		int y = rp[i].first*(cy?2:1);
		if (y > mxy) mxy = y;

		res[rp[i].second*2] = xp;
		res[rp[i].second*2+1] = yp;
	}

	if (sw) for (int i = 0; i < N; i++) swap(res[i*2], res[i*2+1]);
	return res;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int N, W, L;
		scanf("%d %d %d ", &N, &W, &L);
		vector<int> r = readVI(N);

		vector<int> res = solveIt(W, L, r);
		for (int i = 0; i < N; i++) {
			if (res[i*2] < 0 || res[i*2] > W) fprintf(stderr, "bad x\n");
			if (res[i*2+1] < 0 || res[i*2+1] > L) fprintf(stderr, "bad y\n");
			for (int j = 0; j < i; j++) {
				long long d2 = (res[i*2]-res[j*2])*(long long)(res[i*2]-res[j*2]) +
					(res[i*2+1]-res[j*2+1])*(long long)(res[i*2+1]-res[j*2+1]);
				if (d2 < (r[i]+r[j])*(long long)(r[i]+r[j])) {
					fprintf(stderr, "too close\n");
					fprintf(stderr, " %d: r %d, %d, %d\n", i, r[i], res[i*2], res[i*2+1]);
					fprintf(stderr, " %d: r %d, %d, %d\n", j, r[j], res[j*2], res[j*2+1]);
				}
			}
		}
		printf("Case #%d:", cn);
		for (unsigned int i = 0; i < res.size(); i++) printf(" %d", res[i]);
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

