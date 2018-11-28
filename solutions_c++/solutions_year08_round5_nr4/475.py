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

const int MOD = 10007;

int solve() {
	int h, w, m;
	scanf("%d%d%d", &h, &w, &m);
	vector< vector<int> > res(h, vector<int>(w));
	vector< vector<int> > bad(h, vector<int>(w));
	while (m--) {
		int r, c;
		scanf("%d%d", &r, &c);
		bad[r - 1][c - 1] = 1;
	}
	res[0][0] = 1;
	for (int r = 0; r < h; r++)
		for (int c = 0; c < w; c++) {
			if (bad[r][c]) continue;
			if (c + 2 < w && r + 1 < h) {
				res[r + 1][c + 2] += res[r][c];
				res[r + 1][c + 2] %= MOD;
			}
			if (c + 1 < w && r + 2 < h) {
				res[r + 2][c + 1] += res[r][c];
				res[r + 2][c + 1] %= MOD;
			}
		}
	return res[h - 1][w - 1];
}

int main () {
	freopen("d.in", "r", stdin); freopen("d.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int T = 1; T <= nTests; T++)
		printf("Case #%d: %d\n", T, solve());
	fclose(stdin); fclose(stdout);
	return 0;
}
