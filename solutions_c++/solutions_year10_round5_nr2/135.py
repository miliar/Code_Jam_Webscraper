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
    freopen("1.in", "r", stdin);
    freopen("_.out", "w", stdout);
}

long long INF2 = (long long)1e18 + 100;
const int INF = (int)1e9 + 10;

const int MAX = 100 + 10;
long long mas[MAX];

const int MAXL = 1000000;
int dyn[MAX][MAXL];

long long nod(long long a, long long b) {
	if (a == 0) return b;
	if (b == 0) return a;
	return nod(b, a % b);
}

int main()
{
    initialize();

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt) {
		long long len;
		int n;
		cin >> len >> n;
		for (int i = 0; i < n; ++i) {
			cin >> mas[i];
		}
		sort(mas, mas + n);
		for (int i = 0; i < n; ++i) {
			for (int l = 0; l < MAXL; ++l) {
				if (i - 1 >= 0) {
					dyn[i][l] = dyn[i - 1][l];
				}
				else if (l == 0) dyn[i][l] = 0;
				else dyn[i][l] = INF;
				if (l - mas[i] >= 0) {
					dyn[i][l] = min(dyn[i][l], dyn[i][l - mas[i]] + 1);
				}
			}
		}


		long long res = INF2;
		long long add = (len / mas[n - 1]);
		long long start = (len % mas[n - 1]);
		for (; start < MAXL; start += mas[n - 1])
		{
			if (dyn[n - 1][start] != INF) {
				res = min(res, dyn[n - 1][start] + add);
			}
			add -= 1;
		}
		if (res != INF2) {
			printf("Case #%d: %lld\n", tt, res);
		}
		else {
			long long nn = mas[0];
			for (int i = 1; i < n; ++i) {
				nn = nod(nn, mas[i]);
			}
			if (len % nn == 0) {
				cerr << "ERR " << tt << endl;
			}
			printf("Case #%d: IMPOSSIBLE\n", tt);
		}
	}

    return 0;
}