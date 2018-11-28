#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
#pragma comment(linker, "/STACK:64000000")

#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()

const int infinity = 100000000;

int n;
const int N = 20000;
int dp[N + 1][2];
vector<int> g(N + 1), c(N + 1), a(N + 1);

int solve(int at, int val) {
	int &res = dp[at][val];
	if (res != -1) return res;
	if (at > (n - 1) / 2) {//leaf
		if (val != a[at]) return res = infinity;
		return res = 0;
	}
	int res1 = infinity;
	int res2 = infinity;
	{ //AND
		if (val == 0) {
			int L0 = solve(2 * at, 0);
			int L1 = solve(2 * at, 1);
			int R0 = solve(2 * at + 1, 0);
			int R1 = solve(2 * at + 1, 1);
			res1 = min( infinity, min(L0 + R0, min(L0 + R1, L1 + R0)) );
		}
		else res1 = min(infinity, solve(2 * at, 1) + solve(2 * at + 1, 1));
	}
	{ //OR
		if (val == 1) {
			int L0 = solve(2 * at, 0);
			int L1 = solve(2 * at, 1);
			int R0 = solve(2 * at + 1, 0);
			int R1 = solve(2 * at + 1, 1);
			res2 = min( infinity, min(L1 + R1, min(L0 + R1, L1 + R0)) );
		}
		else res2 = min(infinity, solve(2 * at, 0) + solve(2 * at + 1, 0));
	}
	if (c[at] == 1) {
		if (g[at] == 1) res = min(res1, res2 + 1);
		else res = min(res1 + 1, res2);
	}
	else {
		if (g[at] == 1) res = res1;
		else res = res2;
	}
	return res;
}

int solveTestCase() {
	memset(dp, -1, sizeof(dp));
	int val;
	scanf("%d%d", &n, &val);	
	for (int i = 1; i <= (n - 1) / 2; i++)
		scanf("%d%d", &g[i], &c[i]);	
	for (int i = (n - 1) / 2 + 1; i <= n; i++)
		scanf("%d", &a[i]);
	return solve(1, val);
}

int main () {
	freopen("a.in", "r", stdin); freopen("a.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int T = 1; T <= nTests; T++) {
		int res = solveTestCase();
		printf("Case #%d: ", T);
		if (res >= infinity) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
	}
	fclose(stdin); fclose(stdout);
	return 0;
}
