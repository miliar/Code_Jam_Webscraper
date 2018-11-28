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
#include<complex>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef complex<ll> pt;

inline ll dot(const pt& A, const pt& B) {
	return A.real() * B.real() + A.imag() * B.imag();
}

inline ll cross(const pt& A, const pt& B) {
	return A.real() * B.imag() - A.imag() * B.real();
}

inline ll sign(ll n) {
	return n == 0 ? 0 : (n > 0 ? 1 : -1);
}
 
bool seg_point_inter(const pt A, const pt B, const pt P) {
	// reduction from 3 --> 2
	if(A == P || B == P) return 1;
	if(A == B) return P == A; // check
	return dot(B - A, P - A) >= 0 && dot(A - B, P - B) >= 0 
		&& cross(B - A, P - A) == 0;
}

// segment A-B and C-D
// tested srm 368-500
// NOTE: experimental
bool seg_seg_inter(pt A, pt B, pt C, pt D) {
	if(seg_point_inter(A, B, C) || seg_point_inter(A, B, D)
			|| seg_point_inter(C, D, A) || seg_point_inter(C, D, B))
		return 1;
	// if(cross(B - A, D - C) == 0) return 0;
	return sign(cross(C - A, B - A)) == -sign(cross(D - A, B - A))
		&& sign(cross(A - C, D - C)) == -sign(cross(B - C, D - C));
}

#define GET(i, m) ((1 << (i)) & m)
#define SET(i, m) ((1 << (i)) | m)
#define CLR(i, m) (~(1 << (i)) & m)

const int inf = 1000;
int N, K;
int price[128][32];
int path[128][128];

int dp2(int mask, int at, int build);

int cc[1 << 16];
int dp(int mask) {
	// cout << " mask=" << mask << endl;
	if(mask == 0) return 0;
	int& ret = cc[mask];
	if(ret >= 0) return ret;
	ret = dp2(mask, 0, 0);
	bool okay = true;
	for(int i = 0; i < N; ++i) {
		if(!GET(i, mask)) continue;
		for(int j = i + 1; j < N; ++j) {
			if(!GET(j, mask)) continue;
			if(path[i][j]) {
				okay = false;
				break;
			}
		}
		if(!okay) break;
	}
	if(okay) {
		ret = 1;
	}
	return ret;
}

int dp2(int mask, int at, int build) {
	int ret = inf;
	if(at >= N) {
		if(build != 0 && mask != 0)
			return dp(mask) + dp(build);
		return inf;
	}
	if(GET(at, mask)) {
		ret = min(ret, dp2(CLR(at, mask), at + 1, SET(at, build)));
	}
	ret = min(ret, dp2(mask, at + 1, build));
	return ret;
}

int main() {
	int T; cin >> T;
	for(int tt = 1; tt <= T; ++tt) {
		cin >> N >> K;
		for(int i = 0; i < N; ++i) {
			for(int k = 0; k < K; ++k) {
				cin >> price[i][k];
			}
		}
		memset(path, 0, sizeof(path));
		for(int i = 0; i < N; ++i) {
			for(int j = i + 1; j < N; ++j) {
				for(int k = 1; k < K; ++k) {
					pt I1(0, price[i][k-1]);
					pt I2(1, price[i][k]);
					pt J1(0, price[j][k-1]);
					pt J2(1, price[j][k]);
					if(seg_seg_inter(I1, I2, J1, J2)) {
						path[i][j] = 1;
						path[j][i] = 1;
					}
				}
			}
		}
		memset(cc, -1, sizeof(cc));
		int ans = dp((1 << N) - 1);
		cout << "Case #" << tt << ": " << ans << endl;
	}
	return 0;
}

