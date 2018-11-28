#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

typedef long long LL;
template <class A, class B> void CONV(A &x, B &y) { stringstream s; s << x; s >> y; }
int CMP(double a, double b) { return a < b-1e-7 ? -1 : a > b+1e-7 ? 1 : 0; }
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORE(i, v) FOR(i, 0, v.size())
#define SORT(v) sort(v.begin(), v.end())
#define SET(a, n) memset(a, n, sizeof a)

bool grid[100][100], ngrid[100][100];

int main() {
	int c;
	cin >> c;
	FOR(i, 0, c) {
		int r;
		cin >> r;
		SET(grid, false);
		FOR(j, 0, r) {
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			FOR(k, x1-1, x2) FOR(l, y1-1, y2) grid[k][l] = true;
		}
		int res = 0;
		for(;;) {
			int cnt = 0;
			FOR(j, 0, 100) FOR(k, 0, 100) {
				bool temp = grid[j][k] && (j != 0 && grid[j-1][k] || k != 0 && grid[j][k-1]) || j != 0 && grid[j-1][k] && k != 0 && grid[j][k-1];
				ngrid[j][k] = temp;
				cnt += temp;
			}
			memcpy(grid, ngrid, sizeof grid);
			++res;
			if (cnt == 0) break;
		}
		cout << "Case #" << i+1 << ": " << res << endl;
	}
}
