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

#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()

int n, k;
vector<int> x;
const int N = 128;
int dp[N][N];

int simulate() {
	int res = 0;
	vector<bool> alive(n, true);
	for (int step = 0; step < k; step++) {
		int j = x[step];
		alive[j] = false;		
		for (int i = j - 1; i >= 0; i--) {
			if (alive[i])
				++res;
			else
				break;
		}
		for (int i = j + 1; i < n; i++) {
			if (alive[i])
				++res;
			else
				break;		
		}
	}	
	return res;
}

int dummy() {	
	sort(all(x));
	int res = simulate();
	do {
		res = min(res, simulate());
	} while (next_permutation(all(x)));
	return res;
}

int best(int left, int right, int lborder, int rborder) {
	if (left > right || lborder >= rborder)
		return 0;
	int &res = dp[left][right];
	if (res != -1)
		return res;
	res = 2 * n * k;
	for (int i = left; i <= right; i++) {
		int u = best(left, i - 1, lborder, x[i] - 1)
				+ best(i + 1, right, x[i] + 1, rborder)
				+ (rborder - x[i])
				+ (x[i] - lborder);
		res = min(res, u);
	}
	assert(res >= 0);
	return res;
}

int solve(int T) {	
	scanf("%d%d", &n, &k);
	x.resize(k);	
	for (int i = 0; i < k; i++) {
		scanf("%d", &x[i]);
		--x[i];
	}
	sort(all(x));
	for (int i = 0; i <= k; i++)	
		for (int j = 0; j <= k; j++)
			dp[i][j] = -1;
	int res = best(0, k - 1, 0, n - 1);
	//int cres = dummy();
	//if (res != cres)
	//	printf("Test %d. Recieved %d, expected %d.\n", T, res, cres);
	return res;
}

int main () {
	freopen("c.in", "r", stdin); freopen("c.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int T = 1; T <= nTests; T++)
		printf("Case #%d: %d\n", T, solve(T));
	fclose(stdin); fclose(stdout);
	return 0;
}
