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

int main()
{
	int T;
	cin >> T;
	REP (t, T) {
		int R, C;
		cin >> R >> C;
		vector<string> grid;
		int numBlue = 0;
		REP (i, R) {
			string tmp; cin >> tmp; grid.push_back(tmp);
			REP (j, C) if (tmp[j] == '#') ++numBlue;
		}

		REP (i, R - 1) REP (j, C - 1)
			if (grid[i][j] == '#' && grid[i][j + 1] == '#' &&
				grid[i + 1][j] == '#' && grid[i + 1][j + 1] == '#') {
					numBlue -= 4;
					grid[i][j] = '/';
					grid[i][j + 1] = '\\';
					grid[i + 1][j] = '\\';
					grid[i + 1][j + 1] = '/';
			}

		cout << "Case #" << (t + 1) << ":" << endl;
		if (numBlue != 0) cout << "Impossible" << endl;
		else REP (i, R) cout << grid[i] << endl;
	}
	return 0;
}

