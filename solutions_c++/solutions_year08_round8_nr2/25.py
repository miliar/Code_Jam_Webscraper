#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <sstream>
#include <map>
#include <queue>

using namespace std;

const int INF = 1e9;
const double eps = 1e-9;
const int NN = 1 << 20;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

#define mp make_pair
#define pb push_back

int test = 1;
map<string, int> COL;
int n;

int get(string s) {
	if (COL.count(s)) return COL[s];
	int res = COL.size(); return COL[s] = res;
}

vector<pii> o[1 << 9];
int K;

pii O[1 << 9];
int N;

int find() {
	sort(O, O + N);
	int l = 1, b = 1;
	int res = 0;
	for (int i = 0; i < N; i++) {
		if (O[i].first <= l) {
			b = max(b, O[i].second);
		} else {
			if (b < O[i].first) return INF;
			l = b;
			b = max(b, O[i].second);
			res++;
		}
	}
	if (l == 10001) return res;
	if (b == 10001) return res + 1;
	return INF;
}

void solve() {
	int res = INF;
	COL.clear();
	cin >> n;
	for (int i = 0; i < (1 << 9); i++) o[i].clear();
	for (int i = 0; i < n; i++) {
		string s; int A, B;
		cin >> s >> A >> B;
		int c = get(s);
		o[c].push_back(mp(A, B + 1));
	}
	K = COL.size(); if (K < 3) K = 3;

	for (int i = 0; i < K; i++) for (int j = i + 1; j < K; j++) for (int k = j+1; k < K; k++) {
		N = 0; 
		for (int t = 0; t < o[i].size(); t++) O[N++] = o[i][t];
		for (int t = 0; t < o[j].size(); t++) O[N++] = o[j][t];
		for (int t = 0; t < o[k].size(); t++) O[N++] = o[k][t];
		int cur = find();
		res = min(res, cur);
	}
	if (res == INF)
		cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
	else
		cout << "Case #" << test << ": " << res << endl;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T = 1;
	cin >> T;
	for (; test <= T; test++)
	solve();
	return 0;
}