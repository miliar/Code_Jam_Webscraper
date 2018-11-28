#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#define out(v) cout << #v << ": " << (v) << endl
#define FOR(i, n) for (int i = 0; i < (int)(n); ++i)
using namespace std;
typedef long long LL;

int T, N, M;
vector<string> D, L;
int gao2(string s, char x) {
	int ans = 0;
	FOR(i, s.size()) if (s[i] == x) ans |= (1 << i);
	return ans;
}
string gao(string G) {
	int ans = -1;
	string ansD;
	FOR(i, N) {
		int len = D[i].size(), lose = 0;
		vector<string> vec;
		FOR(j, N) if (D[j].size() == len) vec.push_back(D[j]);
		FOR(j, 26) {
			int tot = 0;
			FOR(k, vec.size()) tot += gao2(vec[k], G[j]);
			if (tot == 0) continue;
			if (gao2(D[i], G[j]) == 0) ++lose;
			vector<string> tmp;
			FOR(k, vec.size()) if (gao2(vec[k], G[j]) == gao2(D[i], G[j])) tmp.push_back(vec[k]);
			vec = tmp;
		}
		if (ans < lose)
			ans = lose, ansD = D[i];
	}
	return ansD;
}

int main() {
	cin >> T;
	for (int id = 1; id <= T; ++id) {
		cin >> N >> M;
		D.resize(N); L.resize(M);
		FOR(i, N) cin >> D[i];
		FOR(i, M) cin >> L[i];
		cout << "Case #" << id << ":";
		FOR(i, M) {
			cout << " " << gao(L[i]);
		}
		cout << endl;
	}
	return 0;
}
