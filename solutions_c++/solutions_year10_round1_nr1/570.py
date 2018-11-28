#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <numeric>
#include <functional>

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>

#define FOR(i, a, b) for (int (i) = (a), _b = (b); (i) < _b; ++(i))
#define REP(i, N) FOR(i, 0, N)
#define ALL(x) (x).begin(), (x).end()
#define sz() size()
#define pb(x) push_back(x)
#define mp(a, b) make_pair(a, b)

using namespace std;

typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef vector<bool> VB;

typedef long long LL;
typedef unsigned long long ULL;

vector<string> rotate(const vector<string> &grid) {
	vector<string> ret(grid.size(), string(grid.size(), '.'));
	vector<int> cols(grid.size(), grid.size() - 1);

	for (int i = grid.size() - 1; i >= 0; --i)
		for (int j = grid.size() - 1; j >= 0; --j)
			if (grid[i][j] != '.')
				ret[cols[grid.size() - i - 1]--][grid.size() - i - 1] = grid[i][j];
	return ret;
}

bool check(const vector<string> &grid, int K, int r, int c, char ch) {
	if (r + K <= grid.size()) {
		int p = 0;
		for (int i = r; i < r + K; ++i)
			p += grid[i][c] == ch;
		if (p == K) return 1;
	}
	if (c + K <= grid.size()) {
		int p = 0;
		for (int i = c; i < c + K; ++i)
			p += grid[r][i] == ch;
		if (p == K) return 1;
	}
	if (r + K <= grid.size() && c + K <= grid.size()) {
		int p = 0;
		for (int i = 0; i < K; ++i)
			p += grid[r + i][c + i] == ch;
		if (p == K) return 1;
	}
	return 0;
}

int main() {
	int T;
	cin >> T;

	FOR (kase, 1, T + 1) {
		int N, K;
		cin >> N >> K;

		vector<string> grid(N);
		REP (i, N)
			cin >> grid[i];

		grid = rotate(grid);

		int A = 0, B = 0;
		REP (i, grid.size()) {
			REP (j, grid.size()) {
				A += check(grid, K, i, j, 'R');
				B += check(grid, K, i, j, 'B');
			}
		}

		string ret = "Neither";
		if (A && B)
			ret = "Both";
		else if (A)
			ret = "Red";
		else if (B)
			ret = "Blue";

		cout << "Case #" << kase << ": " << ret << endl;
	}
}
