#include <functional>
#include <algorithm>
#include <iterator>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <cstddef>
#include <vector>
#include <bitset>
#include <cstdio>
#include <cctype>
#include <deque>
#include <stack>
#include <queue>
#include <cmath>
#include <ctime>
#include <list>
#include <map>
#include <set>

using namespace std;

#define mp make_pair
#define pb push_back
#define mref mem_fun_ref
#define bid back_inserter
#define all(x) (x).begin(), (x).end()

typedef long long LL;
typedef istringstream iss;
typedef ostringstream oss;

const long long MAXN = 502;

char start[MAXN][MAXN];
long long mas[MAXN][MAXN];
long long dp[MAXN][MAXN];
long long r, c, d;

inline long long Get(long long x, long long y)
{
	if (x < 0 || y < 0) return 0;
	else return dp[x][y];
}

long long Get(long long lx, long long ly, long long rx, long long ry)
{
	return Get(rx, ry) - Get(lx - 1, ry) - Get(rx, ly - 1) + Get(lx - 1, ly - 1);
}

const double EPS = 1e-8;

bool EQ(double a, double b)
{
	return fabs(a - b) < EPS;
}

bool Check(long long lx, long long ly, long long rx, long long ry, long long k)
{

	double xs = 0, ys = 0, ps = 0;
	for (int i = lx; i <= rx; ++ i)
	{
		LL add = Get(i, ly, i, ry);
		if (i == lx || i == rx) add -= mas[i][ly] + mas[i][ry];

		xs += add * (i + 0.5);
	}

	for (int j = ly; j <= ry; ++ j)
	{
		LL add = Get(lx, j, rx, j);
		if (j == ly || j == ry) add -= mas[lx][j] + mas[rx][j];

		ys += add * (j + 0.5);
	}

	ps = Get(lx, ly, rx, ry) - mas[lx][ly] - mas[lx][ry] - mas[rx][ly] - mas[rx][ry];

	double cx = xs / (double) ps;
	double cy = ys / (double) ps;
	return EQ(cx, lx + k / 2.0) && EQ(cy, ly + k / 2.0);

}

bool F(long long k)
{
	for (long long i = k - 1; i < r; ++ i)
	{
		for (long long j = k - 1; j < c; ++ j)
		{
			if (Check(i - k + 1, j - k + 1, i, j, k))
			{
				return true;
			}
		}
	}
	return false;
}

void Solve()
{


	cin >> r >> c >> d;

	for (long long i = 0; i < r; ++ i)
	{
		cin >> start[i];
		for (long long j = 0; j < c; ++ j)
		{
			mas[i][j] = (start[i][j] - '0') + d;
		}
	}

	dp[0][0] = mas[0][0];
	for (long long j = 1; j < c; ++ j)
	{
		dp[0][j] = dp[0][j - 1] + mas[0][j];
	}
	for (long long i = 1; i < r; ++ i)
	{
		dp[i][0] = dp[i - 1][0] + mas[i][0];
	}
	for (long long i = 1; i < r; ++ i)
	{
		for (long long j = 1; j < c; ++ j)
		{
			dp[i][j] = dp[i][j - 1] + dp[i - 1][j] + mas[i][j] - dp[i - 1][j - 1];
		}
	}

	for (long long k = min(r, c); k >= 3; -- k)
	{
		if (F(k))
		{
			cout << k << endl;
			return;
		}
	}

	cout << "IMPOSSIBLE" << endl;	
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	long long ctest;
	cin >> ctest;

	for (long long test = 0; test < ctest; ++ test)
	{
		cout << "Case #" << test + 1 << ": ";
		Solve();
	}

	return 0;
}
