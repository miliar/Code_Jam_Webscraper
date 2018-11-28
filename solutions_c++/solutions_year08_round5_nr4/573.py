#include "header.h"

void init(){
}

int xi[20], yi[20];
int DP[200][200];

const int MOD = 10007;

void solve() {
	int H, W, R;
	cin >> H >> W >> R;
	memset(DP, 0, sizeof(DP));
	
	REP(i, R) {
		cin >> yi[i] >> xi[i];
		--yi[i];
		--xi[i];
	}
	
	DP[0][0] = 1;
	REP(y, H) REP(x, W) {
		bool ok = true;
		REP(i, R) if (y == yi[i] && x == xi[i]) ok = false;
		if (!ok) continue;
		(DP[y+2][x+1] += DP[y][x]) %= MOD;
		(DP[y+1][x+2] += DP[y][x]) %= MOD;
	}
	
	cout << DP[H-1][W-1];
	
}
