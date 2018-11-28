#include <vector>
#include <algorithm>
#include <utility>
#include <iostream>
#include <sstream>

using namespace std;

typedef pair<int, int> pii;
typedef vector<bool> VB; 

#define SZ(c) ((int) (c).size())

inline int mininutes(int h, int m) {
	return h * 60 + m;
}

bool lt(const pii &p1, const pii &p2) {
	return p1.second < p2.second;
}

int need(vector<pii> &a, vector<pii> &b, int t) {
	int nA = SZ(a);
	int nB = SZ(b);
	VB markB(nB);
	sort(a.begin(), a.end());
	sort(b.begin(), b.end(), lt);
	int res = nA;
	for (int i = 0; i < nA; ++i) 
		for (int j = 0; j < nB; ++j)
			if (!markB[j] && b[j].second + t <= a[i].first) {
				markB[j] = true;
				--res;
				break;
			}
	return res;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int numCases;
	cin >> numCases;
	for (int c = 1; c <= numCases; ++c) {
		int t;
		cin >> t;
		int na, nb;
		cin >> na >> nb;
		vector<pii> a;
		for (int i = 0; i < na; ++i) {
			int h1, m1, h2, m2;
			char c;
			cin >> h1 >> c >> m1 >> h2 >> c >> m2;
			a.push_back(make_pair(mininutes(h1, m1), mininutes(h2, m2)));
		}
		vector<pii> b;
		for (int i = 0; i < nb; ++i) {
			int h1, m1, h2, m2;
			char c;
			cin >> h1 >> c >> m1 >> h2 >> c >> m2;
			b.push_back(make_pair(mininutes(h1, m1), mininutes(h2, m2)));
		}
		printf("Case #%d: %d %d\n", c, need(a, b, t), need(b, a, t));

	}
	return 0;
}