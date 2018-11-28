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

pair<int, int> solveIt(int P, int W) {
	vector<vector<int> > w(P);
	vector<long long > m(P, 0);
	for (int i = 0; i < W; i++) {
		int x, y;
		scanf("%d,%d", &x, &y);
		m[x] |= 1LL<<y;
		m[y] |= 1LL<<x;
		w[x].push_back(y);
		w[y].push_back(x);
	}

	if (m[0]&2) return make_pair(0, w[0].size());

	vector<map<pair<long long, long long>, int> > b(P);
	pair<long long, long long> oton;
	oton.first = m[0];
	oton.second = 1;
	b[0][oton] = 0;
	queue<pair<pair<long long, long long>, int> > q;
	q.push(make_pair(oton, 0));
	int bct = P+1, tct = 0;
	while (!q.empty()) {
		pair<long long, long long> ot = q.front().first;
		int p = q.front().second;
		q.pop();
		int ct = b[p][ot]+1;
		if (ct > bct) break;
		for (int i = 0; i < w[p].size(); i++) {
			int np = w[p][i];
			pair<long long, long long> ton = ot;
			ton.first |= m[np];
			ton.second |= 1LL<<np;
			if (ton.first&2) {
				int ntct = 0;
				for (int j = 0; j < P; j++)
					if (!((ton.second>>j)&1) && ((ton.first>>j)&1)) ntct++;
				if (ct < bct || (ct == bct && ntct > tct)) {
					bct = ct;
					tct = ntct;
				}
			} else if (b[np].find(ton) == b[np].end()) {
				b[np][ton] = ct;
				q.push(make_pair(ton, np));
			}
		}
	}

	return make_pair(bct, tct);
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int P, W;
		scanf("%d %d", &P, &W);

		pair<int, int> res = solveIt(P, W);
		printf("Case #%d: %d %d\n", cn, res.first, res.second);
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

