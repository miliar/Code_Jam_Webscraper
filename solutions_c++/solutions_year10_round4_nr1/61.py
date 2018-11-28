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
const int M = N * 3;
int a[N][N];
int b[M][M];

int main()
{
	freopen("A.in", "r", stdin); freopen("A.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int num = 1; num <= cas; ++num)
	{
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
		{
			int x = 0;
			int y = n - 1 - i;
			for (int j = 0; j <= i; ++j)
			{
				scanf("%d", &a[x][y]);
				++x; ++y;
			}
		}
		for (int i = n; i < 2 * n - 1; ++i)
		{
			int x = i - n + 1;
			int y = 0;
			for (int j = 0; j < 2 * n - i - 1; ++j)
			{
				scanf("%d", &a[x][y]);
				++x; ++y;
			}
		}
		int m;
		for (m = n; m <= 3 * n; ++m)
		{
			bool over = false;
			for (int x = 0; x + n <= m && !over; ++x)
				for (int y = 0; y + n <= m && !over; ++y)
				{
					memset(b, 255, sizeof(b));
					for (int i = 0; i < n; ++i)
						for (int j = 0; j < n; ++j)
							b[x + i][y + j] = a[i][j];
					bool found = false;
					for (int i = 0; i < m && !found; ++i)
						for (int j = i + 1; j < m && !found; ++j)
						{
							if (b[i][j] < 0) continue;
							if (b[j][i] >= 0 && b[i][j] != b[j][i]) found = true;
						}
					if (found) continue;
					for (int i = 0; i < m && !found; ++i)
						for (int j = 0; i + j < m - 1 && !found; ++j)
						{
							if (b[i][j] < 0) continue;
							if (b[m - 1 - j][m - 1 - i] >= 0 && b[i][j] != b[m - 1 - j][m - 1 - i]) found = true;
						}
					if (!found) over = true;
				}
			if (over) break;
		}
		printf("Case #%d: %d\n", num, m * m - n * n);
		fprintf(stderr, "Case #%d: %d\n", num, m * m - n * n);
	}
	return 0;
}
