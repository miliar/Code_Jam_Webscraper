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
    freopen("_L.in", "r", stdin);
    freopen("_.out", "w", stdout);
}

const int MAX = 1000 + 10;
int a[MAX], b[MAX];

int main()
{
    initialize();

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt) {
		int n;
		cin >> n;
		for (int i = 0; i < n; ++i) {
			cin >> a[i] >> b[i];
		}
		int res = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = i + 1; j < n; ++j) {
				if ((a[i] < a[j] && b[i] > b[j]) || 
					(a[i] > a[j] && b[i] < b[j]))
					res++;
			}
		}
		printf("Case #%d: %d\n", tt, res);
	}

    return 0;
}