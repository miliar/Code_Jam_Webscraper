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
    freopen("B.in", "r", stdin);
    freopen("_.out", "w", stdout);
}

const int INF = (int)8e8;

const int MAX = 1000 + 50;
int mas[MAX];

const int MAXP = 12;
int price[MAXP][MAX];


int dyn[MAXP][MAX][MAXP];

int main()
{
    initialize();

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt) {
		int p;
		cin >> p;

		int n = (1 << p);
		for (int i = 0; i < n; ++i) {
			cin >> mas[i];
			mas[i] = p - mas[i];
		}
		for (int i = 0; i < p; ++i) {
			for (int j = 0; j < (1 << (p - i - 1)); ++j) {
				cin >> price[i][j];
			}
		}
		
		for (int i = 0; i < (1 << p); ++i) {
			for (int k = 0; k < mas[i]; ++k) {
				dyn[0][i][k] = INF;
			}
			for (int k = mas[i]; k < MAXP; ++k) {
				dyn[0][i][k] = 0;
			}
		}

		for (int level = 1; level <= p; ++level) {
			int size = (1 << (p - level));
			for (int i = 0; i < size; ++i) {
				for (int lost = 0; lost <= p; ++lost) {
					int& value = dyn[level][i][lost];
					value = INF;
					value = min(value, dyn[level - 1][i * 2][lost] + dyn[level - 1][i * 2 + 1][lost]);
					value = min(value, dyn[level - 1][i * 2][lost + 1] + dyn[level - 1][i * 2 + 1][lost + 1] + price[level - 1][i]);
					int y = 0;
				}
			}
		}
		printf("Case #%d: %d\n", tt, dyn[p][0][0]);
	}

    return 0;
}