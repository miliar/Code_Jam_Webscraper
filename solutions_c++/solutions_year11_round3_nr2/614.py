#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
#define pb push_back

vi pr;
bool B[10005];

__int64 minn(__int64 a, __int64 b) {
	return a < b ? a : b;
}

__int64 maxx(__int64 a, __int64 b) {
	return a > b ? a : b;
}
double minn(double a, double b) {
	return a < b ? a : b;
}

double maxx(double a, double b) {
	return a > b ? a : b;
}


int main() {
	int T;
	freopen("c:\\in.txt", "r", stdin);
	freopen("c:\\B-small-attempt0 (3).in", "r", stdin);
	freopen("c:\\B-small-attempt0 (3).out", "w", stdout);

	B[0] = B[1] = true;
	for (int i = 2; i * i < 10005; ++i) {
		if (B[i] == true) continue;
		for (int j = i * i; j < 10005; j += i) {
			B[j] = true;
		}
	}
	for (int i = 0; i < 10005; ++i) {
		if (B[i] == false) {
			pr.push_back(i);
		}
	}

	scanf("%d", &T);


	for (int testCase = 1; testCase <= T; ++testCase) {
		int L, t, N, C;
		scanf("%d%d%d%d", &L, &t, &N, &C);
		vi a(C);
		for (int i = 0; i < C; ++i) {
			scanf("%d", &a[i]);
		}

		double dp[10000][3] = {0};
		for (int i = 0; i < 10000; ++i) {
			for (int j = 0; j < 3; ++j) {
				dp[i][j] = -1;
			}
		}

		dp[0][0] = 0;
		//dp[0][1] = 0;
		//dp[0][2] = 0;
		for (int i = 1; i <= N; ++i) {
			_int64 hr = a[(i - 1) % C];

			if (i > 0) {
				dp[i][0] = dp[i-1][0] + hr * 2L;


				double t1 = maxx(0L, t - dp[i-1][0]); //time have
				double dist = t1;
				if (dp[i-1][1] > -1) {
					dp[i][1] = minn(dp[i-1][1] + hr * 2L, dp[i-1][0] + 0.5 * maxx(2 * hr - dist, 0) + t1);
				} else {
					dp[i][1] = dp[i-1][0] + 0.5 * maxx(2 * hr - dist, 0) + t1;
				}

				t1 = maxx(0L, t - dp[i-1][1]);
				dist = t1;
				if (dp[i-1][2] > -1) {
					dp[i][2] = minn(dp[i-1][2] + hr * 2L, dp[i-1][1] + 0.5 * maxx(2 * hr - dist, 0) + t1);
				} else if (dp[i-1][1] > -1) {
					dp[i][2] = dp[i-1][1] + 0.5 * maxx(2 * hr - dist, 0) + t1;
				}
			
			}
		}
		double res = 1e30;;
		for (int i = 0; i <= L; ++i) {
			res = min(res, dp[N][i]);
		}
		printf ("Case #%d: %I64d\n", testCase, (__int64)(res + 0.5));

	}

	return 0;
}