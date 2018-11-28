#include <iostream>
#include <algorithm>

using namespace std;

/*
Input
  	
2
3
1 3 -5
-2 4 1
5
1 2 3 4 5
1 0 1 0 1

Output 
Case #1: -25
Case #2: 6

*/

int test;

int n;
long long v1[1000];
long long v2[1000];

int cnt(int x) {
	int res = 0; if (x) return 1 + cnt(x & (x-1)); else return 0;
}

int r[1 << 8];
bool w[1 << 8];

void solve() {
	cin >> n; for (int i = 0; i < n; i++) scanf("%lld", &v1[i]); for (int i = 0; i < n; i++) scanf("%lld", &v2[i]);

	//memset(r, 0x33, sizeof(r));
	//memset(w, 0, sizeof(w));
	//
	//r[0] = 0;

	//for (int i = 1; i < (1 << n); i++) {
	//	int d = cnt(i);
	//	for (int j = 0; j < n; j++) if (i & (1 << j)) {
	//		r[i] = min(r[i], r[ i - (1 << j)] + v1[d-1]*v2[j]);
	//	}
	//}
	long long res = 0;
	sort(v1, v1 + n); sort(v2, v2 + n);
	for (int i = 0; i < n; i++) res += v1[i] * v2[n - 1 - i];
	cout << "Case #" << test << ": " << res << endl;
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int TEST; cin >> TEST;
	for (test = 1; test <= TEST; test++)
		solve();
	return 0;
}