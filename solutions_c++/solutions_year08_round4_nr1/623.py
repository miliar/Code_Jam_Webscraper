#include <cstdio>
#include <cassert>
#include <algorithm>
#include <cstring>

using std::min;

const int MAXM = 1 << 14;

int M, V;
int dp[MAXM][2];
int IC;
bool change[MAXM];
bool initial[MAXM];

#define c1(n) ((n)*2+1)
#define c2(n) ((n)*2+2)

int dpf(int n, int v) {
	if (dp[n][v] != -1)
		return dp[n][v];
	assert(dp[n][v] == -1);
		
	//printf ("in dp %d %d\n", n, v);
	if (n >= IC) {
		if (v == initial[n]) {
			//printf ("0\n");
			return dp[n][v] = 0;
		} else {
			//printf ("inf!\n");
			//assert(M + 1 > 1);
			return dp[n][v] = M + 1;//INFINITY
		}
	}

	if (change[n]) {
		int or_val, and_val;
		if (v == 1) {
			or_val = min(dpf(c1(n), 1) + dpf(c2(n), 1)
				   , min(dpf(c1(n), 1) + dpf(c2(n), 0)
				   	   , dpf(c1(n), 0) + dpf(c2(n), 1)));
			and_val = dpf(c1(n), 1) + dpf(c2(n), 1);
		} else {
			or_val = dpf(c1(n), 0) + dpf(c2(n), 0);
			and_val = min(dpf(c1(n), 0) + dpf(c2(n), 1)
				   , min(dpf(c1(n), 1) + dpf(c2(n), 0)
				   	   , dpf(c1(n), 0) + dpf(c2(n), 0)));
		}
		
		assert(and_val >= 0 && or_val >= 0);
		if (initial[n] == 0) {//OR
			//printf ("try min<%d %d> %d %d\n", n, v, or_val, and_val);
			return dp[n][v] = min(or_val, and_val + 1);
		} else {//AND
			return dp[n][v] = min(or_val + 1, and_val);
		}
	} else {
		if (initial[n] == 0) {//OR
			if (v == 1) {
				dp[n][v] = 
					min(  dpf(c1(n), 1) + dpf(c2(n), 1)
					, min(dpf(c1(n), 1) + dpf(c2(n), 0)
						, dpf(c1(n), 0) + dpf(c2(n), 1)));
				return dp[n][v];
			} else {
				dp[n][v] = dpf(c1(n), 0) + dpf(c2(n), 0);
				return dp[n][v];
			}
		} else {//AND
			if (v == 1) {
				dp[n][v] = dpf(c1(n), 1) + dpf(c2(n), 1);
				return dp[n][v];
			} else {
				dp[n][v] = min(dpf(c1(n), 0) + dpf(c2(n), 1)
				     , min(dpf(c1(n), 1) + dpf(c2(n), 0)
				   	     , dpf(c1(n), 0) + dpf(c2(n), 0)));
				return dp[n][v];
			}
		}
	}
}

int main () {
	int tc;
	scanf ("%d", &tc);

	for (int ctc = 1; ctc <= tc; ++ctc) {
		scanf ("%d %d", &M, &V);
		IC = (M - 1) / 2;
		int i;
		for (i = 0; i < IC; ++i) {
			int x, y;
			scanf ("%d %d", &x, &y);
			initial[i] = x;
			change[i] = y;
		}
		for (; i < M; ++i) {
			int x;
			scanf ("%d", &x);
			initial[i] = x;
		}
		
		memset(dp, -1, sizeof(dp));
		dpf (0, V);
		if (dp[0][V] > M) {
			printf("Case #%d: IMPOSSIBLE\n", ctc);
		} else {
			printf("Case #%d: %d\n", ctc, dp[0][V]);
		}
	}

	return 0;
}
