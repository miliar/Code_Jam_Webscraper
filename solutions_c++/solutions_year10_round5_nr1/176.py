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

const int N = 1000000;
const int M = 100000;
bool flag[N];
int prime[M];
int m;
int a[20];

void prime_gen()
{
	int i, j;
	memset(flag, 0, sizeof(flag));
	m = 0;
	for (i = 2; i < N; ++i)
	{
		if (flag[i]) continue;
		prime[m++] = i;
		for (j = i + i; j < N; j += i) flag[j] = true;
	}
}

int64 extend_gcd(int64 a, int64 b, int64& x, int64& y)
{
	int64 t;
	if (b == 0)
	{
		x = 1, y = 0; 
		return a;
	}
	int64 d = extend_gcd(b, a % b, x, y);
	t = x, x = y;
	y = t - a / b * y;
	return d;    
}

int pow10[7];
int main()
{
	freopen("A-large.in", "r", stdin); freopen("A.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	prime_gen();
	pow10[0] = 1;
	for (int i = 1; i < 7; ++i) pow10[i] = pow10[i - 1] * 10;
	for (int num = 1; num <= cas; ++num)
	{
		int D, n;
		scanf("%d %d", &D, &n);
		int low = INT_MIN;
		for (int i = 0; i < n; ++i) scanf("%d", a + i), low = max(low, a[i]);
		++low;
		if (n == 1)
		{
			printf("Case #%d: I don't know.\n", num);
			continue;
		}
		bool found = false;
		for (int i = 1; i < n; ++i)
			if (a[i - 1] == a[i])
			{
				found = true;
				break;
			}
		if (found)
		{
			printf("Case #%d: %d\n", num, a[n - 1]);
			continue;
		}
		found = false;
		int ret = -1;
		for (int i = 0; i < m && prime[i] <= pow10[D] && !found; ++i)
		{
			if (prime[i] < low) continue;
			int64 P = prime[i];
			int64 A, B;
			if (n > 2)
			{
				int64 x = a[0] - a[1];
				if (x < 0) x += P;
				int64 u, v;
				extend_gcd(x, P, u, v);
				A = (a[1] - a[2]) * u % P;
				if (A < 0) A += P;
				B = (a[1] - A * a[0]) % P;
				if (B < 0) B += P;
				int j;
				for (j = 1; j < n; ++j)
					if (a[j] != (A * a[j - 1] + B) % P) break;
				if (j == n)
				{
					if (ret < 0) ret = (A * a[n - 1] + B) % P;
					else if (ret != (A * a[n - 1] + B) % P)
					{
						found = true;
						break;
					}
				}
			}
			else
			{
				found = true;
			}
		}
		if (!found) printf("Case #%d: %d\n", num, ret);
		else printf("Case #%d: I don't know.\n", num);
	}
	return 0;
}
