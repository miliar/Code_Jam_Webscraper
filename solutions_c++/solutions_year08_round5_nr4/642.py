#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>
using namespace std;

typedef vector<int> VI;
typedef struct {
	int x, y;
} point;

#define EACH(a,b) for(a = b.begin(); a !=b.end(); a++)

bool cmp(point a, point b) {
	return (a.x < b.x || (a.x == b.x && a.y < b.y));
}

long long B[16][2], L[2];
long long MOD = 10007;
int inverse[10007];
int R;

int maxPow(long long &a) {
	int res = 0;
	while(a && (a%MOD) == 0) {
		res ++;
		a /= MOD;
	}
	return res;
}

long long num(int i, long long donex, long long doney) {
	long long ans;
	B[i][0] -= donex;
	B[i][1] -= doney;
	if((B[i][0] + donex) > L[0] || (B[i][1] + doney) > L[1] || B[i][0] < 0 || B[i][1] < 0)
		ans = 0;
	else if(B[i][0] == 0 || B[i][1] == 0)
		ans = 1;
	else {
		ans = 1;
		long long nr, dr;
		int nrp, drp, pow = 0;
		for(long long y = B[i][1], z = 1; y > 0; y--, z++) {
			nr = B[i][0] + y;
			nrp = maxPow(nr);
			dr = z;
			drp = maxPow(dr);
			pow += nrp - drp;
			if(nr)
				ans *= nr % MOD;
			if(dr)
				ans *= inverse[dr % MOD];
			ans %= MOD;
		}
		assert(pow >= 0);
		if(pow > 0)
			ans = 0;
	}
	B[i][0] += donex;
	B[i][1] += doney;
	return ans;
}

int main() {
	int T;
	cin >> T;
	long long H, W, ans, tmp;
	point r[16];
	memset(inverse, -1, sizeof inverse);
	for(int i = 1; i < MOD; i++) {
		for(int j = 1; j < MOD; j++) {
			if((i * j % MOD) == 1)
				inverse[i] = j;
		}
	}
	for(int tt = 1; tt <= T; tt++) {
		cin >> H >> W >> R;
		H--, W--;
		for(int i = 0; i < R; i++) {
			cin >> r[i].x >> r[i].y;
			r[i].x--;
			r[i].y--;
		}
		sort(r, r + R, cmp);
		if((2*H - W)%3 != 0 || (2*H - W) < 0)
			cout << "Case #" << tt << ": 0\n";
		else if((2*W - H)%3 != 0 || (2*W - H) < 0)
			cout << "Case #" << tt << ": 0\n";
		else {
			B[R][0] = L[0] = (2*H - W) / 3;
			B[R][1] = L[1] = (2*W - H) / 3;
			for(int i = 0; i < R; i++) {
				if((2*r[i].x - r[i].y) % 3 != 0)
					B[i][0] = B[R][0]+1;
				else
					B[i][0] = (2*r[i].x - r[i].y) / 3;

				if((2*r[i].y - r[i].x) % 3 != 0)
					B[i][1] = B[R][1]+1;
				else
					B[i][1] = (2*r[i].y - r[i].x) / 3;
			}
			ans = 0;
			tmp = 1;
			long long donex = 0, doney = 0;
			int cnt;
			for(int i = 1; i < (1 << R); i++) {
				donex = 0, doney = 0;
				tmp = 1;
				cnt = 0;
				for(int j = 0; j < R; j++) {
					if(i & (1 << j)) {
						tmp *= num(j, donex, doney);
						tmp %= MOD;
						donex = B[j][0];
						doney = B[j][1];
						cnt ++;
					}
				}
				tmp *= num(R, donex, doney);
				tmp %= MOD;
				if(cnt % 2)
					ans += tmp;
				else
					ans += MOD - tmp;
				ans %= MOD;
			}
			ans = MOD - ans;
			ans += num(R, 0, 0);
			ans %= MOD;
			cout << "Case #" << tt << ": " << ans << endl;
		}
	}
	return 0;
}
