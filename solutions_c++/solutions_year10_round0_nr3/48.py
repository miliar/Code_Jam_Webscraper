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
const int d8[8][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {-1, -1}, {1, -1}, {-1, 1}};
const int d4[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
typedef complex<double> point;
inline int dcmp(double x) { return (x > EPS) - (x < -EPS); }
inline double cross(const point &a, const point &b) { return (conj(a) * b).imag(); }
inline double dot(const point &a, const point &b) { return (conj(a) * b).real(); }

const int N = 1000;
int64 dp[10][N];

int main()
{
	freopen("C-large.in", "r", stdin); freopen("C.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int num = 1; num <= cas; ++num)
	{
		int R, n;
		int64 m;
		scanf("%d %I64d %d", &R, &m, &n);
		int64 tot = 0;
		for (int i = 0; i < n; ++i) scanf("%d", &dp[0][i]), tot += dp[0][i];
		int step;
		for (step = 1; (1 << step) <= n; ++step)
			for (int i = 0; i < n; ++i)
				dp[step][i] = dp[step - 1][i] + dp[step - 1][(i + (1 << (step - 1))) % n];
		int64 ret = 0;
		int cur = 0;
		while (R--)
		{
			if (tot <= m)
			{
				ret += tot;
				continue;
			}
			int64 sum = 0;
			for (int j = step - 1; j >= 0; --j)
				if (sum + dp[j][cur] <= m)
				{
					sum += dp[j][cur];
					cur = (cur + (1 << j)) % n;
				}
			ret += sum;
		}
		printf("Case #%d: %I64d\n", num, ret);
		fprintf(stderr, "Case #%d: %I64d\n", num, ret);
	}
	return 0;
}
