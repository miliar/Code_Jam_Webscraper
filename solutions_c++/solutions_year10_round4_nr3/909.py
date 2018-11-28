#include <algorithm>
#include <cassert>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
static const double EPS = 1e-8;
static const double PI = 4.0 * atan(1.0);
static const double PI2 = 8.0 * atan(1.0);
typedef long long ll;

#define REP(i,n) for(int i=0;i<(int)n;++i)
#define ALL(c) (c).begin(), (c).end()

static int memo[2][128][128];

int main() {
	int C;
	cin >> C;
	for (int c = 1; c <= C; ++c) {
		int R;
		cin >> R;
		memset(memo, 0, sizeof(memo));

		for (int r = 0; r < R; ++r) {
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;

			for (int x = x1; x <= x2; ++x) {
				for (int y = y1; y <= y2; ++y) {
					memo[0][x + 1][y + 1] = true;
				}
			}
		}

		int front = 1;
		int back = 0;

		int counter = 1;
		for (;; ++counter) {
			memset(memo[front], 0, sizeof(int) * 128 * 128);
			bool alive = false;
			for (int x = 1; x < 128; ++x) {
				for (int y = 1; y < 128; ++y) {
					if (memo[back][x][y]) {
						if (!memo[back][x - 1][y] && !memo[back][x][y - 1]) {
						} else {
							memo[front][x][y] = true;
							alive = true;
						}
					} else {
						if (memo[back][x - 1][y] && memo[back][x][y - 1]) {
							memo[front][x][y] = true;
							alive = true;
						}
					}
				}
			}

			//for (int y = 1; y < 10; ++y) {
			//	for (int x = 1; x < 10; ++x) {
			//		cout << memo[front][x][y];
			//	}
			//	cout << endl;
			//}
			//cout << endl;

			swap(front, back);

			if (!alive) {
				break;
			}
		}

		printf("Case #%d: %d\n", c, counter);
	}
}
