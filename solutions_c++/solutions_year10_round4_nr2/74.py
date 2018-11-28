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

const int N = 10;
int v[1 << N];
int a[1 << N];
int dp[1 << (N + 1)][N + 1];
int n;

int run(int u, int already)
{
	int &ret = dp[u][already];
	if (ret >= 0) return ret;
	if (u >= (1 << n))
	{
		if (already >= v[u - (1 << n)]) return ret = 0;
		return ret = INT_MAX;
	}
	ret = INT_MAX;
	int t1 = run(2 * u, already + 1);
	int t2 = run(2 * u + 1, already + 1);
	if (t1 != INT_MAX && t2 != INT_MAX) ret = min(ret, a[u] + t1 + t2);
	t1 = run(2 * u, already);
	t2 = run(2 * u + 1, already);
	if (t1 != INT_MAX && t2 != INT_MAX) ret = min(ret, t1 + t2);
	return ret;
}

int main()
{
	freopen("B.in", "r", stdin); freopen("B.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int num = 1; num <= cas; ++num)
	{
		scanf("%d", &n);
		for (int i = 0; i < (1 << n); ++i) scanf("%d", v + i), v[i] = n - v[i];
		for (int i = n - 1; i >= 0; --i)
			for (int j = 0; j < (1 << i); ++j)
				scanf("%d", a + (1 << i) + j);
		memset(dp, 255, sizeof(dp));
		printf("Case #%d: %d\n", num, run(1, 0));
//		fprintf(stderr, "Case #%d: %d\n", num, ret);
	}
	return 0;
}
