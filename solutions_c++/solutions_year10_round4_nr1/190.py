#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <memory.h>
#include <set>
#include <map>
#include <cstdio>
using namespace std;
#define pb push_back
#define all(c) c.begin(), c.end()
typedef long long int64;

struct Point
{
	int x;
	int y;
	Point(int x_, int y_): x(x_), y(y_)
	{ }
};

template<class T> T sqr(const T& t) {return t * t;}
template<class T> T abs(const T& t) {return ((t > 0) ? (t) : (-t));}

void initialize()
{
    freopen("000.in", "r", stdin);
    freopen("_.out", "w", stdout);
}

const int MAX = 100 + 10;
int table[2 * MAX][2 * MAX];
int n;

bool symX[2 * MAX];
bool symY[2 * MAX];

int main()
{
    initialize();


	const int INF = int(1e9);

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt) {
		cin >> n;
	
		for (int i = 0; i < 2 * MAX; ++i) {
			for (int j = 0; j < 2 * MAX; ++j) {
				table[i][j] = -1;
			}
		}

		for (int i = 0; i < 2 * n - 1; ++i) {
			int x = i;

			int len = i + 1;
			if (i >= n) {
				len = 2 * n - i - 1; 
			}
			int y = MAX - len;
			for (int j = 0; j < len; ++j) {
				int num;
				cin >> num;
				table[x][y + 2 * j] = num;
			}
		}

		for (int i = 0; i < 2 * MAX; ++i) {
			symX[i] = symY[i] = true;
		}

		for (int i = 0; i < 2 * MAX; ++i) {
			for (int j = 0; j < 2 * MAX; ++j) {
				for (int x = 0; x < 2 * MAX; ++x) {
					int ni = 2 * x - i;
					if (ni >= 0 && ni < 2 * MAX && table[i][j] != -1 && table[ni][j] != -1 && (table[i][j] != table[ni][j])) {
						symX[x] = false;
					}
				}
				for (int y = 0; y < 2 * MAX; ++y) {
					int nj = 2 * y - j;
					if (nj >= 0 && nj < 2 * MAX && table[i][j] != -1 && table[i][nj] != -1 && (table[i][j] != table[i][nj])) {
						symY[y] = false;
					}
				}
			}
		}

		int minSum = MAX - 1;
		int maxSum = minSum + 2 * (n - 1);

		int maxDiff = MAX - 1;
		int minDiff = maxDiff - 2 * (n - 1);

		int res = INF;
		for (int i = 0; i < 2 * MAX; ++i) {
			for (int j = 0; j < 2 * MAX; ++j) {
				if (!symX[i] || !symY[j]) continue;

				int sum = i + j;
				int diff = j - i;
				int l = 0;
				l = max(l, 1 + abs(diff - minDiff));
				l = max(l, 1 + abs(diff - maxDiff));
				l = max(l, 1 + abs(sum - minSum));
				l = max(l, 1 + abs(sum - maxSum));
				if (l * l < res) {
					res = l * l;
				}
			}
		}
		res -= n * n;

		printf("Case #%d: %d\n", tt, res);
	}

    return 0;
}