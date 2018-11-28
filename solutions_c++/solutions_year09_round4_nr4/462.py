#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <set>
#include <map>
#include <math.h>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define REP(i, a, b) for (int (i) = (a); (i) <= (b); (i)++)
#define DFOR(i, a, b) for (int (i) = (a) - 1; (i) >= (b); (i)--)
#define CLR(a, b) memset(a, (b), sizeof(a))
#define VI vector <int>
#define VS vector <string>
#define PB push_back
#define MP make_pair
#define SS stringstream
#define INF 1073741824
#define PII pair <int, int>
#define ALL(a) a.begin(), a.end()
#define SZ(x) (int)x.size()

#define LL long long
#define X first
#define Y second

void init()
{
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
}

const int MAXN = 50;

int T;
int n;
int x[MAXN], y[MAXN], r[MAXN];

double calc(int a, int b, int c)
{
	double dist = sqrt(1.0 * (x[b] - x[c])*(x[b] - x[c]) + (y[b] - y[c])*(y[b] - y[c])) + 1.0 * r[b] + 1.0 * r[c];
	return max(1.0 * r[a], dist / 2.0);
}

void solvecase(int test)
{
	cout << "Case #" << test << ": ";
	cin >> n;
	CLR(r, 0);
	CLR(x, 0);
	CLR(y, 0);
	FOR(i, n) {
		cin >> x[i] >> y[i] >> r[i];
	}
	double res = 1000000000.0;
	if (n == 1)
	{
		res = 1.0 * r[0];
	}
	if (n == 2)
	{
		res = max(1.0 * r[0], 1.0 * r[1]);
	}
	if (n == 3)
	{
		res = min(res, calc(0, 1, 2));
		res = min(res, calc(1, 0, 2));
		res = min(res, calc(2, 0, 1));
	}
	printf("%.6lf\n", res);
}

void solve()
{
	cin >> T;
	FOR(i, T) solvecase(i + 1);
}

int main()
{
	init();
	solve();
	return 0;
}