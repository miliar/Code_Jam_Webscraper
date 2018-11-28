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

const int N = 1000000 + 10;
int a[N];

int main()
{
	freopen("C-large.in", "r", stdin); freopen("C.out", "w", stdout);
	a[1] = 1;
	for (int i = 2; i < N; ++i)
	{
		int low, high, mid;
		for (low = i + 1, high = 2 * i - 1; low < high; )
		{
			mid = (low + high + 1) / 2;
			if (i >= 2 * (mid - i))
			{
				low = mid;
			}
			else if (a[mid - i] >= i)
			{
				high = mid - 1;
			}
			else
			{
				low = mid;
			}
		}
		a[i] = high;
	}
	int cas;
	scanf("%d", &cas);
	for (int num = 1; num <= cas; ++num)
	{
		int A1, A2, B1, B2;
		scanf("%d %d %d %d", &A1, &A2, &B1, &B2);
		int64 ret = 0;
		for (int i = A1; i <= A2; ++i)
		{
			if (i >= B1)
			{
				int low, high, mid;
				for (low = B1 - 1, high = min(B2, i); low < high; )
				{
					mid = (low + high + 1) / 2;
					if (i > a[mid]) low = mid;
					else high = mid - 1;
				}
				ret += high - B1 + 1;
			}
			if (B2 >= i + 1)
			{
				ret += max(0, B2 - a[i]);
				ret -= max(0, B1 - 1 - a[i]);
			}
		}
		printf("Case #%d: %I64d\n", num, ret);
	}
	return 0;
}
