#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cassert>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;

#define SZ(x) (int)(x).size()
#define FOR(i, seq, n) for(int i = (seq); i < (n); ++i)
#define FORD(i, seq, n) for(int i = (seq); i >= (n); --i)
#define REP(i, n) for(int i = 0; i < (n); ++i)
#define REPD(i, n) for(int i = (n) - 1; i >= 0; --i)
#define ALL(x) (x).begin(), (x).end()
#define SQR(x) (x)*(x)
typedef unsigned long long u64;
typedef signed long long i64;
typedef pair<int, int> pii;
#define X first
#define Y second

long long dist[1010];
long long dp[1010][3];

long long mn(long long a, long long b) { return a<b?a:b; }
long long mx(long long a, long long b) { return a>b?a:b; }

int main()
{
	int T;
	cin >> T;
	REP (tt, T) {
		int L, N, C;
		long long t;
		cin >> L >> t >> N >> C;
		REP (j, C) {
			long long a; cin >> a;
			for (int i = j; i < N; i += C)
				dist[i] = a;
		}

		dp[0][0] = dp[0][1] = dp[0][2] = 0;
		REP (i, N) {
			dp[i + 1][0] = dp[i][0] + 4 * dist[i];
			dp[i + 1][1] = mn(dp[i][1] + 4 * dist[i], dp[i][0] + 2 * dist[i] + mx(0, t - dp[i][0] / 2));
			dp[i + 1][2] = mn(dp[i][2] + 4 * dist[i], dp[i][1] + 2 * dist[i] + mx(0, t - dp[i][1] / 2));

			//assert(dp[i+1][0] <= dp[i+1][1] && dp[i+1][1] <= dp[i+1][2]);
		}
		long long res = dp[N][0];
		if (L >= 1) res = min(res, dp[N][1]);
		if (L >= 2) res = min(res, dp[N][2]);
		cout << "Case #" << (tt + 1) << ": " << res / 2 << endl;
	}
	return 0;
}

