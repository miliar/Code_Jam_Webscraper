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
    freopen("2.in", "r", stdin);
    freopen("_.out", "w", stdout);
}

const int MAX = 1000 + 10;
int mas[MAX];

int next[MAX];
int cost[MAX];

bool visited[MAX];

int main()
{
    initialize();

	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int r, k, n;
		cin >> r >> k >> n;
		for (int i = 0; i < n; ++i) {
			cin >> mas[i];
		}
		for (int i = 0; i < n; ++i) {
			int p = i;
			int s = 0;
			while (s + mas[p] <= k) {
				s += mas[p++];
				if (p == n) p = 0;
				if (p == i) break;
			}
			next[i] = p;
			cost[i] = s;
		}

		long long res = 0;
		int pos = 0;
		for (int i = 0; i < r; ++i) {
			res += cost[pos];
			pos = next[pos];
		}
		printf("Case #%d: %lld\n", t, res);
	}

    return 0;
}