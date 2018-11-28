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

const int N = 110;
char a[N][N];
double WP[N], OWP[N], OOWP[N];

int main()
{
	freopen("A-large.in", "r", stdin); freopen("A.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int num = 1; num <= cas; ++num)
	{
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%s", a[i]);
		for (int i = 0; i < n; ++i)
		{
			int win = 0, all = 0;
			for (int j = 0; j < n; ++j)
			{
				if (a[i][j] == '1') ++win, ++all;
				else if (a[i][j] == '0') ++all;
			}
			WP[i] = (double)win / all;
		}
		for (int i = 0; i < n; ++i)
		{
			double sum = 0.0;
			int cnt = 0;
			for (int j = 0; j < n; ++j)
			{
				if (a[i][j] == '.') continue;
				int win = 0, all = 0;
				for (int k = 0; k < n; ++k)
				{
					if (k == i) continue;
					if (a[j][k] == '1') ++win, ++all;
					else if (a[j][k] == '0') ++all;
				}
				sum += (double)win / all;
				++cnt;
			}
			OWP[i] = sum / cnt;
		}
		for (int i = 0; i < n; ++i)
		{
			double sum = 0.0;
			int cnt = 0;
			for (int j = 0; j < n; ++j)
			{
				if (a[i][j] == '.') continue;
				sum += OWP[j];
				++cnt;
			}
			OOWP[i] = sum / cnt;
		}
		printf("Case #%d:\n", num);
		for (int i = 0; i < n; ++i)
			printf("%.15f\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
	}
	return 0;
}
