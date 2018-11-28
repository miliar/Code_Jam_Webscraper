#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

#define INF 1000000000

int dp[128][256], D, M, I, n[128];

int _dp(int p, int v) {
	int i, dif, ins;

	if (dp[p][v] == -1) {

		dif = abs(v - n[p]);

		dp[p][v] = _dp(p-1, v) + D;

		for (i=0; i<=M; i++) {
			if (v-i >= 0) dp[p][v] = min(dp[p][v], _dp(p-1, v-i) + dif);
			if (v+i <= 255) dp[p][v] = min(dp[p][v], _dp(p-1, v+i) + dif);
		}

		if (M > 0) {
			for (ins=1; v-ins*M >= 0; ins++) {
				for (i=0; i<=M; i++) {
					if (v-ins*M-i >= 0) dp[p][v] = min(dp[p][v], _dp(p-1, v-ins*M-i) + dif + ins*I);
				}
			}

			for (ins=1; v+ins*M <= 255; ins++) {
				for (i=0; i<=M; i++) {
					if (v+ins*M+i <= 255) dp[p][v] = min(dp[p][v], _dp(p-1, v+ins*M+i) + dif + ins*I);
				}
			}
		}
	}
	return dp[p][v];
}

int main() {

//freopen("in.txt", "r", stdin);

int N, i, RES, t, T;

cin >> T;

for (t=1; t<=T; t++) {

cin >> D;
cin >> I;
cin >> M;
cin >> N;

for (i=1; i<=N; i++) cin >> n[i];

memset(dp, -1, sizeof(dp));
for (i=0; i<256; i++) dp[0][i] = 0;

RES = INF;
for (i=0; i<256; i++) {
	RES = min(RES, _dp(N, i));
}
cout << "Case #" << t << ": " << RES << endl;

}

return 0;
}
