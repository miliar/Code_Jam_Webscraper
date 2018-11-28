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

int W, H;
int MOD = 10007;
int R[101][101];

int find(int w, int h) {
	if (w > W || h > H) return 0;
	if (R[w][h] >= 0) return R[w][h];
	return R[w][h] = (find(w+2, h + 1) + find(w + 1, h + 2)) % MOD;
}

void solve() {
	
	cin >> H >> W;
	memset(R, 0xff, sizeof(R));
	R[W][H] = 1;
	int k;
	cin >> k;
	for (int i= 0; i < k; i++) {
		int w, h; cin >> h >> w;
		R[w][h] = 0;
	}
	cout << "Case #" << test << ": " << find(1, 1) << endl;

}

int main() {
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int T;
	cin >> T;
	for (test = 1; test <= T; test++)
		solve();
	return 0;
}