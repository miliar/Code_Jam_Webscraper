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

const int N = 1000000 + 10;
int a[N];
double b[N];

int main()
{
	freopen("B-small-attempt0.in", "r", stdin); freopen("B.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int num = 1; num <= cas; ++num)
	{
		int C, D;
		scanf("%d %d", &C, &D);
		int n = 0;
		for (int i = 0; i < C; ++i)
		{
			int x, cnt;
			scanf("%d %d", &x, &cnt);
			while (cnt--)
				a[n++] = x;
		}
		double low, high = 0.0;
		for (int i = 1; i < n; ++i)
			high = max(high, abs(a[i] - (a[0] + (double)i * D)));
		for (low = 0.0; high - low > 1e-8; )
		{
			double mid = (low + high) / 2;
			b[0] = a[0] - mid;
			bool found = false;
			for (int i = 1; i < n; ++i)
			{
				if (dcmp(a[i] + mid - b[i - 1] - D) < 0)
				{
					found = true;
					break;
				}
				b[i] = max(a[i] - mid, b[i - 1] + D);
			}
			if (found) low = mid;
			else high = mid;
		}
		printf("Case #%d: %.15f\n", num, high);
	}
	return 0;
}
