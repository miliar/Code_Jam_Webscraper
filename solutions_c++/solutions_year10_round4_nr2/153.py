#include<vector>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<set>
#include<map>
#include<sstream>
#include<queue>
#include<climits>
#include<cmath>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

int P, N;
ll inf;

int miss[2048];
ll price[16][2096];

ll cc[16][2096][16];
ll dp(int p, int i, int m) {
	if(p < 0) {
		// at bottom layer
		if(m <= miss[i]) return 0;
		return inf;
	}
	ll& ret = cc[p][i][m];
	if(ret >= 0) return ret;
	const int left = 2*i;
	const int right = 2*i + 1;
	// don't miss
	ret = price[p][i] + dp(p-1, left, m) + dp(p-1, right, m);
	// miss it !
	ret = min(ret, dp(p-1, left, m+1) + dp(p-1, right, m+1));
	return ret;
}

int main() {
	int T; cin >> T;
	for(int tt = 1; tt <= T; ++tt) {
		cin >> P;
		N = (1 << P);
		for(int i = 0; i < N; ++i) {
			cin >> miss[i];
		}
		inf = 0;
		for(int p = 0; p < P; ++p) {
			int n = (1 << (P - p - 1));
			for(int i = 0; i < n; ++i) {
				cin >> price[p][i];
				inf += price[p][i] + 1;
				for(int m = 0; m < P; ++m) {
					cc[p][i][m] = -1;
				}
			}
		}
		ll ans = dp(P - 1, 0, 0);
		cout << "Case #" << tt << ": " << ans << endl;
	}
	return 0;
}

