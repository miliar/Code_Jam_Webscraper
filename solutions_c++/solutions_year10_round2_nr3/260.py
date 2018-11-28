#include <string>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <queue>
#include <cassert>

using namespace std;

int T;
const int MOD = 100003;
const int MAXN = 510;

int choose[MAXN][MAXN];
int dp[MAXN][MAXN];

int solve(int n, int rank) {
	int &ref = dp[n][rank];
	if (ref != -1) return ref;

	if (rank == n - 1) return 1;
	if (rank == 1) return 1;

	int prevN = rank;
	int prevRank = rank - 1;
	int got = n - prevN - 1;

	ref = 0;
	for (int delta = 0; delta <= got; ++delta) {
		if (prevRank - delta >= 1) {
			ref += ((long long)(solve(prevN, prevRank - delta)) * (long long)(choose[got][delta])) % MOD;
			ref %= MOD;
		}
	}
	return ref;
}

int main(void) 
{
	scanf("%d", &T);

	choose[0][0] = 1;
	for (int i = 1; i < MAXN; ++i) 
		choose[i][0] = 1;

	for (int i = 1; i < MAXN; ++i) 
		for (int j = 1; j <= i; ++j) {
			choose[i][j] = (choose[i - 1][j] + choose[i - 1][j - 1]) % MOD;
		}

	memset(dp, -1, sizeof dp);

	for (int t = 1; t <= T; ++t) {
		int n;
		scanf("%d", &n);
		int ret = 0;
		for (int rank = 1; rank < n; ++rank) {
			ret += solve(n, rank);
			ret %= MOD;
		}
		printf("Case #%d: %d\n", t, ret);
	}

	return 0;
}