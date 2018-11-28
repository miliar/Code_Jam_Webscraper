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

int main()
{
    initialize();

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		int n, k;
		cin >> n >> k;

		printf("Case #%d: ", t + 1);
		if (k % (1 << n) == ((1<<n) - 1)) printf("ON\n");
		else printf("OFF\n");
	}

    return 0;
}