#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

map<pair<vector<pair<long long, long long> > , vector<pair<long long, long long> > >, long long> dp;

long long slv(vector<pair<long long, long long> > a, vector<pair<long long, long long> > b) {
	pair<vector<pair<long long, long long> > , vector<pair<long long, long long> > > pp = make_pair(a, b);
	if (dp.find(pp) != dp.end()) return dp[pp];

	if (a.size() == 0 || b.size() == 0) return 0;
	long long res = 0;
	if (a[0].second == b[0].second) {
		if (a[0].first < b[0].first) { res += a[0].first; b[0].first -= a[0].first; a.erase(a.begin()); }
		else { res += b[0].first; a[0].first -= b[0].first; b.erase(b.begin()); }
		res = max(res, res + slv(a, b));
	} else {
		vector<pair<long long, long long> > ad = a; ad.erase(ad.begin());
		vector<pair<long long, long long> > bd = b; bd.erase(bd.begin());
		res = max(slv(ad, b), slv(a, bd));
	}
	return (dp[pp] = res);
}

int main() {

	//freopen("C.in", "r", stdin);
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small.out", "w", stdout);

	int T; cin >> T;
	for (int x = 1; x <= T; x++) {
		int N, M; cin >> N >> M;
		vector<pair<long long, long long> > a(N), b(M);
		for (int i = 0; i < N; i++) {
			cin >> a[i].first >> a[i].second;
		}
		for (int i = 0; i < M; i++) {
			cin >> b[i].first >> b[i].second;
		}
		long long res = slv(a, b);
		cout << "Case #" << x << ": " << res << endl;;
	}
}
