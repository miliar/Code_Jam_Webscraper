#include <algorithm>
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

int n, k, dp1[50][50], dp2[50][50], dp3[50][50], dp4[50][50];
vector<string> grid;

bool won(char c) {
	SET(dp1, 0);
	SET(dp2, 0);
	SET(dp3, 0);
	SET(dp4, 0);
	FORE(i, grid) FORE(j, grid[0]) {
		if (grid[i][j] == c) {
			dp1[i][j] = (i == 0 ? 1 : 1+dp1[i-1][j]);	
			dp2[i][j] = (j == 0 ? 1 : 1+dp2[i][j-1]);
			dp3[i][j] = (i == 0 || j == 0 ? 1 : 1+dp3[i-1][j-1]);
			dp4[i][j] = (i == 0 || j == n-1 ? 1 : 1+dp4[i-1][j+1]);
		}	
	}
	FORE(i, grid) FORE(j, grid[0]) {
		if (dp1[i][j] == k || dp2[i][j] == k || dp3[i][j] == k || dp4[i][j] == k) return true;
	}
	return false;
}

int main() {
	int t;
	cin >> t;
	FOR(i, 0, t) {
		cin >> n >> k;
		grid = vector<string>(n);
		FOR(j, 0, n) cin >> grid[j];
		vector<string> ngrid = grid;
		FORE(j, grid) FORE(k, grid[0]) ngrid[k][n-j-1] = grid[j][k];
		grid = ngrid;
		//FORE(j, grid) cout << grid[j] << endl;
		for (int j = n-1; j >= 0; --j) {
			FOR(k, 0, n) {
				if (grid[j][k] == '.') continue;
				int x = j;
				while (x < n-1 && grid[x+1][k] == '.') {
					swap(grid[x][k], grid[x+1][k]);
					++x;
				}
			}
		}
		//FORE(j, grid) cout << grid[j] << endl;
		cout << "Case #" << i+1 << ": ";
		bool flag1 = won('R'), flag2 = won('B');
		if (!flag1) {
			if (!flag2) cout << "Neither\n";
			else cout << "Blue\n";
		}
		else {
			if (!flag2) cout << "Red\n";
			else cout << "Both\n";
		}
	}
}
