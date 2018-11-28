#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define mp make_pair
#define all(a) a.begin(),a.end()

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

int test;

int n, m;
char s[100][100];

int res[11][11][1 << 10];

int find(int r, int c, int cm, int nm) {
	if (r == n) return 0;
	if (c == m) return find(r + 1, 0, nm, 0);
	if (c == 0 && res[r][c][cm] >= 0) return res[r][c][cm];
	int R = 0;
	if (s[r][c] == '.' && (cm & (1 << c)) == 0) {
		int ccm = cm;
		ccm |= (1 << c); if (c > 0) ccm |= 1 << (c - 1); if (c + 1 < m) ccm |= 1 << (c + 1);
		int nmm = nm;
		if (c > 0) nmm |= 1 << (c - 1); if (c + 1 < m) nmm |= 1 << (c + 1);
		R = max(R, find(r, c + 1, ccm, nmm) + 1);
	}
	R = max(R, find( r, c + 1, cm, nm));
	if (c == 0) res[r][c][cm] = R;
	return R;
}

void solve() {
	
	cin >> n >> m;
	
	for (int i = 0; i < n; i++) cin >> s[i];
	
	memset(res, 0xff, sizeof(res));

	cout << "Case #" << test <<": " << find(0, 0, 0, 0) << endl;
}

int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	cin >> T;
	for (test = 1; test <= T; test++)
		solve();
	return 0;
}