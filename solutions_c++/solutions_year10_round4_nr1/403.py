#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define sz size()

typedef long long i64;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int Max = 128;

int K;
int diam[Max][Max], d2[Max][Max];
static char table[2*Max][2*Max];

bool reflect1(int S, int x0, int y0, int& x1, int& y1)
{
	y1 = x0;
	x1 = y0;
	if (d2[x1][y1] == -1)
		d2[x1][y1] = d2[x0][y0];

	return (d2[x1][y1] == d2[x0][y0]);
}

bool reflect2(int S, int x0, int y0, int& x1, int& y1)
{
	y1 = S-1-x0;
	x1 = S-1-y0;
	if (d2[x1][y1] == -1)
		d2[x1][y1] = d2[x0][y0];

	return (d2[x1][y1] == d2[x0][y0]);
}

bool isDiamond(int S, int x0, int y0)
{
	for (int x = 0; x < S; x++)
		for (int y = 0; y < S; y++) {
			int d = -1;
			if (x >= x0 && x < x0+K && y >= y0 && y < y0+K)
				d = diam[x-x0][y-y0];
			d2[x][y] = d;
		}

	REP(x, S) REP(y, S) {
		if (d2[x][y] == -1)
			continue;

		int x1, y1;
		int x2, y2;
		int x3, y3;
		if (!reflect1(S, x, y, x1, y1)) return false;
		if (!reflect2(S, x, y, x2, y2)) return false;
		if (!reflect1(S, x2, y2, x3, y3)) return false;
	}

	return true;
}

int solve()
{
	scanf("%d\n", &K);
	for (int i = 0; i < 2*K-1; i++) {
		int nums = i+1;
		if (nums > K)
			nums = 2*K - nums;
		for (int j = 0; j < nums; j++) {
			int r = i;
			if (r >= K)
				r = K-1;
			r -= j;
			int c = i - r;
			scanf("%d", &diam[r][c]);
		}
	}

	for (int size = K; ; size++)
		for (int xOffset = 0; xOffset <= size-K; xOffset++)
		for (int yOffset = 0; yOffset <= size-K; yOffset++)
			if (isDiamond(size, xOffset, yOffset))
				return size*size - K*K;
}

int main()
{
	string file_name;
	file_name = "A-small-attempt0"; 
    freopen((file_name + ".in").c_str(), "r", stdin);
    freopen((file_name + ".out").c_str(), "w+", stdout);

	int nTest = 0;
	scanf("%d", &nTest);
	for (int iTest = 1; iTest <= nTest; iTest++) {
		printf("Case #%d: %d\n", iTest, solve());
	}

    return 0;
}
