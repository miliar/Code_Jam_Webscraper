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
    freopen("0.in", "r", stdin);
    freopen("_.out", "w", stdout);
}

const int MAX = 100 + 10;
bool table[2][MAX][MAX];

void print(int s)
{
	for (int i = 0; i < MAX; ++i) {
		for (int j = 0; j < MAX; ++j) {
			cout << table[s][i][j];
		}
		cout << endl;
	}
	cout << endl;
}

int main()
{
    initialize();

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt) {
		memset(table, 0, sizeof(table));
		int r;
		cin >> r;
		for (int i = 0; i < r; ++i) {
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			if (x1 > x2) swap(x1, x2);
			if (y1 > y2) swap(y1, y2);
			for (int x = x1; x <= x2; ++x) {
				for (int y = y1; y <= y2; ++y) {
					table[0][x][y] = true;
				}
			}
		}

		int t = 0;
		for (; ; ++t) {
			bool ok = false;
			int cur = t % 2, next = 1 - cur;
			for (int i = 0; i < MAX; ++i) {
				for (int j = 0; j < MAX; ++j) {
					table[next][i][j] = table[cur][i][j];
					if (i == 0 || j == 0 || (!table[cur][i - 1][j] && !table[cur][i][j - 1])) {
						table[next][i][j] = false;
					}
					if (i > 0 && j > 0 && (table[cur][i - 1][j] && table[cur][i][j - 1])) {
						table[next][i][j] = true;
					}
					if (table[next][i][j]) ok = true;
				}
			}
			//print(cur);
			if (!ok) break;
		}
		printf("Case #%d: %d\n", tt, t + 1);
	}

    return 0;
}