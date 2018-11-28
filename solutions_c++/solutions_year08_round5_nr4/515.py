#include<iostream>
#include<iomanip>
#include<string>
#include<sstream>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<cmath>
#include<algorithm>

#define x first
#define y second
#define rep(i,n) for(int i=0;i<int(n);i++)

using namespace std;

typedef long long     ll;
typedef vector<int>   vi;
typedef vector<vi>    vvi;
typedef pair<int,int> pii;

void solve() {
	int mod = 10007;
	int H, W, R;
	cin >> H >> W >> R;
	vvi t(H,vi(W,1));
	vvi v(H,vi(W,0));
	while (R--) {
		int a,b;
		cin >> a >> b;
		t[a-1][b-1] = 0;
	}
	v[0][0] = 1;
	for (int i = 0; i < H; i++) {
	   for (int j = 0; j < W; j++) {
			if (t[i][j]) {
				if (i+2 < H and j+1 < W) {
					v[i+2][j+1] = (v[i+2][j+1] + v[i][j]) % mod;
				}
				if (i+1 < H and j+2 < W) {
					v[i+1][j+2] = (v[i+1][j+2] + v[i][j]) % mod;
				}
			}
			else v[i][j] = 0;
	   } 
	} 
	cout << v[H-1][W-1] << endl;;
}

int main() {
	int N;
	cin >> N;
	rep (i,N) {
		cout << "Case #" << i+1 << ": ";
		solve();
	}
}
