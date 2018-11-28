#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const double EPS = 1e-10;
const double PI = acos(-1.0);
typedef long long int64;
#define MP(x, y) make_pair(x, y)
#define SZ(x) ((int)(x).size())
#define sqr(x) ((x) * (x))
template<class T> T gcd(T a, T b) { for (T c; b; c = a, a = b, b = c % b); return a; }
template<class T> void out(const vector<T> &a) { for (int i = 0; i < SZ(a); ++i) cout << a[i] << " "; cout << endl; }
int countbit(int n) { return n == 0 ? 0 : 1 + countbit(n & (n - 1)); }
const int d4[8][2] = {{0, 1}, {1, 1}, {1, 0}, {1, -1}};
typedef complex<double> point;
inline int dcmp(double x) { return (x > EPS) - (x < -EPS); }
inline double cross(const point &a, const point &b) { return (conj(a) * b).imag(); }
inline double dot(const point &a, const point &b) { return (conj(a) * b).real(); }

const int N = 100;
int a[N];
int dp[N][256];

int main()
{
	freopen("B-large.in", "r", stdin); freopen("B1.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int num = 1; num <= cas; ++num)
	{
		int cost_d, cost_i, m, n;
		scanf("%d %d %d %d", &cost_d, &cost_i, &m, &n);
		for (int i = 0; i < n; ++i) scanf("%d", a + i);
		for (int i = 0; i < 256; ++i)
			dp[0][i] = abs(i - a[0]);
		for (int i = 1; i < n; ++i)
			for (int j = 0; j < 256; ++j)
			{
				dp[i][j] = dp[i - 1][j] + cost_d;
				dp[i][j] = min(dp[i][j], cost_d * i + abs(a[i] - j));
				if (m > 0)
				{
					for (int k = 0; k < 256; ++k)
						dp[i][j] = min(dp[i][j], dp[i - 1][k] + abs(j - a[i]) + cost_i * (max(0, (abs(j - k) + m - 1) / m - 1)));
				}
				else
				{
					dp[i][j] = min(dp[i][j], dp[i - 1][j] + abs(j - a[i]));
				}
			}
		int ret = n * cost_d;
		for (int i = 0; i < 256; ++i)
			ret = min(ret, dp[n - 1][i]);
		printf("Case #%d: %d\n", num, ret);
	}
	return 0;
}
