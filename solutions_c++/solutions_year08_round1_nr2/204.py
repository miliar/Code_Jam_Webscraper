#include <iostream>
#include <vector>

using namespace std;

typedef pair<int,int> pii;

int test;

int n, m;

vector<pii> v[2000]; 

int cnt(int n) {
	if (n == 0) return 0; return 1 + cnt(n & (n - 1));
}

void solve() {
	int res = -1;

	cin >> n >> m; for (int i = 0; i < m; i++) v[i].clear();
	
	for (int i = 0; i < m; i++) {
		int T; cin >> T; 
		for (int j = 0; j < T; j++) {
			int x, y; scanf("%d%d",&x, &y); x--;
			v[i].push_back(make_pair(x, y));
		}
	}
	
	for (int i = 0; i < (1 << n); i++) {
		bool ok = true;
		for (int j = 0; j < m; j++) {
			bool f = false;
			for (int k = 0; k < v[j].size(); k++) {
				int t = i & (1 << v[j][k].first);
				if (t == 0 && v[j][k].second == 0) f = true;
				if (t != 0 && v[j][k].second != 0) f = true;
			}
			if (f == false) ok = false;
		}
		if (ok) {
			if (res == -1 || cnt(res) > cnt(i)) res = i;
		}
	}

	cout << "Case #" << test << ": ";
	if (res == -1) cout << "IMPOSSIBLE" << endl; else {
		for (int i = 0 ; i < n; i++) {
			if (i) cout << ' ';
			if (res & (1 << i)) cout << 1; else cout << 0;
		}
		cout << endl;
	}
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int TEST;
	cin >> TEST;
	for (test = 1; test <= TEST; test++)
		solve();
	return 0;
}